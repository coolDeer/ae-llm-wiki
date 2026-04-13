---
type: portfolio
name: "投资经理持仓 / 假想组合"
strategy: "long-only China-Asia tech & macro multi-strategy"
base_currency: "USD"
total_aum: ""
last_updated: "2026-04-13"
---

# 投资经理持仓 / 假想组合

> 本文件由 PM 自维护。`daily-summarize` skill 的 §3（组合影响评估）会读取本文件作为持仓锚点。
> 如本文件为空或未维护，daily-summarize 会 fallback 到 `wiki/thesis/` 中 status=active 的 thesis；如均无，fallback 到 hypothetical 组合。
>
> **使用建议**：手工维护一个简化版（不需要真实金额，只需要相对权重和方向），让 PM 简报有"组合影响"可言。

---

## 当前持仓（Active Positions）

> 状态：暂未填写。下方提供模板示例供 PM 参考填写。

### 模板示例

| 标的 | 方向 | 仓位 % | 入场日期 | 入场价 | 当前价 | 止损位 | 目标位 | thesis 链接 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| [[company/NVIDIA]] (NVDA US) | long | 8% | 2026-01-15 | $1,150 | $1,420 | $1,050 | $1,800 | [[thesis/NVIDIA-Rubin-cycle]] | 核心仓 |
| [[company/Anthropic]] (private) | long | — | — | — | — | — | — | [[thesis/Anthropic-B端深化]] | 不可投，仅跟踪 |
| [[company/宁德时代]] (300750.SZ) | long | 5% | 2025-11-20 | ¥210 | ¥248 | ¥190 | ¥320 | [[thesis/CATL-海外渗透]] | 核心仓 |
| [[company/Tsuruha Holdings 3391]] | long | 3% | 2026-04-13 | ¥9,800 | ¥9,800 | ¥8,500 | ¥12,000 | [[thesis/Tsuruha-整合]] | 新建仓 |

---

## 已平仓 / 历史头寸（Closed Positions）

> 用于 daily-summarize Self-Check 4（vs 上次 brief 一致性）。

| 标的 | 方向 | 入场→出场 | PnL | 平仓原因 |
|---|---|---|---|---|

（暂无）

---

## 关注 watchlist（Pre-position Pipeline）

> 已纳入跟踪、尚未建仓的标的。daily-summarize §4 新建仓建议会优先从 watchlist 中提取。

| 标的 | 关注理由 | 关键催化剂 | 期待入场区间 | 备注 |
|---|---|---|---|---|

（暂无）

---

## 风控约束（Risk Constraints）

| 约束 | 上限 |
|---|---|
| 单一标的仓位 | ≤ 5% |
| 单一行业敞口 | ≤ 25% |
| 单一国家敞口 | ≤ 40% |
| 总杠杆率 | ≤ 1.0x（long-only，无杠杆）|
| Cash 比例 | ≥ 5% |
| 单日组合 VaR (95%) | ≤ 2% NAV |

> 这些是 daily-summarize Self-Check 1（sizing 合理性）的硬指标。任何新建仓建议触碰上限必须显式标注。

---

## 当前组合 vs Benchmark

> Benchmark 待定。建议设为 MSCI AC Asia ex-Japan 或自定义"AI + China consumer + Japan equity 50/30/20"组合。
