---
type: output
title: "投资研究每日复盘 — 2026-04-13 (v2 - 应用 Q7 硬指标)"
date: "2026-04-13"
sources:
  - "[[source/ace-TPU出货更新与AI算力动态-260413]]"
  - "[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]"
  - "[[source/ace-核聚变降本警示-260413]]"
  - "[[source/cb-六维力传感器-260413]]"
  - "[[source/mm-AceCamp-Claude-Mythos-网络安全-260413]]"
  - "[[source/mm-AceCamp-Doubao-竞争格局-260413]]"
  - "[[source/ace-头部AI模型竞争格局-260413]]"
  - "[[source/ace-银屑病IL-23p19-IL-36R-恒瑞-260413]]"
  - "[[source/mm-海尔智家FY25管理层交流-260413]]"
  - "[[source/mm-迈瑞医疗BofA交流-260413]]"
  - "[[source/mm-翰森制药Nomura交流-260413]]"
  - "[[source/mm-Merit-Applovin-Unity-广告-260413]]"
  - "[[source/mm-Merit周度路演-260413]]"
  - "[[source/mm-Tsuruha-BofA-260413]]"
  - "[[source/mm-Tsuruha-MS-260413]]"
  - "[[source/mm-Tsuruha-Nomura-260413]]"
  - "[[source/mm-MOL-JPM-260413]]"
  - "[[source/vk-US-Iran-followup-260413]]"
  - "[[source/ace-41号令储能影响-260413]]"
  - "[[source/cb-Sakana-AI-260413]]"
  - "[[source/cb-LiblibAI-260413]]"
  - "[[source/cb-OpenAI-Atlas浏览器-260413]]"
  - "[[source/mm-GS-大阪有机化学-260413]]"
  - "[[source/mm-MS-大阪有机化学-260413]]"
tags:
  - daily-review
  - qa
  - 资深投资者视角
last_updated: "2026-04-13"
---

# 投资研究每日复盘 — 2026-04-13 (v2)

> **本文件是 v2 重跑版**：v1 创建于 SKILL.md 加入 Q7 硬指标之前；本次重跑应用了两条新硬规则——**sell-side 占比硬指标** + **7 天冷却期**。
> 基于当日 **63 份 source** 回答 7 个标准问题。
> **重要**：今天没有任何 `wiki/comparison/` 或 `wiki/output/` 页面满足 7 天冷却期（最老的也只有 2 天），因此本文件的所有结论**直接 ground 在 source 页**，不引用任何 comparison/output 作为 anchor。

---

## Q1: 今天最大的认知变化

5 条按重要性排序：

### 1. ⚠️ 矛盾 — TPU v8x 推迟 1–2 个月（联发科 IO IP 速率不足 + 良率偏低）
[[company/联发科 (MediaTek)]] 负责的 IO die 因内部新 IO IP 速率未达设计带宽 + 封测良率偏低，TPU v8x 量产推迟 1–2 月；TPU v8ax（[[company/Broadcom]] 设计）要 2026Q3 末–Q4 初才小批量送测；微软数据中心延迟 2–4 季度，Meta 延迟 2–3 季度+，[[company/CoreWeave]] 等 neocloud 受影响最大（来源：[[source/ace-TPU出货更新与AI算力动态-260413]]）。
- **vs wiki**：直接挑战 [[source/acecamp-Anthropic-ARR-算力合作-260412]] 中 Anthropic-Google-Broadcom 3.5GW 长协的近期交付路径。
- **投资含义**：长期 ASIC 方向不变，但短期 timeline 后移 1–2 季度。

