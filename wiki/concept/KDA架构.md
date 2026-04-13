---
type: concept
name: "KDA架构（Kimi Dynamical Attention）"
aliases:
  - "Mew架构"
  - "KDA"
category: "strategy"
tags:
  - ai
  - architecture
  - kimi
  - china
sources:
  - "[[source/ace-头部AI模型竞争格局-260413]]"
  - "[[source/mm-AceCamp-Doubao-竞争格局-260413]]"
last_updated: "2026-04-13"
---

# KDA 架构（月之暗面 Kimi）

## 定义

KDA（Kimi Dynamical Attention）是[[company/Kimi (Moonshot)|月之暗面（Kimi）]] 2026 年 4 月发布的新模型架构，属于 Mew 架构体系的一部分。核心创新在于 Transformer 的 Attention 机制：**每一层增加一个 attention head，实现权重的动态聚焦**，而非传统的等权重叠加。

（来源：[[source/ace-头部AI模型竞争格局-260413]]）

## 技术细节

- **变化点**：改变了对 attention 残差的计算方式
- **机制**：通过在每一层增加一个 attention head，实现推理过程中的动态权重聚焦
- **维度**：基于推理深度的 Transformer 机制（非传统时间序列机制）
- **效果**：对推理优化（特别是数学推理、长上下文）有显著提升

## 重要性

1. **业界评价**：被视为 Attention 机制上的重大科研突破，体现了 Kimi 团队的顶尖科研实力
2. **对推理成本的影响**：通过架构优化减少不必要的计算，预计降低推理成本
3. **预计应用**：整合进未来的 **Kimi 3.0 版本**
4. **竞争意义**：Kimi K2.5 在 Coding 上已领先智谱 GLM-5，KDA 架构若成功将进一步扩大与 MiniMax 等的技术差距

## 在投资研究中的应用

- 评估 Kimi 技术护城河深度：KDA 是 Kimi 科研能力的信号，与 MiniMax 等"性价比路线"形成明显分化
- 国内其他竞争者应对：ByteDance 不做 KDA 级别的架构创新，仍在微创新；MiniMax 的应对策略是专注差异化（多模态），而非直接对标 KDA

## 相关概念

- [[concept/Wan2.2-Animate架构]]（另一个架构创新概念）

## 引用来源

- [[source/ace-头部AI模型竞争格局-260413]]
- [[source/mm-AceCamp-Doubao-竞争格局-260413]]
