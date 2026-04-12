---
description: 从 aecapllc 平台拉取每日研究报告到 raw/ 目录
argument-hint: "[YYYY-MM-DD]"
---

# fetch-reports

从 aecapllc 研究平台获取每日研究内容并下载到 `raw/` 目录。

## 参数

用户可能提供一个可选日期参数 `$ARGUMENTS`：
- 空 → 拉取当天（Asia/Shanghai 时区）
- `YYYY-MM-DD` → 拉取指定日期

## 执行步骤

1. **运行拉取脚本**

   如果 `$ARGUMENTS` 为空：
   ```bash
   python3 scripts/fetch_reports.py
   ```

   如果 `$ARGUMENTS` 有值：
   ```bash
   python3 scripts/fetch_reports.py $ARGUMENTS
   ```

2. **脚本行为说明**

   - 调用 `GET https://api.aecapllc.com/aecapllc-service/common/research/daily/list?date=...`
   - 遍历 `data[]`，判断每条记录的 `mdReportUrl`：
     - 非空 → 下载到 `raw/{date}/{researchTypeName}/{原始文件名}.md`
     - 空 → 跳过（通常是未生成 markdown 的条目）
   - 每份下载文件同目录额外写一个 `{原始文件名}.md.meta.json` sidecar（记录 `research_id` / `research_type` / `title` / `md_url` / `fetched_at` 及完整原始 item）；若文件已存在但 sidecar 缺失会自动补写
   - 已存在的文件不会重复下载（幂等）
   - 最后打印统计：新下载 / 已存在 / 无 md / 失败

3. **处理结果**

   脚本运行后，向用户报告：
   - 本次新下载了多少份报告
   - 按 `researchTypeName` 分类列出新增文件
   - 询问用户是否立即对新文件执行 ingest 流程（遵循 `CLAUDE.md` 中 ingest 工作流）

## 注意

- **不要** 在未确认的情况下直接 ingest——先让用户看到新文件清单，由用户决定是否继续
- 脚本为纯标准库实现，无需额外依赖
- 下载失败时脚本会继续处理其他文件，不要因为个别失败就中断整个流程
