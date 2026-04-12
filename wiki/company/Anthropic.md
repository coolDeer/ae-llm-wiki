---
type: company
name: "Anthropic"
ticker: ""
exchange: ""
sector: "AI / 人工智能"
sub_sector: "大模型 / Foundation Models"
market_cap: "非上市，估值约 $60B（2025 年融资轮）"
founded: "2021"
hq: "San Francisco, USA"
key_people: []
tags:
  - ai
  - saas
  - enterprise-software
  - us
sources:
  - "[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]"
  - "[[source/大模型商业模式-Token价值光谱-260410]]"
  - "[[source/Verdent-AI-Coding访谈-260410]]"
last_updated: "2026-04-11"
confidence: medium
---

# Anthropic

## 公司概况

Anthropic 是一家总部位于旧金山的 AI 安全公司，成立于 2021 年，核心产品为 Claude 系列大语言模型。公司定位为 "AI safety" 优先的基础模型公司，同时积极推进企业级商业化。

## 商业模式

Anthropic 采用多层次的商业模式：

### 消费端
- **Free 版**：基础功能免费
- **Pro 版**：$20/月，个人高级功能
- **Max 版**：$100-200/月，面向重度用户

### 企业端
- **Team 版**：$25/seat/月
- **Enterprise 版**：seat + consumption 混合计费
- **API**：按 token 计价，分三档模型

### API 定价（per million tokens，输入/输出）

| 模型 | 输入 | 输出 |
|------|------|------|
| Opus | $15 | $75 |
| Sonnet | $3 | $15 |
| Haiku | $0.25 | $1.25 |

Batch 处理享受 50% 折扣，prompt caching 最高 90% 折扣。

### 分发渠道
- 80%+ 收入通过 AWS Bedrock / Google Vertex 云市场实现
- "Land and expand" PLG 策略
- 60%+ 企业部署通过云市场完成

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 财务摘要

### 收入结构
- 云市场渠道收入占比 80%+
- API 按用量计费 + 订阅混合模式

### 关键财务指标

| 指标 | 2026E | 2025 | 同比变化 |
|------|-------|------|----------|
| ARR | $4B+ | ~$1B | ~4x |

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 产品矩阵

- **Claude API**：Compliance API、[[concept/MCP|MCP]]、100 万 token 上下文窗口
- **Claude Code**：CLI pair programmer，在初创公司中采用率 70-75%
- **Claude Co-work**：面向非技术人员的 GUI 工具
- **Legal Plugin**：法律行业垂直产品
- **Managed Agents API**：托管 AI agent 服务

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 竞争格局

- **vs Microsoft Copilot**：Claude Code 在初创公司中采用率 70-75%，超越 GitHub Copilot。50 人开发团队年均生产力差距约 $5M。Claude 于 2026 年初成为 M365 Copilot 默认模型。
- **多模型策略兴起**：企业客户越来越倾向于同时使用多个模型。

### 合作伙伴生态
- 总投资 $100M
- Accenture Anthropic Business Group (AABG)：约 30,000 名经培训专业人员
- [[concept/MCP|MCP]] 将集成复杂度降低 80%

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 估值

非上市公司。最近一轮融资估值约 $60B（2025 年）。

## 风险因素

- 大模型竞争加剧（OpenAI、Google、Meta 等）
- 高额研发和算力投入，盈利时间线不确定
- 对 AWS/Google 云市场渠道的依赖度高（80%+ 收入）
- AI 监管风险

## 催化剂

- 2026 ARR 达到 $4B+ 目标的实现进度
- Claude 在 M365 Copilot 中默认集成后的市场扩展
- 企业 "seat-apocalypse" 加速 SaaS 预算向 AI 工具转移
- AI agent 对人力成本的替代（15-20% 成本，40-45% 岗位替代）

## 关键时间线

| 日期 | 事件 |
|------|------|
| 2021 | 公司成立 |
| 2025 | 融资，估值约 $60B |
| 2026 年初 | Claude 成为 M365 Copilot 默认模型 |
| 2026 | ARR 目标 $4B+（4x YoY） |

## 相关页面

- [[industry/AI基础设施|AI 基础设施]]
- [[concept/MCP|MCP]]

## 引用来源

- [[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]
