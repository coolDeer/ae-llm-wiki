---
type: concept
name: "CPO (Co-Packaged Optics)"
aliases:
  - "Co-Packaged Optics"
  - "共封装光学"
  - "光电共封装"
category: "technology"
tags:
  - optical-module
  - semiconductor
  - data-center
sources:
  - "[[source/Merit-光模块测试设备调研-260410|Merit-光模块测试设备调研-260410]]"
  - "[[source/cb-曦智科技IPO光芯片市场-260413]]"
  - "[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
last_updated: "2026-04-13"
---

# CPO (Co-Packaged Optics)

## 定义

CPO（Co-Packaged Optics，共封装光学/光电共封装）是一种将光学引擎直接封装在交换芯片（Switch ASIC）基板上的技术方案，旨在缩短电信号传输距离、降低功耗、提升带宽密度。CPO 被视为数据中心光互连的下一代技术方向，尤其在 3.2T/6.4T 及更高速率场景下具有潜在优势。

## 在投资研究中的应用

### 对光模块测试设备的影响

根据[[source/Merit-光模块测试设备调研-260410|Merit-光模块测试设备调研-260410]]的调研结论：

- **CPO 不会消除对测试设备的需求**：尽管 CPO 改变了光模块的封装形态（从可插拔模块变为芯片级集成），但光电参数测试的本质需求不变。示波器、BER 测试仪、OSA 等核心测试设备仍然必需。
- **可能改变测试设备形态**：CPO 环境下的测试可能需要更精密的片上测试（on-chip testing）能力，对设备的接口和探针技术提出新要求。

### 投资含义

- CPO 商业化进展是[[industry/光模块测试设备|光模块测试设备]]行业的关键变量之一
- CPO 不颠覆测试需求的结论，对 [[company/Keysight|Keysight]]、[[company/Rigol|普源精电]] 等测试设备厂商是利好信号
- 需持续关注 CPO 在数据中心的实际部署时间线和规模

## NVIDIA 的 CPO 路线图

> ⚠️ 更新（2026-04-13）：NVIDIA 在 GTC 2026 明确 CPO 时间表。（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

- **NVIDIA Feynman 平台（2028）**：CPU 将集成 CPO 用于机架内 NVLink 交换机——Jensen Huang 在 GTC 2026 上明确表态
- CPO 是纯增量市场（替代机架内铜缆，在 1.6T 以上铜缆已不可行），**不替代可插拔光模块**
- CPO FAU（光纤阵列单元）单价量产预期 $150+（需耐 500–600°C 回流焊）

## CPO 对光模块厂商的价值链重构

> ⚠️ 更新（2026-04-13）：CPO 将重构光模块供应链价值分配。（来源：[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

- 光模块厂商（InnoLight/Eoptolink）在 CPO 时代竞争力将下降（缺乏 PIC/EIC 键合的半导体工艺能力）
- 价值将上移至掌握芯片和外部光源的 Coherent/Lumentum
- CPO 光互联毛利率将向传统 Scale-Out 光模块水平靠拢（短期 2–3 年无明确落地信号）

## 相关概念

- [[industry/光模块测试设备|光模块测试设备]]
- [[industry/光芯片]]
- [[concept/OCS架构]]
- [[company/Keysight|Keysight]]
- [[company/Rigol|普源精电]]

## 引用来源

- [[source/Merit-光模块测试设备调研-260410|Merit-光模块测试设备调研-260410]]
- [[source/cb-曦智科技IPO光芯片市场-260413]]
- [[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]
- [[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]
