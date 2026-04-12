---
type: industry
name: "AI 基础设施"
parent_sector: "信息技术"
market_size: ""
growth_rate: ""
key_players:
  - "[[company/Anthropic|Anthropic]]"
  - "[[company/华为昇腾|华为昇腾]]"
tags:
  - ai
  - enterprise-software
  - cloud
  - saas
  - ai-chip
sources:
  - "[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]"
  - "[[source/昇腾调研-华为950-260410]]"
  - "[[source/AI平台CCL规格升级-260410]]"
  - "[[source/大模型商业模式-Token价值光谱-260410]]"
  - "[[source/Verdent-AI-Coding访谈-260410]]"
  - "[[source/MS-存储超级周期企业采购影响-260410|MS-存储超级周期企业采购影响-260410]]"
last_updated: "2026-04-11"
---

# AI 基础设施

## 行业概况

AI 基础设施涵盖支撑企业 AI 应用的全栈技术与服务，包括基础模型（Foundation Models）、AI 开发工具、企业 AI 平台、以及底层算力和硬件。2026 年，该行业正经历从实验性采用向大规模企业部署的转折。

## 市场规模与增长

- [[company/Anthropic|Anthropic]] 2026 年 ARR 预计 $4B+（4x YoY），反映企业 AI 采用的高速增长
- 企业 AI 预算来源双重：SaaS 预算再分配 + 人力预算转移（人力占企业支出 60-70%）

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 产业链分析

### 上游：算力与硬件
- GPU/TPU 等 AI 加速器
- HBM 等 AI 专用存储
- AI 硬件需求挤压企业级 DRAM/NAND 供给（来源：[[source/MS-存储超级周期企业采购影响-260410|MS-存储超级周期企业采购影响-260410]]）

### 中游：模型与平台
- 基础模型提供商：[[company/Anthropic|Anthropic]]（Claude）、OpenAI、Google
- 云分发平台：AWS Bedrock、Google Vertex（占 Anthropic 60%+ 部署）
- 集成协议：[[concept/MCP|MCP]]（降低集成复杂度 80%）

### 下游：企业应用
- AI 编程工具：Claude Code（CLI pair programmer，初创公司 70-75% 采用率）
- AI 办公协作：Claude Co-work、M365 Copilot
- 垂直行业应用：Legal Plugin、Managed Agents API
- AI agent：成本为人工的 15-20%

## 竞争格局

| 玩家 | 定位 | 关键优势 |
|------|------|----------|
| [[company/Anthropic|Anthropic]] | 基础模型 + 企业工具 | 安全性、Claude Code 开发者采用率、MCP 生态 |
| OpenAI | 基础模型 + 消费端 + 企业 | 先发优势、品牌、GPT 生态 |
| Google | 基础模型 + 云平台 | Vertex 分发、搜索整合、TPU |
| Microsoft | AI 应用 + 云平台 | M365 生态、Azure、Copilot 分发 |
| Meta | 开源模型 | Llama 开源生态 |

### 关键竞争动态
- Claude 于 2026 年初成为 M365 Copilot 默认模型，标志多模型策略兴起
- 50 人开发团队使用 Claude Code vs Copilot 的年均生产力差距约 $5M
- 企业端呈现多模型并用趋势

（来源：[[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]）

## 关键趋势

1. **"Seat-Apocalypse"**：传统 SaaS 订阅预算正被重新分配至 AI 工具，对 Salesforce、ServiceNow 等传统 SaaS 公司构成威胁
2. **人力替代加速**：AI agent 成本仅为人工 15-20%，客户支持岗位裁减 40-45%
3. **PLG + 云市场分发**："Land and expand" 策略 + 云市场成为主要渠道（80%+ 收入）
4. **合作伙伴生态规模化**：如 AABG 的 30,000 人专业服务团队
5. **硬件供给瓶颈**：AI 组件（HBM）制造优先级挤压企业级存储供给，服务器涨价 100-300%

## 监管环境

- AI 安全监管趋严
- 数据隐私和合规要求提升（Compliance API 应运而生）
- 各国 AI 法规差异化

## 投资机会与风险

### 机会
- 企业 AI 采用仍处早期，TAM 巨大
- 人力成本替代空间广阔（60-70% 企业支出为人力）
- 云市场分发降低获客成本

### 风险
- 模型能力同质化导致定价压力
- 企业采用周期可能慢于预期（8-10 周 bespoke 研究阶段）
- AI 硬件供给瓶颈推高基础设施成本
- 监管不确定性

## 相关公司

- [[company/Anthropic|Anthropic]]

## 相关页面

- [[concept/MCP|MCP]]
- [[industry/存储与企业硬件|存储与企业硬件]]

## 引用来源

- [[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]
- [[source/MS-存储超级周期企业采购影响-260410|MS-存储超级周期企业采购影响-260410]]
