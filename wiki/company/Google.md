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
  - "[[source/ace-Google技术发展线-260413]]"
  - "[[source/mm-AceCamp-Doubao-竞争格局-260413]]"
  - "[[source/cb-三星Galaxy-XR-260413]]"
  - "[[source/ace-TPU出货更新与AI算力动态-260413]]"
  - "[[source/ace-OCS内存基础设施架构逻辑-260413]]"
  - "[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
last_updated: "2026-04-13"
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

## 历史技术发展脉络

> 更新（2026-04-13）：AceCamp 深度梳理 Google AI 发展主线。（来源：[[source/ace-Google技术发展线-260413]]）

- **核心命题始终如一**：从 Larry Page 2000 年将 Google 定义为 AI 公司，到 Transformer 发明，Google 始终围绕"让机器更好地理解信息"这一命题
- **研究→工程→产品的完整链条**：Phil 模型→AdSense（2001-2003）→Google Translate（Franz Och 算法被 Jeff Dean 从 12 小时压缩至 100ms）→Google Brain（2009-2011）→猫咪论文（2012，无监督学习）→DeepMind（2014 收购）→TPU（15 个月从设计到部署）→TensorFlow→Transformer（2017，"Attention Is All You Need"）
- **结构性弱点**：Transformer 发明后未能足够快升级为公司级战略；关键作者大面积流失（形成 OpenAI/Anthropic）；旧利润池（搜索广告）过大导致缺乏冲击旧业务的动力
- **Gemini 多模态的历史基础**：Google 是国内唯一拥有真正端到端多模态基础模型（Gemini）的公司，领先于所有中国竞争者（包括 Qwen 3.5 的形式复制都未达到端到端水平）

## XR 生态（Android XR）

> 更新（2026-04-13）：Google Android XR 首次在三星商业硬件上落地。（来源：[[source/cb-三星Galaxy-XR-260413]]）

- 与[[company/三星电子]]合作，Android XR 系统搭载于 Galaxy XR 头显，是安卓 XR 系统首次商业落地
- 同时与 XREAL 达成 Android XR 合作
- 战略目标：通过三星/XREAL 硬件建立 Android XR 生态，抗衡 Meta Quest 生态和 Apple Vision OS

## Gemini 在中国市场的限制

Google Gemini 大模型在中国无法使用（同 Meta AI），搭载 Gemini 的三星 Galaxy XR 在中国 AI 功能受限，仅作普通 MR 设备使用。（来源：[[source/cb-三星Galaxy-XR-260413]]）

## 风险因素

- Gemini 企业端采用速度低于 Azure（OpenAI 先发优势）
- GCP 市场份额仍排 AWS/Azure 之后
- 客户忠诚度低，易受竞争冲击
- 历史性弱点：将技术优势转化为公司级战略的速度不够快

## 催化剂

- TurboQuant 在 Gemini 生产部署（6x 算力效率提升）
- GCP 增速回到 30%+（已展示信号）
- TPU 外部商业化（通过 Anthropic 等合作案例验证）
- 东亚/东南亚 AI 需求爆发
- Android XR 生态建立（与三星、XREAL 合作）

## 相关页面

- [[company/Anthropic]]
- [[company/Broadcom]]
- [[company/Microsoft]]
- [[company/Amazon]]
- [[company/联发科 (MediaTek)]]
- [[industry/北美云厂格局]]
- [[industry/AI基础设施]]
- [[concept/OCS架构]]
- [[concept/CSP自研芯片]]

## TPU 产品线（2026 年更新）

> ⚠️ 更新（2026-04-13）：TPU v8x 设计问题及 v8ax 路线变更。（来源：[[source/ace-TPU出货更新与AI算力动态-260413]]）

### TPU v8x（推迟）

- IO die 由[[company/联发科 (MediaTek)]]负责，采用较新 IO IP 导致颗粒速率未达设计带宽，封测良率偏低
- 预计延迟 1–2 个月，INT8 算力相比 v7 提升约 43–45%，性能定位介于 B300 和 Blackwell 之间

### TPU v8ax（主要型号）

- 由[[company/Broadcom]]设计，片间互联从光互联转向以太网（1.6T 以太网速率）
- 预计 2026Q3 末–Q4 初向谷歌提供小批量测试样品
- **市场共识更新**：v8ax 可能成为 2026 年 v8 系列主要出货型号（而非此前预期的 v8x）

### 2026–2027 TPU 出货预期

| 年份 | 预期出货 | 备注 |
|------|---------|------|
| 2026 | 420 万颗（有近 10% 上调空间） | 含 v8ax 为主 |
| 2027 | 超 600 万颗 | v7 约 170–180 万 + v8 超 400 万 |

### Anthropic-谷歌-博通 3.5GW 合作（确认）

- 面向 2027 年及以后，对应近 400 万颗 TPU v8
- 与 Fluidstack 1GW 合作（面向 v7，2026 年初宣布）无重叠
- 初期以租用 GCP 资源为主

### OCS 架构：谷歌的内存基础设施布局

- Google Ironwood TPU v7 SuperPod：9,216 颗芯片，共 **1.77 PB 可直接寻址共享 HBM 内存**
- OCS 部署 TCO 收益：TCO 下降 40%、功耗节省 40–50%、延迟降低 70%
- 谷歌 2026 年 OCS 需求约 18,000 台（以自主设计 MEMS 方案+Lumentum/Coherent 为补充）

（来源：[[source/ace-TPU出货更新与AI算力动态-260413]]，[[source/ace-OCS内存基础设施架构逻辑-260413]]，[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

## 引用来源

- [[source/acecamp-Anthropic-ARR-算力合作-260412]]
- [[source/substack-GPUs-6x-TurboQuant-260412]]
- [[source/cb-AWS-vs-Azure-vs-GCP-260412]]
- [[source/cb-AWS-Meta人员变动云厂AI策略-260412]]
- [[source/cb-AI服务器海外市场ODM-260412]]
- [[source/ace-Google技术发展线-260413]]
- [[source/mm-AceCamp-Doubao-竞争格局-260413]]
- [[source/cb-三星Galaxy-XR-260413]]
