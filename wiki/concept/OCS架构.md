---
type: concept
name: OCS 架构（光电路交换 / 内存基础设施框架）
aliases:
  - "OCS"
  - "光电路交换"
  - "Optical Circuit Switching"
  - "Apollo OCS"
category: "technology"
tags:
  - optical
  - semiconductor
  - ai
  - data-center
sources:
  - "[[source/ace-OCS内存基础设施架构逻辑-260413]]"
  - "[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
last_updated: "2026-04-13"
---

# OCS 架构（光电路交换 / 内存基础设施框架）

## 定义

OCS（Optical Circuit Switching，光电路交换）是通过光学手段建立和切换电路路径的技术，在 AI 数据中心中扮演集群级互连节点的角色。传统上 OCS 被视为"交换机替代"（设备框架），但新的分析框架将其定位为"内存基础设施"——通过控制可寻址 HBM 域的拓扑边界，成为 AI 超大规模集群扩展的核心组件。

（来源：[[source/ace-OCS内存基础设施架构逻辑-260413]]）

## 在投资研究中的应用

### 估值框架的核心争议

| 框架 | 代表类比 | EV/Sales 参考 |
|------|---------|-------------|
| 设备框架（传统） | Cisco/Arista/Ciena | 7–12x |
| 内存基础设施框架（新） | Astera Labs | 15x+（Astera 30x+） |

- Lumentum 2026 财年 Q2 OCS 订单积压突破 $4 亿（较基准 $1,000 万/季度飙升）
- Coherent 在 OFC 2026 上将 2030 年 OCS TAM 从 $20 亿上调至 $40 亿

（来源：[[source/ace-OCS内存基础设施架构逻辑-260413]]）

### OCS 的双轨架构

1. **DCN（数据中心网络）层**：传统交换带宽属性（设备定价框架）
2. **集群级互连（纵向扩展）层**：内存拓扑控制器角色——定义可寻址 HBM 域的物理边界

### 关键数据

- Google Ironwood TPU v7 SuperPod：9,216 颗芯片，每颗 192GB HBM3e，共 **1.77 PB 可直接寻址共享 HBM 内存**
- OCS 部署 TCO 收益（Google 数据）：TCO 下降 40%、功耗节省 40–50%、延迟降低 70%

（来源：[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]，[[source/ace-OCS内存基础设施架构逻辑-260413]]）

### OCS 与 HBM 的关系：净正向效应

- **市场误解**：OCS 提升 HBM 利用率 → 减少 HBM 采购需求（净负向）
- **正确分析**：OCS 通过杰文斯悖论机制使 HBM 净需求正向扩张：
  - 消除算法规模硬性限制 → 上下文窗口爆炸增长 → 新增量需求大于效率节省
  - HBM 需求增长曲线远超单 GPU HBM 容量增长

（来源：[[source/ace-OCS内存基础设施架构逻辑-260413]]）

### OCS 需求预测

| 客户 | 2026 年需求 | 2027 年需求 |
|------|-----------|-----------|
| Google | ~18,000 台 | >30,000 台 |
| Microsoft | ~2,000 台 | — |
| 整体市场 | — | >40,000 台（CAGR 30–50%） |

（来源：[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

### 供应格局

- Coherent 液晶技术为主（自产，高壁垒）
- Lumentum 为次
- Google 自主设计 MEMS 方案（Celestica 代工），Lumentum/Coherent 为补充
- MEMS 方案至少 1.5 年才能量产（技术壁垒）

（来源：[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

### NVIDIA 的立场（GTC 2026）

- NVIDIA Feynman 平台（2028）：CPU 将集成 CPO 用于机架内 NVLink 交换机
- NVIDIA 当前（Rubin 平台）使用以太网/InfiniBand，OCS 主要是 Google/其他 CSP 的方案

（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

## 结构性观察

- OCS 的"估值叙事切换"是半导体光学行业少见的从制造周期性向 IP 护城河的商业模式跨越
- Google Apollo OCS 架构将 HBM 地址空间的物理边界定义权交给光层，OCS 供应商未来可能掌握 AI 集群扩展的"土地审批权"
- 国内 OCS 路径（华为 CloudMatrix 384 vs 谷歌方案架构差异）是重要后续跟进方向

## 相关概念

- [[concept/CPO]]
- [[industry/光芯片]]
- [[industry/AI基础设施]]
- [[company/Google]]

## 引用来源

- [[source/ace-OCS内存基础设施架构逻辑-260413]]
- [[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]
- [[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]
