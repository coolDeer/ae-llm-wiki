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
  - "[[source/acecamp-Anthropic-ARR-算力合作-260412]]"
  - "[[source/substack-GPUs-6x-TurboQuant-260412]]"
  - "[[source/cb-AI服务器海外市场ODM-260412]]"
  - "[[source/ace-TPU出货更新与AI算力动态-260413]]"
  - "[[source/ace-OCS内存基础设施架构逻辑-260413]]"
  - "[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
last_updated: "2026-04-13"
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

## 去英伟达化与 ASIC 路线（新增，2026-04-12）

> ⚠️ 更新（2026-04-12）：ASIC 路线的系统性进展。（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]，[[source/cb-AI服务器海外市场ODM-260412]]）

### ASIC 占比增长

AI 服务器中自研 ASIC 占比：~5%（2024）→ 8–9%（2025）→ 15%（2026E）

北美 CSP 自研芯片方向：
- **Google TPU**：外部商业化，Broadcom 制造，向 Anthropic 供货
- **AWS Trainium/Inferentia**：内部使用，推理场景性价比优势
- **Meta MTIA**：广告推理专用
- **Azure Maia**：减少英伟达依赖

### Broadcom-Google-Anthropic 标志性合作

- 博通基于谷歌 TPU 规格开发定制芯片，协议至 2031 年
- 2027 年起 Anthropic 获约 3.5 GW 算力
- 首次形成"芯片设计–生产制造–算力部署"全链条闭环，与英伟达垂直整合正面对抗

### TurboQuant 算法（去英伟达化的软件路径）

- Google Research 发布（2026-03-25）
- KV Cache 压缩 6x（3 bits，零精度损失），单 GPU 并发用户 9 → 50+
- 相当于将每个 GPU 的有效内存提升 6x，无需购买新硬件
- 供给约束（DRAM）+ 需求爆炸（Agent）+ 算法压缩三体问题中，算法是移动最快的变量

（来源：[[source/substack-GPUs-6x-TurboQuant-260412]]）

## GB200/GB300 全球需求概况（2026E）

| CSP | GB300 2026E（柜） |
|-----|-----------------|
| Microsoft | ~28,000 |
| Google | ~19,000 |
| Meta | ~17,000 |
| AWS | ~15,000 |
| 合计 | ~79,000 |

（来源：[[source/cb-AI服务器海外市场ODM-260412]]）

## OCS 与光互连的新发展（2026-04 更新）

> ⚠️ 更新（2026-04-13）：OCS 从"带宽设备"向"内存基础设施"的估值框架重构。（来源：[[source/ace-OCS内存基础设施架构逻辑-260413]]，[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

- **1.6T 光模块 2026 年出货预测**：约 1,500 万颗（已计入供应约束）；InnoLight ~50%、Eoptolink ~25%、Coherent ~22%
- **OCS 需求**：谷歌 2026 年约 18,000 台，2027 年超 30,000 台；整体市场 CAGR 30–50%
- **CPO 定位**：纯增量市场（替代机架内铜缆，不替代可插拔光模块）；NVIDIA Feynman 平台（2028）将集成 CPO
- **光纤超级周期**：AI DC + 长途网络 + 政府项目三驱动力，从 2024H2 起进入历史级超级周期

## NVIDIA GTC 2026 架构更新

> ⚠️ 更新（2026-04-13）：Rubin 平台 LPU 架构详情。（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

- **NVIDIA Dynamo（GPU+LPU 混合）**：token 效率提升最高 35 倍；LPU 内置 500MB SRAM，带宽 7x GPU
- **CSP 自研替代时间表**：推理替代进行中；训练替代要到 2028 年以后
- **AWS Trainium**：自研芯片年收入 >$100 亿，三位数增长

（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]，[[source/ace-CPU与GPU供需及国内格局-260413]]）

## 相关公司

- [[company/Anthropic|Anthropic]]
- [[company/Broadcom]]
- [[company/Google]]
- [[company/NVIDIA]]
- [[company/Amazon]]
- [[company/Microsoft]]
- [[company/Meta]]

## 相关页面

- [[concept/MCP|MCP]]
- [[industry/存储与企业硬件|存储与企业硬件]]
- [[industry/北美云厂格局]]
- [[industry/国产AI服务器]]
- [[industry/AI芯片]]

## 引用来源

- [[source/Merit-Anthropic企业业务调研-260410|Merit-Anthropic企业业务调研-260410]]
- [[source/MS-存储超级周期企业采购影响-260410|MS-存储超级周期企业采购影响-260410]]
- [[source/acecamp-Anthropic-ARR-算力合作-260412]]
- [[source/substack-GPUs-6x-TurboQuant-260412]]
- [[source/cb-AI服务器海外市场ODM-260412]]