### 2. ⚠️ 矛盾 — NVIDIA Rubin LPU + Feynman CPO + 中国份额 55%
[[company/NVIDIA]] GTC 2026 发布 Rubin 平台 LPU，内置 ~500 MB SRAM，带宽比 GPU 快 7×；GPU+LPU 混合 token 效率 **+35×**；每 GW 年收入 **$750 亿 → $1500 亿翻倍**；中国市场份额维持 **55%**；Feynman 2028 集成 CPO（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）。
- **vs wiki**：与 [[source/Merit-Anthropic企业业务调研-260410]] / [[source/acecamp-Anthropic-ARR-算力合作-260412]] 中"算力去英伟达化"叙事形成对照——**护城河在加宽**。
- **投资含义**：NVIDIA 短中期 inherently bullish。

### 3. ⚠️ 矛盾 — 核聚变降本逻辑被 Nature Energy 顶刊系统性修正
Nature Energy 2026（DOI: 10.1038/s41560-026-02023-8）：经验率假设从普遍的 8–20% 修正为 **2–8%**；磁约束最小单位 ~530 MW，复杂度评分 **6.8**（高于核裂变电站）；首台聚变电站 CAPEX $1,404–$43,000/kW，跨度 **30 倍**（来源：[[source/ace-核聚变降本警示-260413]]）。
- **vs wiki**：与 [[source/cb-fusion-260412]] 的乐观判断（中国聚变玩家扩张、高温超导带材需求）矛盾。
- **结构性观察**：商业公司 vs 体制内院所的预期系统性分裂，资本市场偏向乐观叙事是 systemic bias。
- **投资含义**：聚变可能限定在算力中心 / 战略储备等高价值场景。

### 4. ⚠️ 矛盾 — "具身智能"90% 落地为伪命题（FANUC 资深专家警示）
工业机器人 10+ 年从业的 FANUC 背景专家直接表态："很多人形机器人去落地的时候……全部都是采用传统视觉加轨迹规划的做法，做这样的事情是完全没有任何意义的"。点名 [[company/智元]]（工业场景预编程）/ [[company/宇树]]（运动控制强但灵巧手投入少）/ [[company/优必选]]（与宝马合作但传统预编程）（来源：[[source/cb-六维力传感器-260413]]）。
- **vs wiki**：与 [[source/cb-1X-NEO-260412]] / [[source/cb-Xpeng-IRON-260412]] / [[source/cb-六维力传感器-260412]] 都偏乐观矛盾。
- **投资含义**：六维力传感器 TAM 系统性高估；具身智能 vs 预编程的边界**应成为投资筛选的硬标准**。

### 5. ✦ 净新 — Anthropic 进入进攻性网络安全（Claude MythOS Preview）
[[company/Anthropic]] 与某 Unit 42 背景网络安全公司合作 Project Glasswings；Claude MythOS 具备**意图感知攻击**（感知 prompt 中恶意意图触发"绝望""敌对"心态）+ 类人渗透测试（动态扫描、实时编写 Python、挖掘深层漏洞）。**现有 policy 型防火墙 / WAF 几乎无防御能力**（来源：[[source/mm-AceCamp-Claude-Mythos-网络安全-260413]]）。
- **vs wiki**：完全 net new。原 [[source/Merit-Anthropic企业业务调研-260410]] 中 Anthropic B 端商业化主要是 Claude Code + API。
- **投资含义**：Anthropic B 端进入更深路径——**安全防御范式重塑者**。

> **注**：上述 4 条矛盾在今天另一次 query 中已固化为 `comparison/2026-04-12-vs-04-13-叙事修正`，但**该 comparison 页 0 天 < 7 天冷却期**，本 daily-review 不引用它作为 anchor，所有结论独立 ground 在 source 页。

---

## Q2: 反共识数据点 / Expectation Gap

按 surprise 强度排序：

