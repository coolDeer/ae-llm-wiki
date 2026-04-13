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
  - "[[source/acecamp-Anthropic-ARR-算力合作-260412]]"
  - "[[source/substack-Anthropic-Advisor-Strategy-260412]]"
last_updated: "2026-04-12"
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

| 指标 | 数值 | 时间 |
|------|------|------|
| ARR | ~$30 亿 | 2025-06 |
| ARR | ~$90 亿 | 2025-12 |
| ARR | ~$190 亿 | 2026-02 |
| ARR | $300 亿+ | 2026-04 |
| ARR（作者预期年底） | $550–650 亿 | 2026E |

> ⚠️ 更新（2026-04-12）：原 ARR $4B+（2026E）严重低估，实际 2026Q2 已达 $300 亿+，4 个月增长 233%。（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]）

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]，[[source/acecamp-Anthropic-ARR-算力合作-260412]]）

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

## 算力战略

> ⚠️ 更新（2026-04-12）：Anthropic 与博通（Broadcom）和谷歌达成战略算力合作。（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]）

- 博通基于谷歌 TPU 规格开发定制芯片，合同有效期至 2031 年
- 2027 年起 Anthropic 将获约 **3.5 GW** 算力（约相当于多个大型超算中心）
- 三方合作覆盖"芯片设计–生产制造–算力部署"全链条闭环
- 意义：被视为"去英伟达化"ASIC 路线的标志性事件，首次对英伟达 GPU 垄断形成系统性挑战

### Advisor Strategy（新产品）

2026 年 3 月推出 Beta 功能：Opus 作为后台 Advisor（顾问），Sonnet/Haiku 作为 Executor（执行器）。

- Sonnet + Opus Advisor：SWE-Bench 提升 2.7pp，成本降低 11.9%
- Haiku + Opus Advisor：BrowseComp 得分翻倍（+109%），成本比 Sonnet 单独降低 85%

（来源：[[source/substack-Anthropic-Advisor-Strategy-260412]]）

## 政府与监管

> ⚠️ 更新（2026-04-12）：两个重要事件。（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]）

1. **五角大楼争议**：美国政府将 Anthropic 列为供应链风险（因 AI 安全防护栏僵持），已有超百家企业客户表达顾虑，Anthropic 称可能损失数十亿美元收入。
2. **英国橄榄枝**：英国科技部已拟定方案（扩大伦敦办公室、推动英美双重上市），斯塔默政府支持，聘前首相苏纳克为高级顾问，计划 CEO 阿莫代伊 5 月底访英时提交。

## 估值

非上市公司。最近一轮融资估值约 $60B（2025 年）。2026 年 4 月 ARR 已达 $300 亿+，全年 ARR 轨迹将大幅重估估值。

## 风险因素

- 大模型竞争加剧（OpenAI、Google、Meta 等）
- 高额研发和算力投入，盈利时间线不确定
- 对 AWS/Google 云市场渠道的依赖度高（80%+ 收入）
- AI 监管风险
- 五角大楼供应链风险标签导致企业客户顾虑（更新 2026-04-12）
- 区域访问限制和封号策略限制全球增长（自我设限）

## 催化剂

- ARR 高速增长轨迹（4 个月 +233%）
- Advisor Strategy 产品化带动 API 更深度使用
- 3.5 GW 算力 2027 年上线，打通算力瓶颈
- 英国双重上市计划（若推进）
- Claude 在 M365 Copilot 中默认集成后的市场扩展

## 关键时间线

| 日期 | 事件 |
|------|------|
| 2021 | 公司成立 |
| 2025 | 融资，估值约 $60B |
| 2025-06 | ARR 约 $30 亿 |
| 2025-12 | ARR 约 $90 亿 |
| 2026 年初 | Claude 成为 M365 Copilot 默认模型 |
| 2026-02 | ARR 约 $190 亿 |
| 2026-03 | Advisor Strategy Beta 推出 |
| 2026-04 | ARR 突破 $300 亿 |
| 2026-05 | CEO 阿莫代伊访英（计划） |
| 2027 | 3.5 GW 算力上线（与 Broadcom/Google 协议） |
| 2031 | Broadcom/Google 算力协议到期 |

## 相关页面

- [[industry/AI基础设施|AI 基础设施]]
- [[concept/MCP|MCP]]
- [[company/Broadcom]]
- [[company/Google]]
- [[company/OpenAI]]

## 引用来源

- [[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]
- [[source/acecamp-Anthropic-ARR-算力合作-260412]]
- [[source/substack-Anthropic-Advisor-Strategy-260412]]
