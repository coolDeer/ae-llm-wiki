---
type: source
title: TPU 26年出货更新、v8x设计问题、Anthropic谷歌博通合作展望及AI算力动态
source_type: transcript
author: AceCamp
date: "2026-04-12"
raw_path: "raw/2026-04-13/acecamp_article/260412 - TPU 26年出货存上调空间， v8x因设计问题推迟量产，Anthropic和谷歌博通合作展望。IFS与SpaceX就TeraFab合作方式，微软向基模的发力，CPU或5月再次涨价，边缘计算需求等。联发科_SambaNova_AMD_ARM_CoreWeave_Meta_Oracle_OpenAI_260413100938.md"
research_id: "69dc774796aab61ca8ce447e"
research_type: "acecamp_article"
entities:
  - "[[company/Google]]"
  - "[[company/Broadcom]]"
  - "[[company/Anthropic]]"
  - "[[company/Microsoft]]"
  - "[[company/NVIDIA]]"
  - "[[company/联发科 (MediaTek)]]"
  - "[[company/SambaNova]]"
  - "[[company/CoreWeave]]"
  - "[[company/Meta]]"
  - "[[industry/AI基础设施]]"
  - "[[concept/CSP自研芯片]]"
  - "[[concept/Arm架构服务器CPU]]"
quality: high
tags:
  - ai
  - semiconductor
  - compute
  - us
  - china
last_updated: "2026-04-13"
---

## 来源概要

AceCamp 专家访谈纪要，聚焦 Google TPU v8x/v8ax 延迟及出货预期、Anthropic-谷歌-博通 3.5GW 合作细节、Intel TeraFab/SpaceX 合作、微软自研基模转向、Arm AGI CPU 前景、Intel CPU 5 月涨价预期及边缘计算动态。

## 关键要点

1. **核心数据**
   - TPU v8x：由[[company/联发科 (MediaTek)]]负责 IO die，采用其内部较新 IO IP 导致颗粒速率未达设计带宽，封测良率偏低，预计延迟 1–2 个月。INT8 算力相比 v7 提升约 43–45%，性能定位介于 B300 和 Blackwell 之间。
   - TPU v8ax：由[[company/Broadcom]]设计，片间互联从光互联转向以太网，单端口 1.6T 以太网速率，对标训练场景；预计 2026Q3 末–Q4 初向谷歌提供小批量测试样品。
   - 2026 年 TPU 总出货预期维持 420 万颗，谷歌表示有近 10% 产能提升空间。2027 年预计超 600 万颗（v7 约 170–180 万 + v8 超 400 万）。
   - Anthropic-谷歌-博通 3.5GW 合作面向 2027 年及以后，对应近 400 万颗 TPU v8，初期以租用 GCP 资源为主。
   - 该 3.5GW 合作与 Fluidstack 1GW 合作无重叠（后者面向 v7 需求，2026 年初已宣布）。
   - Intel CPU 将于 5 月针对 64 核及以下处理器进行结构性涨价（供不应求最严重品类）。
   - AMD MI355/MI455 需求旺盛：微软和 Meta 未下调总量，仅调整交货节奏；Oracle 与 AMD 商谈追加供应。

2. **关键判断与观点**
   - Google CoWoS 产能不是瓶颈（已锁定 300+ 万片），EMIB 预计 4Q26 才开始小规模供货。
   - TPU v8 上将试验 CXL 3.0 接口实现 DRAM 池化，但外部存储柜方案因光交换延迟可行性不大；机柜内 CXL DRAM 模组方案更可行；产品化要到 TPU v9。
   - 微软数据中心延迟 2–4 个季度；Meta 延迟 2–3 个季度以上；[[company/CoreWeave]] 等 neocloud 受影响最大（控制力弱、第三方建设项目型模式）。
   - 微软内部已确定必须自研基座模型（OpenAI 排他协议到期 + 产品路线不清晰）。

3. **行业参与者行为模式**
   - CSP vs. neocloud 建设模式差异显著：传统 CSP 建设连续性强、延迟影响可控；neocloud 项目型建设、议价能力弱，受变压器/电力设备/人员短缺冲击最大。
   - Intel/SambaNova PD 分离推理方案市场接受度预计有限：软件适配工作量大、目标客群窄（大体量云厂商或大型企业私有化部署）。
   - Arm 重返服务器市场的策略转向：此前因生态不兼容失败，现借 AI 推理场景（CPU 负担不高）和 AI Agent 爆发重新切入。

