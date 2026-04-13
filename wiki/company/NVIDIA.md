---
type: company
name: "NVIDIA Corporation"
ticker: "NVDA"
exchange: "NASDAQ"
sector: "半导体"
sub_sector: "AI 加速器 / GPU / 数据中心"
market_cap: "约 $5 万亿（2025 年）"
founded: "1993"
hq: "Santa Clara, CA, USA"
key_people: []
tags:
  - semiconductor
  - ai
  - compute
  - us
sources:
  - "[[source/substack-GPUs-6x-TurboQuant-260412]]"
  - "[[source/acecamp-Anthropic-ARR-算力合作-260412]]"
  - "[[source/cb-OpenAI梯云纵生态布局-260412]]"
  - "[[source/cb-AI服务器海外市场ODM-260412]]"
  - "[[source/cb-中美贸易谈判算力影响-260412]]"
  - "[[source/ace-CPU与GPU供需及国内格局-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
  - "[[source/ace-TPU出货更新与AI算力动态-260413]]"
last_updated: "2026-04-13"
confidence: high
---

# NVIDIA Corporation

## 公司概况

NVIDIA 是全球 AI 算力市场的绝对垄断者，GPU 在 AI 数据中心市场占有率超过 90%。Jensen Huang 领导下，公司从游戏显卡厂商转型为 AI 基础设施公司，市值突破 $5 万亿。

## 产品线

### 主要 AI 芯片产品

| 系列 | 产品 | 状态 |
|------|------|------|
| Hopper | H100, H200, H20 | EOL 推进中（H20 停产，恢复需 6 月+） |
| Blackwell | B200, B100, B30 | 主力产品（2025–2026 年） |
| Vera Rubin | — | 2026 年底发布，350x 吞吐 vs Hopper |

- B30：专为中国市场开发（降规格），单卡 $20,000–25,000，中美政策博弈中
- GB200/GB300：机柜式交付（144 柜标准），2025–2026 年主力产品

（来源：[[source/cb-AI服务器海外市场ODM-260412]]，[[source/cb-中美贸易谈判算力影响-260412]]）

### 软件生态

- **CUDA**：AI 计算事实标准，构成最强护城河
- **NVLink**：GPU 互联，大集群训练核心技术
- **全栈生态**：从芯片到框架到应用，形成完整闭环

## 市场格局

### 算力市场主导地位

- AI 数据中心 GPU 市占率：90%+
- 2024 年数据中心收入：绝对主导
- Vera Rubin 目标：2027 年底 GPU 累计销售额 $1 万亿（Jensen Huang）
- HBM 供应：与 Samsung/SK Hynix/Micron 签订多年合同

（来源：[[source/substack-GPUs-6x-TurboQuant-260412]]）

### 资本生态

- 早期投资 OpenAI（$1000 亿，以算力换股权）
- 投资 xAI（马斯克）
- 向 OpenAI 回流投资参与 Stargate 计划

（来源：[[source/cb-OpenAI梯云纵生态布局-260412]]）

## 主要客户需求（CSP，2026E）

### GB300 需求（柜，2026E）

| 客户 | GB300 2026E |
|------|-------------|
| Microsoft | ~28,000 |
| Google | ~19,000 |
| Meta | ~17,000 |
| AWS | ~15,000 |

（来源：[[source/cb-AI服务器海外市场ODM-260412]]）

## GTC 2026 更新：Rubin 平台与路线图

> ⚠️ 更新（2026-04-13）：NVIDIA GTC 2026 发布 Rubin 平台架构与 LPU 详情。（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

### Rubin 平台（当前主力）

- **LPU（Language Processing Unit）**：基于 Grok 技术（$200 亿授权收购）
  - 内置 SRAM ~500MB，数据传输带宽比 GPU 快 7 倍
  - 确定性执行（pre-scheduled），专为高速 token 生成设计
  - LPU 由三星代工（设计简单，无需台积电最先制程）
- **GPU+LPU 混合系统（NVIDIA Dynamo）**：token 生成效率最高提升 35 倍；每 GW 年收入可翻倍（$1,500 亿 vs 纯 GPU）
- LPU rack 与 GPU rack 建议比例：5 LPU : 8 GPU
- GPU+LPU 不会减少 HBM 需求：GPU 仍需 288GB HBM 处理 KV cache 加载任务

