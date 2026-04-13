---
type: source
title: SMBC：NVIDIA GTC 2026 AI算力与光互联解决方案最新趋势
source_type: transcript
author: SMBC Nikko Securities / JST Consulting（Hasegawa）
date: "2026-04-13"
raw_path: "raw/2026-04-13/meeting_minutes/260413 - SMBC Latest Trends in AI Computing and Optical Interconnect Solutions Presented by Nvidia at GTC 2026_260413100923.md"
research_id: ""
research_type: "meeting_minutes"
entities:
  - "[[company/NVIDIA]]"
  - "[[company/Google]]"
  - "[[company/Amazon]]"
  - "[[industry/AI基础设施]]"
  - "[[concept/CPO]]"
  - "[[concept/OCS架构]]"
  - "[[concept/CSP自研芯片]]"
quality: high
tags:
  - ai
  - semiconductor
  - optical
  - compute
  - us
last_updated: "2026-04-13"
---

## 来源概要

SMBC Nikko Securities 午间研讨会，JST Consulting CEO Hasegawa 主讲，聚焦 NVIDIA GTC 2026 发布的 Rubin 平台架构（含 LPU）、Google TPU 独特架构与 3.5GW Anthropic 合作、AWS 自研芯片增长、OFC 2024 行业动向及光通信行业"超级周期"预测。

## 关键要点

1. **核心数据**
   - NVIDIA Rubin 平台 LPU（Language Processing Unit）：基于 Grok 技术（$200 亿授权）；内置 SRAM ~500MB，数据传输带宽比 GPU 快 7 倍；确定性执行（pre-scheduled）
   - GPU+LPU 混合系统（NVIDIA Dynamo）：token 生成效率提升最高 35 倍；每 GW 年收入可翻倍（$1500 亿 vs 纯 GPU 系统）
   - LPU rack 与 GPU rack 比例：提议 5 LPU : 8 GPU
   - AWS Trainium 自研芯片业务：三位数增长，年收入超 $100 亿
   - AWS 声称比 NVIDIA 成本效益高 30–40%（去除 65% 营业利润率）
   - Google Anthropic 3.5GW 合作：2027 年投入运营，单笔合同规模接近微软全年产能扩张量
   - Google TPU Superpod：3D Torus 拓扑，ICI（Inter-Chip Interconnect）无交换机协议，确定性执行
   - Lumentum OCS 订单积压：从 $1,000 万/季度基准飙升至超 $4 亿（H2 2024 起）
   - NVIDIA Feynman 平台（2028）：CPU 将集成 CPO 用于机架内 NVLink 交换机

2. **关键判断与观点**
   - LPU 不会替代 CPU；LPU 与 CPU 功能根本不同（LPU 专为高速 token 生成，CPU 为通用命令中枢）
   - LPU 将由三星代工（设计简单，无需台积电最先进工艺）
   - GPU+LPU 不会减少 HBM 需求：GPU 仍需 288GB HBM 处理 KV cache 加载任务
   - XPU（Google TPU 等）在成本效益上有优势；NVIDIA GPU+LPU 在算力密度上更强——双方均有竞争力，市场可以容纳两种路线
   - 光纤行业将从 2024H2 起进入历史级"超级周期"（AI 数据中心 + 长途网络 + 政府项目叠加）

3. **行业参与者行为模式**
   - CSP（Google/AWS）将自研芯片向外部商业化（对外销售/出租），而 Meta 自研芯片仅内部使用；微软对 NVIDIA 依赖度最高
   - 行业在 OFC 2024 上大量设立 MSA（Multi-Source Agreements）应对供应约束——标准化先于大规模出货
   - 超大型 CSP 通过预付光纤建设成本确保快速部署（如 Lumen PCF 网络），掌握供应链主导权

4. **与市场共识不同的观点**
   - LPU 制造不需要台积电最先进工艺（三星可生产），打破"先进制程=AI 竞争力"的简单化认知
   - DeepSeek 因频繁系统故障市场占有率下滑（而非算法能力问题），强调稳定服务的重要性

5. **时效性信号**
   - Rubin 平台 2024H2 进入量产（当前主力产品）
   - NVIDIA Feynman（CPO）2028 年路线图明确
   - 光纤/光器件价格预计 2024H2 开始显著上涨

## 重要数据点

| 指标 | 数值 |
|------|------|
| LPU 内存 | ~500 MB SRAM |
| LPU vs GPU 带宽 | 7x 更快 |
| GPU+LPU token 效率提升 | 最高 35x |
| LPU:GPU rack 比例（建议） | 5:8 |
| AWS 自研芯片年收入 | >$100 亿 |
| Lumentum OCS 季度积压（峰值） | >$4 亿 |

## 值得注意的观点/引语

> "NVIDIA's proposed optimal solution is a hybrid system combining GPUs and LPUs…the GPU handles memory-intensive tasks like loading the KV cache, while the LPU handles the actual high-speed token generation…35 times more efficient."

> "By 2028, the 'Feynman' platform will incorporate Co-Packaged Optics (CPO) for intra-rack communication." — Jensen Huang at GTC 2026

> "The consensus is that starting from the second half of 2024…the optical fiber industry will push into a historic super cycle."

## 结构性观察

- **NVIDIA 从芯片厂商到 AI 基础设施平台商的转型**在 Rubin 架构中体现得最为清晰：5 种机柜类型（GPU/LPU/CPU/Storage/Switch）意味着 NVIDIA 在试图主导整个 AI 工厂的物理基础设施设计权，而非仅出售芯片。
- **LPU 的 Grok 收购背景**揭示了 NVIDIA 防御性收购逻辑：Google TPU 架构师（Grok 创始人）的确定性执行技术被 NVIDIA 以 $200 亿成本内化，同时封堵了外部竞争者对该技术的商业化路径。
- **光通信"超级周期"的三驱动力**（AI DC + 长途网络 + 政府项目）叠加在不同时间窗口，构成罕见的多周期共振——但各细分赛道进入门槛不同：长途网络更多受益 Corning/Fujikura 等光纤大厂，DC 内互联更多受益 Lumentum/Coherent 等高端供应商。

## 与现有知识的关系

### 新增信息
- LPU 完整技术架构（500MB SRAM、7x 带宽、确定性执行、集成 C2C）
- NVIDIA Dynamo 混合系统 35x token 效率数据
- NVIDIA Feynman (2028) CPO 路线图（Jensen Huang 明确表态）
- AWS Trainium 自研芯片 $100 亿+ 年收入规模
- 光纤超级周期时间节点（2024H2）

### 印证之前观点
- Lumentum OCS 积压飙升（与 OCS 架构文章数据一致：从 $1000 万→超 $4 亿）
- Google TPU ICI 无交换机确定性执行架构（与 TPU 出货更新来源一致）
- Google-Anthropic 3.5GW 合作（2027 年运营，与 acecamp-Anthropic 来源一致）

### 矛盾/需修正
- 无

## 后续跟进项

- LPU 三星代工实际合作时间节点
- Rubin 平台 LPU rack 实际部署量（2025H2）
- NVIDIA Feynman CPO 规格细节

## 引用来源

原始文件：`raw/2026-04-13/meeting_minutes/260413 - SMBC Latest Trends in AI Computing...md`