4. **与市场共识不同的观点**
   - TPU v8ax 或成为 2026 年 v8 系列主要出货型号（因 v8x 延迟），而非此前预期的 v8x 主导。
   - 微软和 Meta 的 MI355/MI455 需求并未下调（数据中心建设延迟与芯片采购节奏分离）。

5. **时效性信号**
   - TPU 2026 年 420 万颗预期上调空间来自其他云厂商释放的 CoWoS 产能（每月约 1 万多片）。
   - Intel 已确认 5 月针对 64 核及以下 CPU 结构性涨价。

## 重要数据点

| 指标 | 数值 | 来源/时间 |
|------|------|-----------|
| TPU v8x INT8 算力提升 vs v7 | ~43–45% | 专家估算 |
| TPU v8x 延迟 | 1–2 个月 | 当前判断 |
| 2026 TPU 总出货预期 | 420 万颗 | 维持不变 |
| 2026 TPU 产能上调空间 | ~10% | 谷歌内部 |
| 2027 TPU 预期 | 超 600 万颗 | 展望 |
| Anthropic-谷歌-博通合作 | 3.5GW，面向 2027+ | 2026-04 宣布 |
| AMD MI355/MI455 中国市场份额 | ~4% | 2025 年 |
| NVIDIA 中国 GPU 市场份额（含灰色渠道） | ~55% | 2025 年 |
| Intel CPU 服务器市场份额 | 60% | 2025 年底 |
| Arm 架构服务器 CPU 份额 | 16% | 2025 年底 |

## 值得注意的观点/引语

> "数据中心建设延迟对不同厂商的影响程度各异……影响更多的是 neocloud，如 CoreWeave、Lambda 等。CoreWeave 此前的算力中心建设已因此推迟了约两个季度，其与甲骨文合作的部分计划也已推迟至 2027 年或更晚。"

> "微软内部已基本确定必须自研基座模型，当前快速的算力扩张也部分是为了保障未来自研模型的发展需求。"

> "Arm 将自身精准定位于 AI Agent 和推理前端，认为这是重返服务器市场的良机。相较于已接近饱和的边缘计算市场，服务器领域是其寻求增长的唯一方向。"

## 结构性观察

- **CSP 与 neocloud 的建设模式分化**正在加剧：传统 CSP 的连续性建设模式赋予其更强的抗扰动能力，而 neocloud 的项目型外包模式在供应链波动中暴露结构性脆弱；未来算力建设份额可能向大型 CSP 集中。
- **TPU 向外部商用化的路径**正在从"Anthropic 单一大客户"模式向更广泛的 GCP 算力租赁演进；谷歌的 IFS 协议（Intel 提供技术支持，SpaceX/Tesla 承担资本）预示着 TPU 生态的半独立化探索。
- **CPU 涨价节奏**反映 AI 推理对中低核数服务器 CPU 的超预期需求弹性——这一需求来自边缘推理、智能体调度等新场景，不完全依赖 GPU 扩张。
- **Arm 架构的渗透路径**已从"取代 x86"的正面竞争转向"填充 GPU+CPU 推理架构中 CPU 侧的增量需求"——这是一个更现实但也更可持续的增长逻辑。

## 与现有知识的关系

### 新增信息
- TPU v8x IO die 由联发科负责，且已出现具体质量问题（IO 速率未达标、封测良率低）
- TPU v8ax 正式确认以太网路线（放弃光互联），由博通设计
- 3.5GW 合作与 Fluidstack 1GW 合作无重叠（时间和技术栈不同）
- Intel TeraFab 合作架构细节：Intel 提供 PDK/技术服务，不直接做代工，特斯拉方出资建厂
- Intel CPU 5 月涨价确认，范围限于 64 核及以下

### 印证之前观点
- Anthropic 深度绑定 Google TPU 路线（来源：acecamp-Anthropic-ARR-算力合作-260412）
- ASIC 对 NVIDIA 的长期分食（来源：acecamp-Anthropic-ARR-算力合作-260412）
- CoreWeave 等 neocloud 建设延迟（之前已有信号）

### 矛盾/需修正
- 无明显矛盾，但此前预期 v8x 为 2026 主力出货型号；现更新为 v8ax 可能成为主要型号

## 后续跟进项

- 追踪 TPU v8ax 2026Q3–Q4 样品交付情况
- 关注 Intel CPU 5 月实际涨价执行情况
- 微软自研基模进展（2027 年目标）
- CoreWeave/Oracle 数据中心交付推迟实际影响

## 引用来源

原始文件：`raw/2026-04-13/acecamp_article/260412 - TPU 26年出货...md`
