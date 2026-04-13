---
type: source
title: "AceCamp Doubao Channel Check: Doubao竞争格局、Qwen/Kimi/MiniMax、Claude Code Leak、算力供需"
source_type: transcript
author: "AceCamp - 行业专家"
date: "2026-04-13"
raw_path: "raw/2026-04-13/meeting_minutes/260413 - AceCamp Doubao Channel Check_ Competitive Landscape Shifts with Qwen, Kimi, and MiniMax Impact of Claude Code Leak Changes in Compute Power Supply and Demand_260413100925.md"
research_id: "69dca91f96aab61ca8ce44a2"
research_type: "meeting_minutes"
entities:
  - "[[company/字节跳动 (Doubao)]]"
  - "[[company/阿里巴巴]]"
  - "[[company/Kimi (Moonshot)]]"
  - "[[company/MiniMax]]"
  - "[[company/智谱]]"
  - "[[company/Anthropic]]"
  - "[[company/OpenAI]]"
  - "[[company/Google]]"
  - "[[company/DeepSeek]]"
  - "[[company/腾讯]]"
quality: high
tags:
  - ai
  - china
  - llm
  - competitive-landscape
  - compute
last_updated: "2026-04-13"
---

# AceCamp Doubao Channel Check：竞争格局 / Claude Code Leak / 算力（2026-04-13）

## 来源概要

行业专家对中国大模型市场三层结构、国内外模型能力差距、蒸馏策略、[[company/字节跳动 (Doubao)|字节跳动]]大模型团队人才流动、算力短缺现状以及文生视频竞争格局进行深度拆解。

## 关键要点

1. **国内市场三层结构**：
   - 大厂模型（Alibaba Qwen）：企业端市占率约 1/3，综合能力评分稳定在 85 分以上
   - 垂直模型公司（Kimi、智谱、MiniMax）：发展节奏类似美国 2023-2024，受益于 DeepSeek 开源红利
   - 追赶型大厂（字节跳动、腾讯）：资源丰富但基础模型相对弱，字节基础模型训练连续三个季度未有突破，60-70 人离职

2. **国内外模型能力差距**：
   - 核心功能差距（质变型）：Google Gemini 拥有端到端多模态基础模型（国内无一复制）；OpenAI GPT-4.5 具备超强 Agent 能力；Anthropic Claude 聚焦"Agent-as-a-Service"（Code/Work/Skills）
   - 技术性能差距：国内约落后 6-12 个月（一代），接近 Claude 3 系列或 GPT-4 水平

3. **蒸馏策略**：蒸馏持续有效，三大价值：训练效率提升、数据飞轮补充（补 Claude 的 Coding 数据优势）、R&D 架构洞察。字节严禁蒸馏（2025 春节起），阿里极少蒸馏，腾讯积极蒸馏（AWS/Google Cloud 频繁 API 违规标记），Kimi/智谱确认使用蒸馏。

4. **Claude 在 Coding 的数据飞轮（与共识不同的观点）**：Claude 的 Coding 优势已进入"2.0 时代"——开发者在 Claude 上开发 Agent，Claude 优先获得 Agent 开发模式数据，形成封闭的正向飞轮。竞争者蒸馏只能获取"输出数据"，而无法获取"用户反馈"这一更高价值的标注。

5. **字节 2025 年路线图**：
   - 5-6 月里程碑：C 2.5，对标 Kimi 2.5 的长上下文、原生多模态架构
   - 9-10 月里程碑："跨越式"模型，目标接近 Gemini 1.5 水平
   - Coding 独立团队 Q2 成立，目标年底达到 85 分（Claude 为 90+）
   - 备选方案：若目标未达成，将 R&D 中心转移至海外

6. **算力极度短缺**：字节以 2-3 倍溢价回购二手 H100/H800；腾讯被迫购买海光 10000 卡集群；C 端聊天机器人市场仅 A100 缺口就超过 10 万张；Kimi/智谱各缺约 10000 张 H100 用于 Coding

