#!/usr/bin/env python3
"""
从 aecapllc 研究平台拉取每日研究内容到 raw/ 目录。

用法:
    python scripts/fetch_reports.py              # 拉取当天
    python scripts/fetch_reports.py 2026-04-12   # 拉取指定日期
    python scripts/fetch_reports.py --dry-run    # 只列出不下载
    python scripts/fetch_reports.py --json       # JSON 格式输出统计

目录规则:
    raw/{date}/{researchTypeName}/{原始文件名}.md

逻辑:
    1. 调 /research/daily/list 获取列表
    2. 遍历每条记录，若 mdReportUrl 非空则下载
    3. 为空则跳过（通常是未生成 markdown 的条目）
    4. 已存在的文件直接跳过，避免重复下载

仅使用 Python 标准库，无外部依赖。
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

# 忽略 SSL 证书校验（macOS Homebrew Python 常见问题）
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

API_URL = "https://api.aecapllc.com/aecapllc-service/common/research/daily/list"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_ROOT = PROJECT_ROOT / "raw"
CST = timezone(timedelta(hours=8))  # Asia/Shanghai


def today_cst() -> str:
    return datetime.now(CST).strftime("%Y-%m-%d")


def safe_filename(name: str) -> str:
    """清理文件名中的非法字符，保留中文和常见符号。"""
    name = re.sub(r'[/\\:*?"<>|]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def extract_filename_from_url(url: str) -> str:
    """从 S3 URL 中提取文件名（URL 已编码，需要解码后处理）。"""
    path = urllib.parse.urlparse(url).path
    filename = urllib.parse.unquote(path.split("/")[-1])
    return safe_filename(filename)


def http_get_json(url: str, params: dict, timeout: float = 30.0) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"Content-Type": "application/json", "User-Agent": "llm-wiki-fetcher/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_list(date: str | None) -> list[dict]:
    params = {"date": date} if date else {}
    payload = http_get_json(API_URL, params)
    if payload.get("code") != 200:
        raise RuntimeError(f"API error: {payload.get('message')}")
    return payload.get("data") or []


def encode_url(url: str) -> str:
    """对 URL path 做百分号编码，处理包含空格或特殊字符的 S3 链接。"""
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parts.path, safe="/")
    query = urllib.parse.quote(parts.query, safe="=&")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, query, parts.fragment))


def write_sidecar(target: Path, item: dict) -> None:
    """在下载文件旁写 {filename}.meta.json，记录 API 原始元数据。"""
    sidecar = target.with_name(target.name + ".meta.json")
    md = item.get("metadata") or {}
    meta = {
        "research_id": md.get("researchId"),
        "research_type": md.get("researchTypeName"),
        "title": md.get("title"),
        "md_url": item.get("mdReportUrl"),
        "fetched_at": datetime.now(CST).isoformat(timespec="seconds"),
        "raw": item,
    }
    sidecar.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def download(url: str, target: Path, timeout: float = 60.0) -> bool:
    """下载文件到 target。成功返回 True，失败 False。"""
    try:
        req = urllib.request.Request(encode_url(url), headers={"User-Agent": "llm-wiki-fetcher/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("wb") as f:
                while True:
                    chunk = r.read(64 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"  ✗ 下载失败: {url}\n    {e}", file=sys.stderr)
        return False


def process(date: str, *, dry_run: bool = False) -> dict:
    items = fetch_list(date)
    print(f"[{date}] 获取到 {len(items)} 条记录")

    stats = {
        "total": len(items),
        "downloaded": 0,
        "skipped_no_md": 0,
        "skipped_exists": 0,
        "failed": 0,
        "new_files": [],
        "by_type": {},
    }

    for item in items:
        md_url = item.get("mdReportUrl")
        meta = item.get("metadata") or {}
        title = meta.get("title", "(no title)")
        research_type = meta.get("researchTypeName") or "unknown"

        if not md_url:
            stats["skipped_no_md"] += 1
            print(f"  ⊝ 跳过（无 md）: [{research_type}] {title}")
            continue

        filename = extract_filename_from_url(md_url)
        target = RAW_ROOT / date / research_type / filename
        rel = target.relative_to(PROJECT_ROOT)

        if target.exists():
            sidecar = target.with_name(target.name + ".meta.json")
            if not sidecar.exists():
                write_sidecar(target, item)
                print(f"  + 补写 sidecar: {sidecar.relative_to(PROJECT_ROOT)}")
            stats["skipped_exists"] += 1
            print(f"  = 已存在: {rel}")
            continue

        if dry_run:
            print(f"  → 将下载: {rel}")
            stats["new_files"].append(str(rel))
            stats["by_type"].setdefault(research_type, []).append(str(rel))
            continue

        if download(md_url, target):
            write_sidecar(target, item)
            stats["downloaded"] += 1
            stats["new_files"].append(str(rel))
            stats["by_type"].setdefault(research_type, []).append(str(rel))
            print(f"  ✓ {rel}")
        else:
            stats["failed"] += 1

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch daily research reports.")
    parser.add_argument(
        "date",
        nargs="?",
        default=None,
        help="日期 YYYY-MM-DD，默认当天（Asia/Shanghai）",
    )
    parser.add_argument("--dry-run", action="store_true", help="只列出，不下载")
    parser.add_argument("--json", action="store_true", help="JSON 格式输出统计")
    args = parser.parse_args()

    date = args.date or today_cst()
    stats = process(date, dry_run=args.dry_run)

    print()
    if args.json:
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        print(
            f"完成: 新下载 {stats['downloaded']} / "
            f"已存在 {stats['skipped_exists']} / "
            f"无 md {stats['skipped_no_md']} / "
            f"失败 {stats['failed']}"
        )
        if stats["by_type"]:
            print("\n按类型汇总:")
            for rtype, files in stats["by_type"].items():
                print(f"  [{rtype}] {len(files)} 份")

    return 0 if stats["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