### 1. NVIDIA 中国份额 55%（vs 共识"H20 受限后大跌至 30%"）
- **新数据**：维持 **55%**（来源：[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）
- **Gap 方向**：**强利好 NVDA**，强利空国产 AI 芯片（[[company/寒武纪]] / [[company/海光]] / [[company/沐曦]]）的近期估值

### 2. 阳光电源 FY26 净利预期 106-107 亿（vs 共识 80-90 亿）
- **新数据**：**106-107 亿，PE ~16.5×**；PowerTitan 3.0 降本 12% + 800V 高压直流可能开启 AIDC 配储新市场（来源：[[source/mm-Merit周度路演-260413]]）
- **Gap 方向**：**利好阳光电源**

### 3. 恒瑞 SHR-1139 IL-23p19/IL-36R 双靶点 PASI 90 = 100%（高剂量 52 周）
- **市场共识**：IL-23/IL-17 老靶点 PASI 90 ~80% 是天花板
- **新数据**：[[company/恒瑞医药]] SHR-1139 16 周 PASI 90 = 66.7-83.3%，**52 周高剂量组 100%**，无严重不良事件（来源：[[source/ace-银屑病IL-23p19-IL-36R-恒瑞-260413]]）
- **Gap 方向**：**强利好恒瑞**（FIC 全球首创双靶点）

### 4. 核聚变经验率 2-8%（vs 普遍 8-20%）
- **新数据**：Nature Energy 28 位专家评估合理区间 2-8%，**整整低一个量级**（来源：[[source/ace-核聚变降本警示-260413]]）
- **Gap 方向**：**强利空**通用聚变商业化叙事

### 5. AppLovin Q1 实际增速低于预期 + Unity 17-19% 远低于早期 35%
- **市场共识**：广告复苏温和，二线平台 15-20%
- **新数据**：游戏广告主 Q1 实际 +15%（vs 预期 +20%），Unity Q1 17-19%（vs 早期预期 35%），AppLovin CPM QoQ +30% 但客户预算回流一线 Meta/Google（来源：[[source/mm-Merit-Applovin-Unity-广告-260413]]）
- **Gap 方向**：**双向**——Meta/Google 强于二线广告平台

### 6. 海尔智家 Casarte 高端线 OPM ~20%（vs 共识中国家电低毛利）
- **新数据**：[[company/海尔智家]] Casarte 2025 OPM **~20%**，双位数收入增长（来源：[[source/mm-海尔智家FY25管理层交流-260413]]）
- **Gap 方向**：**利好高端化战略奏效的中国家电**

---

## Q3: 跨板块串联

### 1. ⚠️ 削弱主题：算力去英伟达化
**反向证据**：
- TPU v8x 推迟 1-2 月（[[source/ace-TPU出货更新与AI算力动态-260413]]）
- NVIDIA Rubin LPU 35× token 效率 + Feynman 2028 CPO + 中国 55%（[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]）

**结论**：长期 ASIC 方向不变，但短期 timeline 后移 1-2 季度，NVIDIA 护城河在加宽。

### 2. ✓ 强化主题：反内卷（4 个板块同时印证）
- **化工**：[[company/大阪有机化学工业]] **GS + MS 两家券商同日双覆盖**（[[source/mm-GS-大阪有机化学-260413]] + [[source/mm-MS-大阪有机化学-260413]]）——日本特殊化学品在中国卷不动后形成稀缺溢价
- **储能**：国家发改委 41 号令收紧储能 + 阳光电源 PowerTitan 3.0 通过技术创新而非价格战突围（[[source/ace-41号令储能影响-260413]] + [[source/mm-Merit周度路演-260413]]）
- **日本药妆**：[[company/Tsuruha Holdings 3391]] **三家券商同日横评**（[[source/mm-Tsuruha-BofA-260413]] + [[source/mm-Tsuruha-MS-260413]] + [[source/mm-Tsuruha-Nomura-260413]]）——整合后规模效应是反内卷的另一种形式
- **半导体**：04-12 已有 Skyworks-Qorvo 合并、电子特气 WF6 涨价、大陆硅片国产化主题，今天延续

**结论**：[[concept/反内卷]] 是今天最强的跨板块主题，2026 年是结构性整合年。

### 3. ✦ 净新主题：AI 应用层"模型力 vs 数据飞轮 vs 渠道护城河"三分化
- **数据飞轮型**：[[company/LiblibAI]] >2000 万用户 + 订阅 >70% + Star Alpha 自研模型（[[source/cb-LiblibAI-260413]]）
- **架构创新难复制型**：[[company/Sakana AI]] CTM 架构训练成本低 100×、灵活性极差，"一家大厂无法复现"（[[source/cb-Sakana-AI-260413]]）
- **渠道捆绑型**：[[company/OpenAI]] Atlas 浏览器 macOS + Agent + **不做广告变现**（[[source/cb-OpenAI-Atlas浏览器-260413]]）
- **激进追赶型**：[[company/字节跳动 (Doubao)]] 从智谱挖人 + Kimi K2.5 反超 GLM-5（[[source/mm-AceCamp-Doubao-竞争格局-260413]] + [[source/ace-头部AI模型竞争格局-260413]]）

**结论**：AI 应用层不再是"哪家模型最强"的故事，投资人应明确判断每个标的的护城河类型。

### 4. ✓ 强化主题：中国创新药从 "Me-too" 到 "FIC + BD 出海"
- 恒瑞 SHR-1139 FIC 双靶点（[[source/ace-银屑病IL-23p19-IL-36R-恒瑞-260413]]）
- [[company/翰森制药]] Hansoh 3692 BD 出海 + 2094 减重药（[[source/mm-翰森制药Nomura交流-260413]]）
- [[company/迈瑞医疗]] 300760 IVD 国产替代 12% → 20%，2026Q3 拐点（[[source/mm-迈瑞医疗BofA交流-260413]]）

**结论**：中国创新药 + 医疗器械同时出现"代际切换"信号，速度快于预期。

---

## Q4: 高确信度多头方向

### 首选：**[[company/NVIDIA]] (NVDA US)**

**逻辑**：今天 3 个独立信号同时支持——
1. TPU v8x 推迟 1-2 月（去英伟达化时间表后移）
2. Rubin LPU 35× token 效率 + 每 GW 年收入翻倍
3. 中国份额维持 55%（共识太悲观）

**催化剂**：
- **2024H2**：Rubin 平台量产 + Blackwell Ultra 大规模出货
- **2026Q1**：Q4 财报 + Rubin LPU 实际 token 效率验证
- **2026 全年**：TPU v8x 延迟 → CSP 转向 NVIDIA 现货补单
- **2027**：Feynman 路线图细节公布

**时间窗口**：短-中期 **6-12 月**

**主要风险**：
1. AMD MI 系列在 CSP 拿大单（Meta PSI 重组暗示多源化）
2. 中国本土卡国产替代加速（[[company/寒武纪]] / [[company/海光]] 突破）
3. 估值已 high，single-quarter miss 可能 -10%+ 回调
4. 中国出口管制升级

**Invalidation / 止损**：
- 中国份额跌破 **40%**
- Rubin 量产延迟 ≥ 1 季度
- Rubin LPU 实际 token 效率 < **20×**
- 任一 CSP 公布"自研 ASIC 替代 NVIDIA 50%+ workload"

**仓位建议**：核心仓 + 短期加仓（不超过总仓位的 10-15%）

### 备选：**[[company/阳光电源]] (300274.SZ)**
FY26 净利 106-107 亿 vs 共识 80-90 亿，PE 16.5× 安全边际。**催化剂**：Q1 财报 + PowerTitan 3.0 商业化。

---

## Q5: 高确信度空头 / 减仓方向

### 首选：**减持依赖"具身智能 = AI Agent"叙事的标的**

**最具体的标的**：[[company/小鹏汽车]] (XPEV) — IRON 量产时间表与具身智能定义直接相关，今天的 FANUC 专家警示削弱了 IRON 的"具身智能"叙事溢价。

**为什么动**：
- **关键数据**：FANUC 背景资深专家直接说"做这样的事情完全没有任何意义"——来自工业机器人 10+ 年从业者的硬话
- **结构性观察**：六维力传感器 TAM 系统性高估；表演型机器人不需要灵巧手

**催化剂（向下）**：
- 2026Q2-Q3 任何人形机器人厂商发布"端到端学习 demo"失败
- 1X NEO 2026 计划交付推迟
- 第三方独立评测显示当前人形机器人 = 工业机械臂 + 语音封装

**时间窗口**：短-中期 **3-9 月**

**Invalidation**：
- 出现真正端到端的具身智能 demo（非预编程 + 非简单视觉伺服）
- 具身智能 RL/IL 训练成本下降 10×

**仓位建议**：减持 / 暂不加仓

### 备选：减持纯聚变叙事股
中国聚变玩家多为国企不上市；若有任何"聚变概念股"在 wiki 中被乐观引用（如 [[industry/可控聚变]] 中"联创光电转 FRC"——昨天已标注待证实），今天的 Nature Energy 顶刊给出非常清晰的"减仓理由"。

---

## Q6: 知识缺口与下一步 ingest 优先级

### 1. NVIDIA 中国 55% 份额的实际拆解（**最高优先级**）
- **缺口**：是 H20 / 改良版 / 走私 / 还是 B20、B30 等替代品？哪些客户在买？
- **重要性**：Q4 多头逻辑的核心证据。如果 55% 是"短期补库存"而非"持续份额"，论点崩塌
- **建议获取**：SemiAnalysis Dylan Patel 最新 China substack、香港代理商 channel check、NVDA 财报会 Q&A

### 2. TPU v8x 良率回升节奏 + v8ax 实际送测时间（**高**）
- **缺口**：联发科 IO IP 问题是"封测良率优化"还是"硅片重新流片"？前者 1-2 月可解，后者 3-6 月
- **重要性**：直接决定"算力去英伟达化"时间表的修正幅度
- **建议获取**：台积电封测厂 channel check、Broadcom CEO 下次电话会 Q&A

### 3. 恒瑞 SHR-1139 Phase 2/3 时间表 + 海外 BD 计划（**高**）
- **缺口**：Phase 2/3 何时启动？是否有海外授权？
- **重要性**：Q4 备选多头 + 中国创新药主题验证
- **建议获取**：恒瑞最新研发管线披露、AAD 2026 后续摘要、专门的恒瑞专家访谈

### 4. 真正端到端具身智能 demo 进展（**中**）
- **缺口**：是否有任何中国/海外公司已做出非预编程 demo？1X NEO 2026 实际交付状态？
- **重要性**：Q5 空头逻辑的 invalidation condition
- **建议获取**：1X NEO 实地评测、Figure 最新 demo、Skild AI / Physical Intelligence 动态

### 5. AppLovin / Unity Q1 财报数据（**中**）
- **缺口**：Channel check 显示 Q1 实际低于预期，但官方数据待 5 月披露
- **建议获取**：5 月 AppLovin / Unity Q1 财报 + Q2 guidance（被动等待）

### 质量不足 / 单一信源
- **[[source/cb-六维力传感器-260413]]**：FANUC 资深专家**单一信源**，需 ≥2 个独立信源（Boston Dynamics、Figure、智元 内部专家）交叉验证
- **[[source/ace-核聚变降本警示-260413]]**：来自 single Nature Energy paper，学术共识形成需要时间
- **[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]**：JST Consulting CEO 第三方解读，Rubin LPU 35× token 效率是宣传数字，量产后需独立基准

---

## Q7: 自我红队（Bias Check）— 应用 v2 硬指标

### 🔧 硬指标 1：Sell-side 占比检查

**今天 source 类型分布（共 63 份）**：

| 类型 | 数量 | 占比 | 分类 |
|---|---|---|---|
| acecamp_article | 15 | 23.8% | 专家网络 / 独立研究 |
| chat_brilliant | 18 | 28.6% | 1-on-1 专家电话 |
| meeting_minutes (纯卖方) | 19 | **30.2%** | **Sell-side broker** |
| meeting_minutes (AceCamp / Merit / Taclink / warren) | 9 | 14.3% | 专家网络 |
| vital_knowledge | 2 | 3.2% | 独立宏观新闻 |

**纯 sell-side 占比 = 19 / 63 = 30.2%** → ✅ **未触发 50% 警示线**

**纯卖方券商分布**：BofA × 2 / Daiwa × 2 / GS × 4 / JPM × 1 / MS × 4 / Nomura × 4 / SMBC × 2

**虽未触发硬警示，仍需注意的偏差风险**：
- [[company/Tsuruha Holdings 3391]] 的判断完全来自 BofA + MS + Nomura **同日三家覆盖**——是 3 家共识而非 3 个独立观点（分析师可能在同一 IR 会议听同一管理层）
- [[company/海尔智家]] / [[company/迈瑞医疗]] / [[company/翰森制药]] 都是"管理层电话会 + 卖方笔记"，管理层语气总是偏正面
- **Q4 NVIDIA 多头**部分依赖 SMBC 这一份 sell-side 解读（[[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]），需注意其偏多倾向

### 🔧 硬指标 2：7 天冷却期检查

**今天可能引用的 comparison/output 页面 last_updated 检查**：

| 页面 | last_updated | 距今天数 | 7 天冷却期 |
|---|---|---|---|
| `comparison/2026-04-12-vs-04-13-叙事修正` | 2026-04-13 | **0 天** | ❌ **不可作 anchor** |
| `output/投资总结报告-260412` | 2026-04-13 | **0 天** | ❌ **不可作 anchor** |
| `output/投资总结报告-260410` | 2026-04-11 | **2 天** | ❌ **不可作 anchor** |

**结论**：今天**没有任何**符合冷却期的 comparison/output 页面。本 daily-review 全部结论**直接 ground 在 source 页**，不引用任何 comparison/output 作为 anchor。

> **这正是冷却期规则的设计目的**：防止 daily-review 反复引用自己刚创建的同主题输出页面形成循环论证。今天就是最典型的应用场景——comparison/2026-04-12-vs-04-13-叙事修正 与本 daily-review 共享同一组 source，互相引用是循环。

### 其他 bias 检查

**3. ⚠️ Confirmation bias 风险**
今天 Q1 的 5 条认知变化里 **4 条都是反向证据**。是否过度强调反向？
- **反问**：如果今天的 source 集合换一组（多 5 份偏 ASIC 多头的 sell-side），会不会得出完全相反的 "ASIC 加速" 结论？
- **建议**：下次 daily-review 应主动寻找 1-2 条"04-12 乐观叙事仍未被推翻"的证据作为对冲

**4. ⚠️ "我希望它真" 风险**
"算力去英伟达化时间表后移" 高度依赖**单一 AceCamp 专家访谈**（TPU v8x 推迟）。
- **反问**：如果联发科真的是"1 个月修复 IO IP"而非"3-6 个月重新流片"，整个论点崩塌。是否过度依赖单一信源？

---

## 引用来源

**核心 5 份**：
- [[source/ace-TPU出货更新与AI算力动态-260413]]
- [[source/mm-SMBC-NVIDIA-GTC2026光互联趋势-260413]]
- [[source/ace-核聚变降本警示-260413]]
- [[source/cb-六维力传感器-260413]]
- [[source/mm-AceCamp-Claude-Mythos-网络安全-260413]]

**支撑 19 份**：见 frontmatter `sources` 完整列表

**横向参考（仅作"今日 query 副产品"标记，不作 anchor）**：
- `comparison/2026-04-12-vs-04-13-叙事修正`（0 天 < 7 天冷却期）
- `output/投资总结报告-260412`（0 天 < 7 天冷却期）
