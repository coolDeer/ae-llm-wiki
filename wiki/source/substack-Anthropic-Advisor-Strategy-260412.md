---
type: source
title: "AI IQ Soars and Costs Drop with Just One Line of Code!"
source_type: article
author: "AI Disruption"
date: "2026-04-12"
raw_path: "raw/2026-04-12/substack/260412 - AI IQ Soars and Costs Drop with Just One Line of Code!_260412120024.md"
entities:
  - "[[company/Anthropic]]"
quality: medium
tags:
  - ai
  - anthropic
  - agent
  - us
research_id: "69db8708a632f193bdad7034"
research_type: "substack"
last_updated: "2026-04-12"
---

# Anthropic Advisor Strategy（大小模型协作）分析（260412）

## 来源概要

介绍 Anthropic 在 Claude 平台推出的 Advisor Strategy（Beta）：Opus 作为后台顾问，Sonnet/Haiku 作为执行器，实现智能提升 + 成本降低的双重目标。

## 关键要点

1. **核心数据**：Sonnet + Opus Advisor 在 SWE-Bench Multilingual 比 Sonnet 单独提高 2.7pp，成本降低 11.9%。Haiku + Opus Advisor 在 BrowseComp 得分 41.2%（vs Haiku 独立 19.7%，提升 109%），成本比 Sonnet 独立降低 85%。
2. **关键判断**："大模型做顾问，小模型做执行"颠覆传统"大模型做编排，小模型做子任务"的模式，Opus 只在执行器真正卡住时介入，其余时间保持轻量运行。
3. **行业参与者行为**：此前开发者需自行摸索大小模型协作模式，Anthropic 将这一"hard-earned experience"官方化并 API 化（一行代码启用）。Advisor 每次仅输出 400–700 token 指导计划，主要长输出由 Executor 完成。
4. **与共识差异**：市场认为 Opus 用于重度任务、Sonnet/Haiku 用于轻量任务的分层使用是正常路径，但 Advisor Strategy 证明混合调用可以同时提升质量并降低成本，打破了"质量与成本的权衡"预设。
5. **时效性信号**：Advisor tool Beta 测试中，API header 为 `anthropic-beta: advisor-tool-2026-03-01`，模型版本 `advisor-20260301`。

## 重要数据点

| 组合 | Benchmark | vs 基线 | 成本变化 |
|------|-----------|---------|---------|
| Sonnet + Opus Advisor | SWE-Bench Multilingual | +2.7pp | -11.9% |
| Haiku + Opus Advisor | BrowseComp | +109% | -85% vs Sonnet |

- Advisor 只做高层指导，不调用任何工具，不生成最终输出
- `max_uses` 参数可控制 Advisor 调用上限，token 消耗单独计费

## 值得注意的观点/引语

> "Developers can instantly give their agents near-Opus-level intelligence at extremely low cost."

> "The Advisor never calls any tools itself... Its sole responsibility is to provide high-level strategic guidance."

## 结构性观察

- Advisor Strategy 本质是 AI 系统内部的"专家咨询"模式，将稀缺的高智能计算资源（Opus）集中在最关键的决策节点，而非均匀分配，与人类组织中"顾问介入关键节点"的模式同构。
- 此模式标志着 Anthropic 将平台化走向深入：不再只卖模型，而是卖"模型协作编排框架"。这向开发者展示了 Anthropic 对 Agent 系统设计的主张。

## 与现有知识的关系

### 新增信息
- Advisor Strategy 产品功能（全新）
- Haiku + Advisor 的极端成本效率数据

### 印证之前观点
- Anthropic 持续在 API 层创新，强化 B 端开发者生态

### 矛盾/需修正
- 无

## 后续跟进项

- Advisor Strategy 正式发布时间
- 企业采用率跟踪

## 引用来源

- 原文：raw/2026-04-12/substack/260412 - AI IQ Soars and Costs Drop...
