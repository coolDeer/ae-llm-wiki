---
type: company
name: "月之暗面（Kimi）"
ticker: ""
exchange: ""
sector: "AI / 人工智能"
sub_sector: "大模型 / Foundation Models"
market_cap: "非上市，现金流充足（融资状况较好）"
founded: "2023"
hq: "北京，中国"
key_people: []
tags:
  - ai
  - china
  - llm
sources:
  - "[[source/mm-AceCamp-Doubao-竞争格局-260413]]"
  - "[[source/ace-头部AI模型竞争格局-260413]]"
last_updated: "2026-04-13"
confidence: medium
---

# 月之暗面（Kimi）

## 公司概况

月之暗面（Kimi）是国内领先的垂直大模型公司，核心产品为 Kimi 大语言模型系列，以长上下文、原生多模态和 Agent 能力著称。公司现金流充足，被认为是中国国内技术架构最完善的基础模型之一。

（来源：[[source/mm-AceCamp-Doubao-竞争格局-260413]]）

## 商业模式

- API 对外服务（B2B 和 C 端）
- 核心优势场景：长上下文推理、Coding Agent、原生多模态
- 曾租用字节跳动大规模 GPU 集群进行预训练（2024、2025 年），2025 年下半年起停止租用（改用蒸馏）

## 技术架构

### 核心能力

- **参数规模**：约 1 万亿（1T）总参数，活跃参数约 30B，是 MiniMax 的约 3 倍
- **三大特性**：长上下文推理 + 高速 + 高精度
- **原生多模态**：视觉理解（图像 OCR）已原生集成进基础模型
- **Agent 能力**：可自动生成并执行 Agent 代码，支持多 Agent 协作

### KDA 架构（最新创新）

（来源：[[source/ace-头部AI模型竞争格局-260413]]）

- 2026 年 4 月发布，被业界视为重大科研突破
- **核心机制**：改变 attention 残差的计算方式，每一层增加一个 attention head 实现权重动态聚焦（而非简单等权重叠加）
- **非时间序列**：基于推理深度的 Transformer 机制，对推理优化有显著效果
- **Mew 架构**：KDA 是 Mew 架构体系的一部分，同等级别的创新
- **预计用途**：整合进 Kimi 3.0 版本
- 当前 Kimi 2.5 已具备图像输入双模态能力

## 竞争格局

- **vs 智谱**：Kimi K2.5 Coding 表现优于 GLM-5，发布时间早约 1 个月
- **vs MiniMax**：更强的 Coding 产品力，参数量 3-4 倍于 MiniMax；MiniMax 的极致性价比是 Kimi 的最大对手
- **vs ByteDance**：ByteDance 将 Kimi 架构作为对标基准（C 2.5 目标匹配 Kimi 2.5）
- **vs Anthropic Claude**：国内 Coding 市场的最强对手仍是 Claude，Kimi 在本土化和价格上有优势

## 蒸馏策略

确认使用蒸馏（来源：[[source/mm-AceCamp-Doubao-竞争格局-260413]]）
- 2025 年下半年模型（K2.2/K2.5）发布时停止了对字节大规模集群的租赁，改用蒸馏节省计算
- 蒸馏 Claude Coding 数据是 Coding 能力建立的重要来源之一

## 算力约束

- 缺口约 **10,000 张 H100**，无渠道购买，是主要增长约束
- 被列入实体清单（间接影响，无法获得最新英伟达 GPU）

## 风险因素

- 算力硬约束限制扩张
- Coding Agent 赛道竞争激烈（Anthropic Claude 主导全球）
- 人才被字节跳动挖角
- C 端市场被 Doubao 主导，上升空间有限

## 催化剂

- Kimi 3.0（KDA 架构集成）：可能是新一轮技术跃升
- 多模态扩展（视频输入）计划中
- B2B SME 市场 Agent 需求爆发

## 相关页面

- [[company/MiniMax]]
- [[company/智谱]]
- [[company/字节跳动 (Doubao)]]
- [[concept/KDA架构]]

## 引用来源

- [[source/mm-AceCamp-Doubao-竞争格局-260413]]
- [[source/ace-头部AI模型竞争格局-260413]]
