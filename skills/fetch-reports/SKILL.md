---
name: fetch-reports
description: 从 aecapllc 研究平台拉取每日研究内容到 raw/ 目录。接受可选日期参数（YYYY-MM-DD），默认当天（Asia/Shanghai）。按 {date}/{researchTypeName} 组织文件，每份文件同目录写一份 {filename}.meta.json sidecar 记录 research_id/research_type/title 等元数据，跳过没有 markdown 版本的条目，不重复下载已存在文件。
argument-hint: "[YYYY-MM-DD]"
---

# fetch-reports

从 aecapllc 研究平台获取每日研究内容并下载到 `raw/` 目录。

## 用途

每日研究的入口 skill：
- 分析师早上通过此 skill 拉取前一天/当天的新增研究报告
- 定时任务可直接调用底层脚本，无人值守拉取
- 拉取完成后交由 `CLAUDE.md` 中定义的 ingest 工作流处理

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `$ARGUMENTS` | 否 | 日期 `YYYY-MM-DD`，留空则拉取当天（Asia/Shanghai） |

## 依赖

- 仅依赖 Python 3 标准库，无需 pip 安装任何包
- 需要项目根目录存在 `raw/` 和 `scripts/fetch_reports.py`

## 执行步骤

1. **运行拉取脚本**

   - `$ARGUMENTS` 为空：
     ```bash
     python3 scripts/fetch_reports.py
     ```
   - `$ARGUMENTS` 有值：
     ```bash
     python3 scripts/fetch_reports.py $ARGUMENTS
     ```

2. **脚本行为**

   - 调用 `GET https://api.aecapllc.com/aecapllc-service/common/research/daily/list?date=...`
   - 遍历 `data[]`：
     - `mdReportUrl` 非空 → 下载到 `raw/{date}/{researchTypeName}/{原始文件名}.md`
     - `mdReportUrl` 为空 → 跳过（通常是未生成 markdown 的条目）
   - 每份下载文件同目录额外写一个 `{原始文件名}.md.meta.json` sidecar，记录 `research_id` / `research_type` / `title` / `md_url` / `fetched_at` 以及完整原始 API item；若文件已存在但 sidecar 缺失，会自动补写
   - 已存在的文件不会重复下载（幂等）
   - 打印统计：新下载 / 已存在 / 无 md / 失败

3. **处理结果**

   脚本运行后向用户报告：
   - 本次新下载了多少份报告
   - 按 `researchTypeName` 分类列出新增文件
   - 询问用户是否立即对新文件执行 ingest 流程（遵循 `CLAUDE.md` 中 ingest 工作流）

## 重要约束

- **不要** 在未确认的情况下直接 ingest——先让用户看到新文件清单，由用户决定是否继续
- 下载失败时脚本会继续处理其他文件，不要因为个别失败就中断整个流程
- 脚本已禁用 SSL 证书校验，以兼容 macOS Homebrew Python 的证书问题

## 相关文件

- `scripts/fetch_reports.py` — 拉取逻辑实现
- `.claude/commands/fetch-reports.md` — Claude Code 的 slash command 入口（内容与本文件一致）
- `CLAUDE.md` — ingest 工作流定义
