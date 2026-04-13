---
type: concept
name: CSP 自研芯片（超大规模云厂商自研 AI 芯片）
aliases:
  - "XPU"
  - "超大规模自研 ASIC"
  - "云厂自研芯片"
category: "strategy"
tags:
  - semiconductor
  - ai
  - compute
  - cloud
sources:
  - "[[source/ace-TPU出货更新与AI算力动态-260413]]"
  - "[[source/ace-CPU与GPU供需及国内格局-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
last_updated: "2026-04-13"
---

# CSP 自研芯片

## 定义

CSP 自研芯片是指超大规模云厂商（Google、AWS、Microsoft、Meta 等）针对自身 AI 计算需求自行设计的专用芯片（ASIC），区别于采购 NVIDIA/AMD 等通用 GPU。主要动机：成本控制（声称比 NVIDIA 成本效益高 30–40%）和供应链安全。

（来源：[[source/ace-CPU与GPU供需及国内格局-260413]]）

## 在投资研究中的应用

### 主要厂商现状

| 厂商 | 自研芯片 | 用途 | 外部商业化 |
|------|---------|------|----------|
| Google | TPU v7/v8 | 训练+推理 | 有（GCP 对外） |
| AWS | Trainium（训练）/ Inferentia（推理） | 训练+推理 | 有（对外销售） |
| Meta | MTIA | 推理 | 无（仅内部） |
| Microsoft | 已决定自研基座模型+自研芯片 | 训练+推理 | 待定 |

### 关键财务数据

- AWS Trainium 自研芯片年收入：**>$100 亿**（三位数增长，2026）
- AWS 声称 vs NVIDIA：成本效益高 30–40%（去除 NVIDIA 65% 营业利润率的逻辑）
- Google Anthropic 3.5GW 合作：对应约 400 万颗 TPU v8，2027 年运营

（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]，[[source/ace-TPU出货更新与AI算力动态-260413]]）

### 时间表：推理替代 vs 训练替代

| 场景 | 时间表 | 说明 |
|------|-------|------|
| 推理市场大规模替代 | 2025–2027 年（进行中） | 成本优势显著，软件适配相对容易 |
| 训练市场大规模替代 NVIDIA | 2028 年以后 | 软件生态复杂，NVIDIA 护城河深 |

（来源：[[source/ace-CPU与GPU供需及国内格局-260413]]）

### 中国 CSP 自研能力

- 国内 CSP（百度、腾讯等）自研能力弱于海外（Google、AWS）
- 现阶段仍以采购国内第三方（寒武纪、海光、华为昇腾）为主
- 中国推理市场发展速度和占比可能高于海外（训练端仍依赖 NVIDIA/AMD）

（来源：[[source/ace-CPU与GPU供需及国内格局-260413]]）

### CSP vs Neocloud 建设模式分化

- **传统 CSP**：连续性自建，供应链控制力强，抗扰动能力强
- **Neocloud（CoreWeave 等）**：项目型外包，第三方建设，供应链冲击下影响最大
- 结论：未来算力建设份额可能向大型 CSP 集中

（来源：[[source/ace-TPU出货更新与AI算力动态-260413]]）

## 结构性观察

- CSP 自研的最大意义是"重置 AI 算力成本基础"——每个 CSP 通过自研绕开 NVIDIA 65% 营业利润率的部分，形成结构性的价格优势
- 自研训练芯片替代要到 2028 年以后（时间比市场预期更晚），但自研推理已在大规模进行

## 相关概念

- [[concept/Arm架构服务器CPU]]
- [[concept/CPO]]
- [[industry/AI基础设施]]
- [[industry/AI芯片]]

## 引用来源

- [[source/ace-TPU出货更新与AI算力动态-260413]]
- [[source/ace-CPU与GPU供需及国内格局-260413]]
- [[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]
