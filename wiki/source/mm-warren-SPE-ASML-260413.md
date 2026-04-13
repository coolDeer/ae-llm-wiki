---
type: source
title: "Warren — 半导体设备：ASML产能瓶颈、Lasertec地位强化与Google TPU v9"
source_type: transcript
author: "（机构未知，代码名"warren"）"
date: "2026-04-13"
raw_path: "raw/2026-04-13/meeting_minutes/260413 - warren_260413100923.md"
research_id: "69dc65d896aab61ca8ce4468"
research_type: "meeting_minutes"
entities: []
quality: high
tags:
  - semiconductor
  - ai
  - us
last_updated: "2026-04-13"
---

## 来源概要

代号"warren"的半导体产业链专家电话会，深入讨论 SPE（半导体生产设备）产能扩张紧迫性、ASML EUV 产能瓶颈（Zeiss 镜头）、TSMC N3 容量紧张、Nvidia 从训练到推理的硬件组合转移、Lasertec 地位强化及 Google TPU v9 竞争力。

**注**：本文件不在 Japan+Macro 主题范围内（主要覆盖全球半导体设备），来源摘要页依规创建但不创建日本特定实体页。

## 关键要点

1. **ASML 产能约束核心**：Zeiss 镜头（生产周期 15-18 个月）是 ASML EUV 的主要瓶颈；Zeiss 私有公司，扩产意愿不确定；管理层需发布 90-100 台/年产能扩张计划才能支撑股价；当前无扩产情况下最大约 75 台。
2. **TSMC 的应对策略**：拉前 Lam Research ALD 干光刻胶技术（可减少 2/3 EUV 曝光量→产出率提升约 40%），已在 A14 节点验证；二次选择是减少 EUV 层数+增加 ArF 浸没曝光，尚未启用。
3. **行业参与者行为模式**：韩国（三星/Hynix）愿意预付款/溢价以锁定 EUV 工具；TSMC 坚持"仅凭 PO"政策→成为 ASML 眼中"麻烦客户"→TSMC 已派高管赴 ASML 荷兰总部争取产能。这一"客户行为差异"是供货分配的关键驱动力。
4. **Lasertec 地位强化**：KLA actinic 检查工具使用非 Zeiss 镜头（TSMC 不接受），KLA 在 TSMC 的开发暂停；TSMC 本季度安装 3 台 Lasertec（A200/A300/A10 平台）——A10 是 R&D 部门首次直接参与选型，意味着 A10/A7 节点光学检查已无可替代方案。
5. **Google TPU v9**：架构极其激进（4 个 N2P 计算 die + 8 个 N3 I/O die + 16 个 HBM4），性能可能可比 Nvidia Rubin Ultra；供应链多元化（Broadcom/MediaTek/Samsung 为设计+封装合作方）。

## 重要数据点

| 指标 | 数值 |
|------|------|
| ASML 客户 2025 需求汇总 | ~90 台（预期修订至 100+） |
| ASML 无扩产情况下最大产出 | ~75 台 |
| TSMC 2024 EUV 请求/实际获得 | 26/24 台 |
| Samsung 2024 EUV 请求/实际 | 21/17 台 |
| Hynix 2024 EUV 分配 | 14 台 |
| TSMC N3 2025 新增产能 | ~40k-45k wafers/月 |
| TSMC AMD N3 需求 vs. 供给 | AMD 请求 3x，仅获承诺 2x |
| Dry Photoresist EUV 效率提升 | ~40% |
| Rubin Ultra vs. Rubin | N3 + 核心重分配（FP4），CoWoS 两模块拼接 |

## 值得注意的观点/引语

> "TSMC is sending a high-level delegation to ASML headquarters to secure tool supply — TSMC's insistence on its own purchasing policies has made it a 'problematic customer.'"

> "The next major constraint is expected to emerge in PCBs and ABF substrates, driven by rising component volumes and increasing layer counts."

> "Google TPU v9 has the potential to match or even exceed Nvidia Rubin Ultra, assuming successful execution."

## 结构性观察

1. **EUV 分配博弈揭示了"购买关系即供应安全"**：愿意预付款的韩国厂商获得更好分配，而技术领先的 TSMC 因坚持标准采购政策反而处于供货劣势。这是半导体供应链中"关系型 vs. 交易型"采购模式的真实代价。
2. **PCB/ABF 基板是下一个瓶颈**：从内存/光模块→前道晶圆容量→后道封装（PCB/ABF）的瓶颈轮动，为 Ibiden 等 ABF 基板供应商提供多年成长逻辑。
3. **AI 推理 vs. 训练的硬件组合转变**：GPU:CPU 比从 1:0.5（训练时代）→ 1:2.4（推理时代），意味着推理阶段对 CPU/DRAM/存储的需求比例大幅提升，分散 Nvidia 在"AI 硬件定义权"上的垄断，AMD CPU 等受益。

## 与现有知识的关系

### 新增信息
- ASML 产能约束细节（Zeiss 镜头瓶颈、High-NA 资源重调）。
- TSMC 干光刻胶提前验证（A14 节点，原计划 A10）。
- Google TPU v9 多供应商战略细节。

### 印证之前观点
- Rorze（同日）提到 TSMC Micron 投资带动的设备大订单，与本文件的 TSMC 产能扩张叙事印证。

### 矛盾/需修正
- 无

## 后续跟进项

- ASML FY2025 产能目标正式宣布（Q2 财报后）
- Lasertec A200 验证结果
- Google TPU v9 量产时间线

## 引用来源

原始文件：`raw/2026-04-13/meeting_minutes/260413 - warren_260413100923.md`
