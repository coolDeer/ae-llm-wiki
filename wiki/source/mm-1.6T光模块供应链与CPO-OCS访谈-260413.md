---
type: source
title: AceCamp光通信访谈：1.6T光模块订单、技术路径与供应链（含CPO/OCS）
source_type: transcript
author: AceCamp
date: "2026-04-13"
raw_path: "raw/2026-04-13/meeting_minutes/260413 - AceCamp Optical Communications Interview_ Orders, Technology Paths, and Supply Chain for 1.6T Optical ModulesCPOOCS_260413100926.md"
research_id: ""
research_type: "meeting_minutes"
entities:
  - "[[industry/AI基础设施]]"
  - "[[industry/AI-PCB与CCL]]"
  - "[[concept/CPO]]"
  - "[[concept/OCS架构]]"
  - "[[company/NVIDIA]]"
  - "[[company/Google]]"
  - "[[company/Microsoft]]"
quality: high
tags:
  - optical
  - semiconductor
  - ai
  - supply-chain
  - us
  - china
last_updated: "2026-04-13"
---

## 来源概要

AceCamp 光通信专家访谈（英文 AI 摘要），系统覆盖 1.6T 光模块供应链瓶颈（EML/Faraday 旋转器短缺）、EML vs SiPh 市场格局、CPO 价值链演变及 OCS 需求预测。

## 关键要点

1. **核心数据**
   - 2026 年 1.6T 光模块行业预测：约 1,500 万颗（已计入供应约束）
   - Lumentum 200G EML 年产能：3,000–4,000 万颗（仅够生产约 500 万颗 1.6T 模块）
   - 1.6T 市场份额（当前年）：InnoLight ~50%、Eoptolink ~25%、Coherent ~22%、Lumentum ~5%（不含 NVIDIA 内部 Mellanox，Mellanox 另占约 20%）
   - 1.6T SiPh 模块 vs EML 模块 BOM 成本差：SiPh 低 $120–130（SiPh ~$400+，EML ~$550–580）
   - EML 1.6T DR 模块 BOM 明细：EML 芯片 $160、DSP $160、PCBA $60、TIA $60、PD Array $56、无源器件 $30–40
   - 当前售价：EML 版 $1,100–1,200；SiPh 版 ~$1,000
   - 2028 年 BOM 预期：降至约 $450（DSP 降至 $120，EML 降至 $10–15）
   - 1.6T SiPh 份额预计占 60–70%（vs 800G 时 ~40%）
   - OCS 需求预测：2026 年谷歌 ~18,000 台，微软 ~2,000 台；2027 年谷歌超 30,000 台，整体超 40,000 台；CAGR 30–50%
   - OCS 供应：Coherent 液晶技术为主（自产，高壁垒）；Lumentum 为次；MEMS 方案至少 1.5 年才能量产
   - InP（磷化铟）衬底：全球需求约 70–80 万片/月，供给约 40 万片/月——严重短缺

2. **关键判断与观点**
   - EML 不会被 SiPh 完全替代：EML 仍是长距（500m–2km）主流及 3.2T 以上（400G/lane，SiPh 材料限制 ~200G/lane）的唯一方案
   - SiPh 主导短距 DR 应用（30m–500m）；未来机架内应用将由 SiPh 的 NPO 和 CPO（光引擎）主导
   - CPO 是纯增量市场（替代铜缆无法支持 1.6T 以上的机架内互联），而非替代可插拔模块
   - OCS 部署对所有主要 CSP 而言是"不可避免"的（Google 部署后实现 TCO 下降 40%、功耗节省 40–50%、延迟降低 70%）

3. **行业参与者行为模式**
   - CSP 采用"供应绑定"（binding）模式采购关键器件：直接向 Lumentum 锁定 EML 配额，再指导光模块厂商从该配额采购
   - Coherent/Lumentum 在 ELS/PLS（外部光源）上优先保障自家产品，对竞争对手形成供应瓶颈
   - 中国出口管制对 InP 外卖审查期延长（影响 AXT 等厂商），被视为中国以上游材料控制推动国内 EML 芯片厂商的策略（类比稀土策略）

4. **与市场共识不同的观点**
   - NVIDIA 通过 Mellanox 内部供应约占 1.6T 市场 20%（市场报告通常不含此数据，导致外部市场份额被高估）

5. **时效性信号**
   - Source Photonics EML 产能 1 亿颗/年是年底扩产后的峰值产能，而非 2024 全年供应量；对外部市场的大规模供应最早 Q4 才开始

## 重要数据点

| 指标 | 数值 |
|------|------|
| 2026 年 1.6T 出货量预测 | 1,500 万颗 |
| EML 1.6T BOM | $550–580 |
| SiPh 1.6T BOM | ~$400+ |
| 当前 1.6T InnoLight 份额 | ~50% |
| OCS 谷歌 2026 需求 | ~18,000 台 |
| OCS 谷歌 2027 需求 | >30,000 台 |
| CPO FAU 单价（量产） | $150+ |

## 值得注意的观点/引语

> "CPO is considered a purely incremental market for optical component and module makers. It addresses on-board (intra-rack) connectivity, replacing traditional copper cables which are becoming impractical at speeds of 1.6T and beyond."

> "China appears to be strategically using its control over upstream materials (InP) to foster the growth and adoption of its domestic midstream component suppliers (e.g., EML chips), similar to the strategy used with rare earths and Faraday rotators."

## 结构性观察

- **SiPh vs EML 的共存而非替代**是市场最常被误读的格局——EML 的长距优势（物理材料特性）决定了其不可替代性，SiPh 的推进主要在短距 DR 应用，而 3.2T 时代将再次向 EML 倾斜（400G/lane 超越 SiPh 材料限制）。
- **InP 衬底战略化**：中国通过控制 InP 出口审查时间（而非完全禁止）制造不确定性，迫使北美买家溢价采购，同时为国内 EML 芯片厂商创造国产替代窗口——这是精准的"供应链博弈"而非全面脱钩。
- **CPO FAU 的价值链重构**：光模块厂商（InnoLight/Eoptolink）在 CPO 时代的竞争力将下降（缺乏 PIC/EIC 键合的半导体工艺能力），价值将上移至掌握芯片和外部光源的 Coherent/Lumentum；这与目前市场普遍对 InnoLight 的高估值期望存在结构性冲突。

## 与现有知识的关系

### 新增信息
- 1.6T 供应链详细 BOM 分解（EML vs SiPh 成本对比）
- OCS 具体需求数据（谷歌 2026/2027 台数）
- InP 衬底战略化解读
- NVIDIA Mellanox 内部供应 ~20% 1.6T 市场份额
- CPO FAU 高复杂度要求（$150+，500–600°C 回流焊耐热）

### 印证之前观点
- 1.6T SiPh 份额提升趋势（与其他光模块访谈一致）
- OCS 需求高速增长（与 OCS 内存架构分析文章一致）

### 矛盾/需修正
- 无

## 后续跟进项

- Source Photonics 实际 EML 供货规模（Q4 2026）
- CPO 价值链重构对 InnoLight 估值影响
- 中国国内 InP 产能建设节奏

## 引用来源

原始文件：`raw/2026-04-13/meeting_minutes/260413 - AceCamp Optical Communications Interview...md`