### Feynman 平台（2028 年路线图）

- **CPU 将集成 CPO**（Co-Packaged Optics）用于机架内 NVLink 交换机
- Jensen Huang 在 GTC 2026 明确表态：2028 年引入 CPO

（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

## 中国市场格局（2025–2026 年）

> ⚠️ 更新（2026-04-13）：中国 AI 芯片市场份额量化数据。（来源：[[source/ace-CPU与GPU供需及国内格局-260413]]）

- 中国 AI 芯片市场份额（2025 年）：NVIDIA ~55%（含灰色渠道）、AMD ~4%；NVIDIA+AMD 合计约 60%
- AMD 中国销售（2025 年全年）：MI308X+工作站显卡总销量约 16 万片（进口许可证限制，仅 6 个月有销售）
- **预计 2026 年 NVIDIA+AMD 中国合计份额将大幅下滑**（本土厂商获得市场窗口）
- 国内 AI 芯片分散格局：寒武纪、海光、平头哥、华为、沐曦、天数智芯等约 7–8 家头部厂商

1.6T 光模块中 NVIDIA 内部 Mellanox 供应：
- NVIDIA 通过 Mellanox 内部供应约占 1.6T 市场 20%（外部市场份额数据通常不含此部分）

（来源：[[source/ace-CPU与GPU供需及国内格局-260413]]，[[source/mm-1.6T光模块供应链与CPO-OCS访谈-260413]]）

## 竞争威胁

### ASIC 路线的挑战

Broadcom-Google-Anthropic 合作被认为是"去英伟达化"的标志性事件：
- 短期：英伟达地位不可撼动（GPU 需求仍主导市场）
- 中长期：ASIC 占比从 5% → 15%（2026E），持续分食英伟达份额
- TurboQuant 算法：让现有 GPU 效率提升 6x，降低购买新硬件的紧迫性

（来源：[[source/acecamp-Anthropic-ARR-算力合作-260412]]，[[source/substack-GPUs-6x-TurboQuant-260412]]）

### 中国市场压力

- H20 停产，H100 EOL，B30 政策待定
- 中国市场份额下滑：90%（2021）→ <70%（2025H1）
- B30 进入中国需中美双方政府批准

（来源：[[source/cb-中美贸易谈判算力影响-260412]]）

## 风险因素

- ASIC 路线长期分食市场份额
- TurboQuant 等算法降低硬件升级紧迫性
- 中国市场受出口管制持续萎缩
- 反垄断调查（数据中心 GPU 市占 90%+ 引发监管关注）
- 对 OpenAI 的集中依赖（60% 估值溢价来自 OpenAI 绑定）

## 催化剂

- Vera Rubin 2026 年底发布（350x 吞吐 vs Hopper）
- GPU 销售额 2027 年底 $1 万亿目标
- AI agent 时代驱动推理需求爆炸
- B30 进入中国市场（政策落地则大增量）

## 关键时间线

| 日期 | 事件 |
|------|------|
| 2026-03 | Jensen Huang 在 GTC 宣布 Vera Rubin，350x 吞吐；2027 年底 $1 万亿销售目标 |
| 2026E | B200 产品线 2026 年 B100 主力出货量 260–350 万片 |
| 2026 年底 | Vera Rubin 发布 |
| 2027 | 推理商业化时代主导，GPU 累计销售 $1 万亿目标节点 |

## 相关页面

- [[company/Broadcom]]
- [[company/Google]]
- [[company/OpenAI]]
- [[industry/AI基础设施]]
- [[industry/AI芯片]]
- [[industry/国产AI服务器]]

## 引用来源

- [[source/substack-GPUs-6x-TurboQuant-260412]]
- [[source/acecamp-Anthropic-ARR-算力合作-260412]]
- [[source/cb-OpenAI梯云纵生态布局-260412]]
- [[source/cb-AI服务器海外市场ODM-260412]]
- [[source/cb-中美贸易谈判算力影响-260412]]
