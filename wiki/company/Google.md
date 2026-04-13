---
type: company
name: "Google LLC / Alphabet Inc."
ticker: "GOOG"
exchange: "NASDAQ"
sector: "云计算 / AI / 广告"
sub_sector: "AI 平台 / 搜索 / 云服务"
market_cap: ""
founded: "1998"
hq: "Mountain View, CA, USA"
key_people: []
tags:
  - cloud
  - ai
  - advertising
  - semiconductor
  - us
sources:
  - "[[source/acecamp-Anthropic-ARR-算力合作-260412]]"
  - "[[source/substack-GPUs-6x-TurboQuant-260412]]"
  - "[[source/cb-AWS-vs-Azure-vs-GCP-260412]]"
  - "[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]"
  - "[[source/cb-AI服务器海外市场ODM-260412]]"
last_updated: "2026-04-12"
confidence: medium
---

# Google LLC / Alphabet Inc.

## 公司概况

Google 是 AI 战略最为全栈的超大规模云厂商，技术覆盖算力芯片（TPU）、基础模型（Gemini）、云平台（GCP）和应用层（Search/Workspace）。同时通过与 Anthropic 和 Broadcom 的战略合作，在 AI 算力基础设施领域持续强化护城河。

## AI 战略

### 全栈优势（四层）

| 层次 | 产品 | 市场地位 |
|------|------|---------|
| 算力芯片 | TPU（Cloud TPU v5/v6） | 自研最成熟，已外部商业化 |
| 基础模型 | Gemini | Arena 排行榜领先，商业化加速 |
| 云平台 | GCP / Vertex AI | 数据科学/ML 用户核心选择 |
| 应用层 | Search / Workspace / 广告 | 全球最大广告平台 |

在所有大型科技公司中，Google 是唯一在四层全面布局且均有竞争力的公司。

（来源：[[source/cb-AWS-Meta人员变动云厂AI策略-260412]]）

### Anthropic 战略合作

- 向 Anthropic 提供 Google Cloud 基础设施支持
- 与 Broadcom 联合为 Anthropic 开发定制 TPU 芯片
- 协议有效期至 2031 年，2027 年起提供 3.5 GW 算力
- 意义：TPU 从内部工具向外部商用基础设施的关键转型

（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]）

### TurboQuant 算法

- Google Research 发布 TurboQuant（2026 年 3 月 25 日）
- 将 KV Cache 压缩 6x（3 bits，零精度损失）
- Google 既研发算法又运营 Gemini：若在 Gemini 推理中应用，可将 GPU 有效算力提升 6x
- 形成对所有竞争对手的算力效率优势

（来源：[[source/substack-GPUs-6x-TurboQuant-260412]]）

## GCP 云服务

### 核心定位

- **用户画像**：数据驱动型、媒体、出海企业、AI/ML 初创公司
- **技术优势**：冷启动速度最快、全球网络延迟最低（google.com 多年运营基础）
- **数据科学**：BigQuery、ML 训练套件业界顶级
- **新兴市场**：东南亚/南美扩张最快（凭借网络速度和产品优势）

### 区域布局

- 全球 40+ 区域
- 中国：无数据中心（合规性差）
- 东南亚/台湾：快速扩张，凭借网络时延优势赢得出海客户

### 劣势

- **客户忠诚度低**：采用开源架构，迁移成本低，容易流向其他平台
- **中国无基础设施**：国内客户只能走香港/新加坡
- **企业生态**弱于 Azure（无 Windows/Office 绑定）

（来源：[[source/cb-AWS-vs-Azure-vs-GCP-260412]]）

## AI 服务器采购

- GB200（2025 年）：~4500 柜
- GB200（2026E）：~2100 柜（切换至 GB300）
- GB300（2025 年）：~1200 柜
- GB300（2026E）：~19,000 柜（四大 CSP 中最高）
- ODM：英业达主导（~50% 份额）

注：Google GB300 采购量高于 AWS（19K vs 15K），可能反映其 ASIC/TPU 比例更高，对英伟达纯 GPU 依赖相对更低。

（来源：[[source/cb-AI服务器海外市场ODM-260412]]）

## 风险因素

- Gemini 企业端采用速度低于 Azure（OpenAI 先发优势）
- GCP 市场份额仍排 AWS/Azure 之后
- 客户忠诚度低，易受竞争冲击

## 催化剂

- TurboQuant 在 Gemini 生产部署（6x 算力效率提升）
- GCP 增速回到 30%+（已展示信号）
- TPU 外部商业化（通过 Anthropic 等合作案例验证）
- 东亚/东南亚 AI 需求爆发

## 相关页面

- [[company/Anthropic]]
- [[company/Broadcom]]
- [[company/Microsoft]]
- [[company/Amazon]]
- [[industry/北美云厂格局]]
- [[industry/AI基础设施]]

## 引用来源

- [[source/acecamp-Anthropic-ARR-算力合作-260412]]
- [[source/substack-GPUs-6x-TurboQuant-260412]]
- [[source/cb-AWS-vs-Azure-vs-GCP-260412]]
- [[source/cb-AWS-Meta人员变动云厂AI策略-260412]]
- [[source/cb-AI服务器海外市场ODM-260412]]