7. **文生视频竞争**：当前技术周期即将迭代，下一轮重心转向"一模型多场景"。主要玩家：可灵（快手）、万象（阿里）、C-Dance（字节）、VLOGGER（Google）。Google 有潜力凭借算力优势发动"降维打击"（支持 2 分钟 4K 视频）。

## 重要数据点

- Qwen 企业端市占率：约 **1/3**（跨所有云含私有化部署）
- 国内模型技术落后：约 **6-12 个月**（一代），接近 Claude 3 系列
- 字节 C 端聊天机器人 A100 缺口：**>10 万张**（实际进口不足 30 万张）
- 字节回购 H100/H800 溢价：**2-3 倍**
- Kimi 缺口：约 **10000 张 H100**，Zhipu 同等级别
- Ascend 910B：无法单独处理视频生成，仅能在 384 节点超集群场景下支持
- 华为 910B：仅处理 prefill 阶段，不适合训练
- 寒武纪 690：支持 ~64B 参数文本推理，不支持视频

## 值得注意的观点/引语

> "Claude 现在是 2.0 era 的优势——它的模型能够看到程序员如何开发 Agent，领先所有竞争者。这不是传统的数据优势，而是生态和时序优势。"（来源转述）

> "字节的 C-DANCE 2.0 领先是暂时的，因为文生视频每个技术阶段天花板都不高，到五六月技术就会进入下一个迭代周期，大家重新竞争。"

> "Google 有可能用算力优势发动降维打击，推出国内公司因算力短缺根本做不到的 2 分钟 4K 视频能力。"

## 结构性观察

1. **国内大模型赛道的人才旋转门正在形成**：核心人才路径：Kimi/智谱 → 字节跳动（被高薪挖角补强基础模型）；字节跳动 → 腾讯/阿里（海外时差、股权问题导致主动离职）。这种有规律的人才流动意味着国内各家的技术壁垒会随时间收窄，而不是扩大。

2. **算力短缺创造了不对称竞争优势**：中国市场的算力约束是对创业公司最大的结构性障碍——Kimi/智谱缺口 10000 张 H100 且"无处购买"，而字节已是唯一能提供大规模集群的算力托管方（Kimi 曾租用字节算力），这造成了字节的算力垄断优势，即使模型能力不够强。

3. **Doubao 的 C 端护城河是生态飞轮而非模型能力**：Doubao 将"pacifier"功能（陪伴、记忆）与抖音/电商生态深度整合，且将永久免费策略用至 2025 年才转向订阅，是典型的"以规模换锁定"的平台战略，而非技术竞争。

4. **蒸馏的边际成本正在上升**：DeepSeek CEO 已成立专项团队反蒸馏，OpenAI 也在积极部署反制措施，未来蒸馏的成本和风险将系统性上升，依赖蒸馏的公司需要提前规划。

## 与现有知识的关系

### 新增信息
- 字节大模型团队离职人数（60-70 人）和具体路线图（C 2.5，5-6 月；跨越式，9-10 月）
- 蒸馏各公司使用情况的直接来源
- Claude 2.0 时代数据飞轮描述
- 算力短缺的具体量化数据（缺口张数、溢价倍数）
- Claude Code Leak 影响（通过蒸馏，竞争者获取 Coding 数据）

### 印证之前观点
- Anthropic Claude 在 Coding 的领先地位（印证 acecamp-Anthropic-ARR-算力合作-260412）
- Doubao 在 C 端的主导地位（与此前 Doubao 调研一致）

### 矛盾/需修正
- 无重大矛盾

## 后续跟进项
- 字节 C 2.5 发布（5-6 月）：是否真正实现 Kimi 2.5 对标能力
- 字节"跨越式"模型（9-10 月）：是否实现 Gemini 1.5 水平
- DeepSeek 反蒸馏技术措施进展
- Kimi 3.0 发布（KDA 架构集成）

## 引用来源

原始文件：`raw/2026-04-13/meeting_minutes/260413 - AceCamp Doubao Channel Check...`
