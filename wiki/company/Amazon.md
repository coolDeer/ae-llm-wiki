---
type: company
name: "Amazon.com Inc. / AWS"
ticker: "AMZN"
exchange: "NASDAQ"
sector: "云计算 / 电商"
sub_sector: "云基础设施 / AI 平台"
market_cap: ""
founded: "1994"
hq: "Seattle, WA, USA"
key_people: []
tags:
  - cloud
  - ai
  - us
sources:
  - "[[source/cb-AWS-vs-Azure-vs-GCP-260412]]"
  - "[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]"
  - "[[source/cb-AI服务器海外市场ODM-260412]]"
last_updated: "2026-04-12"
confidence: medium
---

# Amazon.com Inc. / AWS

## 公司概况

Amazon Web Services（AWS）是全球最大的云基础设施服务商。在 AI 时代，AWS 采取"平台化"战略（Bedrock 多模型超市），而非押注单一模型，通过聚合多家 AI 模型并收取基础设施佣金实现商业化。

## AWS 云服务

### 核心技术优势

1. **Nitro 系统架构**：将网络和存储开销几乎全部在硬件层面处理，其他厂商目前难以复制
2. **Graviton（ARM 自研芯片）**：性价比高，内部客户认可度高
3. **产品灵活性**：乐高式精细化服务，工程师可自由组合（最灵活，也最复杂）

### 核心劣势

- AI 模型层相对弱（Bedrock 多模型策略但缺乏旗舰自有模型）
- 定价最复杂（账单体系复杂，隐形费用多）
- AI 商业化实现最慢（平台化需等待 AI adoption rate 更高）

（来源：[[source/cb-AWS-vs-Azure-vs-GCP-260412]]）

### 区域布局

- 北美和日本为核心优势区域
- 国内：光环新网 + 西云数据运营，账号体系与全球物理断开，合规麻烦

## AI 战略

### Bedrock 平台

AWS 的核心 AI 战略是平台化而非垂直整合：
- 聚合 Anthropic、OpenAI（新战略合作）等多家 AI 模型
- 按 token 使用 + 平台计算费用双重收费
- 用户可根据工作负载选择最合适的模型
- 本质：不赌哪个模型赢，收取基础设施佣金

与 Anthropic 的合作：Anthropic 80%+ 收入通过 AWS Bedrock 实现，AWS 是 Anthropic 最大单一渠道。

（来源：[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]）

### Amazon Nova（自有模型）

- 强项：语音、读图（可自动总结电视节目内容）
- 定位：补充 Bedrock 生态，而非主攻前沿

### 内部 AI 化

- **Amazon Q**：内部知识库 + 自然语言生成 Agent 平台
- 销售 quota 已包含 AI 相关目标
- 研发考核：AI 帮你做了多少 coding（而非写了多少代码）

（来源：[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]）

### Anthropic 合作 vs OpenAI 新合作

- 2025 年与 OpenAI 宣布战略合作，被视为 Bedrock 平台化战略的延伸（非放弃 Anthropic）
- Bedrock 策略是多模型并存，新增 OpenAI 是扩充而非替换

## 用户画像

- **互联网/初创/游戏公司**：工程师文化，崇尚灵活性和自由
- **CTO 决策**：不希望被微软"全家桶"绑定
- **海外**：默认首选云平台

（来源：[[source/cb-AWS-vs-Azure-vs-GCP-260412]]）

## 人员变动（2025-11）

- 宣布裁 3 万人（第一波 14000 人，第二波约 2026 年 1 月）
- 主要：疫情超招人员 + PrimeVideo/Alexa + 流程化可被 AI 替代的岗位
- 中国区基本未涉及
- 与 Capex 关系不大，主要是效率提升

（来源：[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]）

## AI 服务器采购

- GB200（2025 年）：~6500 柜
- GB200（2026E）：~3000 柜
- GB300（2025 年）：~1900 柜
- GB300（2026E）：~15,000 柜
- ODM：富士康（30%）、英业达（25%）、广达（20%）为主要供应商

（来源：[[source/cb-AI服务器海外市场ODM-260412]]）

## 风险因素

- AI 商业化速度慢于 Azure 和 GCP（Bedrock 平台化依赖高 adoption rate）
- 模型层竞争力弱（无 Gemini 或 OpenAI 级旗舰）
- OpenAI 合作可能带来渠道冲突（Anthropic 作为主要 B 端模型合作方）

## 催化剂

- Bedrock 多模型策略在 AI adoption 普及后规模效应显现
- Graviton 自研芯片降本优势
- 2027 年推理阶段：按需付费商业化成熟

## 相关页面

- [[company/Anthropic]]
- [[company/Google]]
- [[company/Microsoft]]
- [[industry/北美云厂格局]]

## 引用来源

- [[source/cb-AWS-vs-Azure-vs-GCP-260412]]
- [[source/cb-AWS-Meta人员变动云厂AI策略-260412]]
- [[source/cb-AI服务器海外市场ODM-260412]]
