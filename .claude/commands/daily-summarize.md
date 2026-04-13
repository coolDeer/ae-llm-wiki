---
description: 资深投资经理 (PM) 视角的每日简报 — IC briefing 格式，9 章节，含 sizing/止损/路演要点
argument-hint: "[YYYY-MM-DD]"
---

# daily-summarize

资深投资经理（PM）视角的每日简报。在 `/daily-review` 完成后调用，把 epistemic 复盘转换为 operational 决策简报，输出 `wiki/output/daily-summarize-{date}.md`。

## 参数

`$ARGUMENTS` 可选，日期 `YYYY-MM-DD`，留空取当天（Asia/Shanghai）。

## 9 个固定章节

| § | 章节 | 内容 |
|---|---|---|
| §1 | 执行摘要 | 3-5 句话 + 1 个明确行动建议 |
| §2 | 市场快照 | 跨资产 1-line（股/债/大宗/汇率/宏观）|
| §3 | 组合影响评估 | 遍历 portfolio.md / active thesis，每仓位标 强利好/利好/中性/利空/强利空 |
| §4 | 新建仓建议 | 1-3 个，A/B/C 优先级，**完整可执行单据**（sizing / 入场 / 止损 / 目标 / 催化剂 / 风险）|
| §5 | 减仓 / 对冲 | 优先动现有头寸，标紧急/一般/监控 |
| §6 | 风险预警 | invalidation 接近触发 / 新增 tail risk / cross-position correlation |
| §7 | 催化剂日历 | 前瞻 1-2 周财报 / 政策 / 产品发布 |
| §8 | 研究任务清单 | 复用 daily-review Q6，分配 owner + 截止日 |
| §9 | 路演要点 | 3-5 条立即可用于 IC / LP / 客户的话 |

末尾强制 **Self-Check**：sizing 合理性 / liquidity 可执行性 / cross-correlation 隐含风险 / vs 上次 brief 一致性

## 执行步骤

1. **确定日期**
2. **检查前置** — Glob `wiki/source/*-{date短码}.md`；同日 `daily-review-{date}.md` 强烈建议存在（不存在则提示先 `/daily-review`，允许 fallback）
3. **读持仓锚点** — 优先 `wiki/portfolio.md`，fallback 到 `wiki/thesis/` active，再 fallback 到 hypothetical
4. **建立 mental map** — `wiki/index.md` + `wiki/log.md` 最近 5 条
5. **读 source + daily-review** — 重点提取 daily-review 的 Q4/Q5/Q6
6. **逐章节作答** — §1-§9 + Self-Check
7. **写文件** — `wiki/output/daily-summarize-{YYYY-MM-DD}.md`
8. **更新 index.md** — Output 表新增一行
9. **追加 log.md** — `## [YYYY-MM-DD] daily-summarize | PM 简报`，简述 §1 / §4 首选 / §5 首选 / §6 最大风险 / §9 第一条

## 重要约束

- **章节顺序固定**
- **§4 / §5 必须给完整可执行单据**——sizing + 入场 + 止损 + 目标
- **§3 必须 reference portfolio.md 或 active thesis**
- **§9 路演要点必须立即可用**（直接 copy 进 IC slide 不需修改）
- **Self-Check 4 项缺一不可**
- **如 daily-review 同日已生成，必须引用 Q4/Q5/Q6**——daily-summarize 是它的"决策化转换"
- **如有紧急行动**（§4/§5 优先级 = 紧急），必须在 §1 突出
- **不修改 source / entity / portfolio 页面**——只读综合，输出只在 `wiki/output/`

## 与其他 skill 的关系

- `/fetch-reports` → ingest → `/daily-review` → **`/daily-summarize`** 是标准日循环
- daily-review = epistemic（学习），daily-summarize = operational（决策）
- 两者形成 epistemic → operational 流水线

## 相关文件

- `skills/daily-summarize/SKILL.md` — 完整 skill 定义
- `skills/daily-review/SKILL.md` — 上游 epistemic 复盘
- `wiki/portfolio.md` — PM 持仓锚点（PM 自维护）
- `CLAUDE.md` / `AGENTS.md` — wiki schema
