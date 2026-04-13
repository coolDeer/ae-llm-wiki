---
description: 资深投资者视角的每日复盘 — 7 个标准问题基于 wiki 自动作答
argument-hint: "[YYYY-MM-DD]"
---

# daily-review

资深投资者视角的每日复盘。基于当日 ingest 的 wiki 内容（source + entity 页面），针对 7 个固定问题逐一回答，输出 `wiki/output/daily-review-{date}.md`。

## 参数

`$ARGUMENTS` 可选，日期 `YYYY-MM-DD`，留空取当天（Asia/Shanghai）。

## 7 个标准问题

| # | 问题 | 目的 |
|---|---|---|
| Q1 | 今天最大的认知变化是什么？（vs wiki 既有观点；矛盾 / 印证 / 净新）| 识别拐点 |
| Q2 | 哪个数据点最反共识？Expectation gap 在哪里？ | 抓 alpha |
| Q3 | 跨板块串联：source 之间交叉印证 / 矛盾？强化或削弱了哪条 theme？ | 主题编织 |
| Q4 | 如果必须新建 1 个仓位，最高确信度方向？标的 / 催化剂 / 时间窗口 / 止损 | actionable long |
| Q5 | 如果必须减仓 / 翻空 1 个仓位，最该动的是什么？为什么？ | actionable short |
| Q6 | 最大的知识缺口 + 应主动获取的信息 + 需二手验证的 source | 驱动下轮 ingest |
| Q7 | 自我红队：confirmation bias / 集体性来源偏差 / "希望它真"的判断 / wiki 自我强化（含 sell-side 占比硬指标 + 7 天冷却期） | 防自我强化 |

## 执行步骤

1. **确定日期** — `$ARGUMENTS` 为空时取当天（Asia/Shanghai 时区）
2. **检查前置** — Glob `wiki/source/*-{日期短码}.md`，确认有当日 source；没有则提示先 `/fetch-reports` + ingest
3. **建立 mental map** — Read `wiki/index.md` + `wiki/log.md` 最近 3 条
4. **读当日 source 页** — Glob 所有当日 source，Read 或 Grep `## 关键要点` / `## 结构性观察` / `## 与现有知识的关系`
5. **逐问作答** — 严格按 `skills/daily-review/SKILL.md` 中每问的格式要求：
   - Q1：每条标 ⚠️ 矛盾 / ✓ 印证 / ✦ 净新
   - Q2：至少 3 条 expectation gap，按 surprise 强度排序
   - Q3：至少 3 条 cross-source 串联，每条 ≥ 2 份 source
   - **Q4 / Q5 不许空话**——必须给 [[company/具体标的]] + 催化剂 + 时间窗口 + 风险 + 止损
   - Q6：3-5 个缺口，每条带"如何获取"
   - Q7：至少 2 条具体的 red-team 反问
6. **写文件** — `wiki/output/daily-review-{YYYY-MM-DD}.md`，遵循 SKILL.md 中的 frontmatter 和章节结构
7. **更新 index.md** — Output 表新增一行
8. **追加 log.md** — `## [YYYY-MM-DD] daily-review | 7 问复盘`，简述 Q1 / Q2 / Q4 / Q5 / Q6 一行总结

## 重要约束

- **问题集固定**——不根据当天素材改问题、加问题、删问题
- **所有断言可追溯**——`（来源：[[source/...]]）`
- **Q4 / Q5 必须具体**——具体 ticker / 具体逻辑 / 具体止损
- **Q7 必须真 red team**——包含两条硬指标：
  1. **Sell-side 占比硬指标**：计算今天 source 中 meeting_minutes / broker_report 占比；≥ 50% 必须显式警示
  2. **7 天冷却期**：引用 `wiki/comparison/` 或 `wiki/output/` 时，若目标 `last_updated` < 7 天，**不得作为 anchor**——只能作为"今天 query 的副产品"提及。防止 wiki 自我强化（循环论证）
- **不要修改任何 source 或 entity 页面**——daily-review 是只读综合，输出只在 `wiki/output/`
- **如果触发重大叙事修正**——建议在 Q1 末尾 + 总结里提示"建议归档为 comparison 页"

## 与其他 skill 的关系

- `/fetch-reports` → ingest → `/daily-review` 是标准日循环
- `/daily-review` 与 `投资总结报告-{date}.md` 互补：前者短而精（7 问），后者全而长（综合报告）
- 重大叙事修正可触发 `wiki/comparison/` 页面创建（如 [[comparison/2026-04-12-vs-04-13-叙事修正]]）

## 相关文件

- `skills/daily-review/SKILL.md` — 完整 skill 定义和问题集说明
- `CLAUDE.md` / `AGENTS.md` — wiki schema
