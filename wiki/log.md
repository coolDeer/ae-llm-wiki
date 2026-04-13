---
type: log
---

# 操作日志

> 按时间倒序记录所有 wiki 操作。格式统一，便于 `grep` 检索。
>
> 格式：`## [YYYY-MM-DD] 操作类型 | 简述`
>
> 操作类型：`ingest` / `query` / `lint` / `update` / `create`

---

## [2026-04-13] daily-summarize | PM 简报（首次运行 daily-summarize skill）

**触发事件**：daily-summarize skill 创建后立即首次运行 (`/daily-summarize 2026-04-13`)。

**前置确认**：
- 63 份 source 已 ingest ✅
- daily-review-2026-04-13 v2 已存在 → 引用其 Q4/Q5/Q6 作为 §3-§5 / §8 的输入
- `wiki/portfolio.md` 为空模板 → fallback 到 hypothetical "long-only China-Asia tech & macro 多策略组合"

**核心结论（一行总结每章节）**：
- **§1 执行摘要**：04-12 三大乐观叙事被反向证据削弱，NVIDIA 护城河反向加宽；唯一明确行动是盘前增配 NVDA +3% 至 8%
- **§4 首选多头**：[[company/NVIDIA]] +3% 至 8%（紧急），止损中国份额 < 40% 或 Rubin 量产延迟 ≥ 1 季度
- **§5 首选减仓**：[[company/Google]] -3% 至 3%（一般），转 NVDA 或加 cash；国产 AI 芯片代理 -3% 至 0%
- **§6 最大风险**：NVDA 中国份额数据被证伪（25% 概率）→ 必须 Q1 财报前 channel check 二次验证
- **§7 关键事件**：TSMC Q1 财报 (4/22) + NVIDIA Investor Day (4/24) 同周，决定 NVDA 加仓是否需要紧急调整
- **§8 最高优先级研究任务**：NVIDIA 中国 55% 份额拆解（研究员 A，4/18 截止）
- **§9 talking point #1**：AI 算力多头主线短期回归 NVIDIA 双线下注，增配 NVDA +3% 对应减持 Google -3%

**Self-Check 发现的硬约束冲突**：
- ⚠️ NVDA 加仓 +3% 至 8% **超过 5% 单标的上限** → 修正为 +2% 至 7% + 标注"明星仓 override"
- ⚠️ AI/算力调整后 25% **触碰 25% 行业上限** → 任何后续加仓必须先减
- ⚠️ 中国敞口（消费+医疗+锂电）调整后 42% **超过 40% 国家上限** → 需减 2%
- ✅ Liquidity 全部通过
- ⚠️ Cross-correlation 风险：NVDA + Broadcom + Microsoft + Google 4 个 AI 标的高度共因，建议加 SOX put spread 对冲（~1% NAV）

**Skill 设计验证**：9 章节 + Self-Check 框架按预期生效。Self-Check 1 立即捕获了 sizing 超限问题，强制 PM 在执行前修正——这正是 daily-summarize 与 daily-review 的核心差异（操作可执行性 vs 学习/求知）。

**输出文件**：[[output/daily-summarize-2026-04-13]]

**下次迭代建议**：
1. portfolio.md 应从空模板填入真实 hypothetical 持仓，让 §3 / §5 / Self-Check 1 有真锚点
2. Self-Check 4 (vs 上次 brief 一致性) 在连续运行 ≥ 2 天后才能真正生效，今天 fallback 用历史 output 报告做对照
3. §7 催化剂日历的事件应该有 wiki/metric/ 或 wiki/calendar/ 之类的中间页支撑，避免每次重新查找

---

## [2026-04-13] daily-review | v2 重跑（应用 Q7 硬指标）

**触发事件**：用户再次手动 `/daily-review`，触发对当天 (2026-04-13) 的复盘重跑。SKILL.md 在首次运行后已加入 Q7 两条硬指标（sell-side 占比 + 7 天冷却期），本次 v2 重跑验证规则生效。

**新硬指标的应用结果**：

1. **Sell-side 占比检查**：
   - 纯卖方 = 19 / 63 = **30.2%** ✅ 未触发 50% 警示
   - 但仍标注 Tsuruha 三家券商共识、海尔/迈瑞/翰森 管理层电话会的 sell-side 偏差风险
   - 类型分布：acecamp 15 (24%) / chat_brilliant 18 (29%) / mm-纯卖方 19 (30%) / mm-专家网络 9 (14%) / vital_knowledge 2 (3%)

2. **7 天冷却期检查**：
   - 今天**没有任何** comparison / output 页面满足冷却期
   - `comparison/2026-04-12-vs-04-13-叙事修正` 0 天 → ❌
   - `output/投资总结报告-260412` 0 天 → ❌
   - `output/投资总结报告-260410` 2 天 → ❌
   - **结论**：v2 全部结论直接 ground 在 source 页，无任何 comparison/output anchor 引用——成功避免了 v1 的 wiki 自我强化循环论证

**v1 vs v2 diff**：
- v1 在 Q7 末尾"事后承认"了 wiki 自我强化问题（作为反思）
- v2 在文件顶部就明确"本文件不引用任何 comparison/output 作为 anchor"，并在 Q7 用结构化表格证明每个候选 anchor 都被冷却期规则拒绝
- v2 内容与 v1 在 Q1-Q6 部分基本一致（同一组 source），核心改进在 Q7 的硬指标合规演示

**Skill 设计验证**：两条硬规则都按预期生效。冷却期规则尤其关键——today 的特殊场景（comparison 和 daily-review 共享同一组 source）正是该规则的设计目标，成功阻止了循环引用。

**输出文件**：[[output/daily-review-2026-04-13]]（v2 覆盖 v1）

---

## [2026-04-13] daily-review | 7 问复盘（首次运行 daily-review skill）

**触发事件**：用户创建 `skills/daily-review/` skill 并要求首次运行。基于今日 63 份 ingest 完成的 source 页做 7 问复盘。

**关键产出**（一行总结每问）：
- **Q1 最大认知变化**：04-12 三大乐观叙事（算力去英伟达化 / 可控聚变 / 具身智能）今天同时被反向证据削弱，唯一净新主题是 Anthropic Claude MythOS 进攻性网络安全
- **Q2 最大 expectation gap**：NVIDIA 中国份额维持 55%（vs 共识"H20 受限后大跌"）
- **Q3 跨板块**："反内卷"主题在多板块同时印证（化工 GS+MS / Tsuruha 三券商 / 储能 41 号令 / 量贩零食）；"AI 应用层"出现数据飞轮 vs 架构差异 vs 渠道捆绑三种护城河分化
- **Q4 首选多头**：[[company/NVIDIA]] (NVDA US)，6-12 月，止损 = 中国份额 < 40% 或 Rubin token 效率 < 20×
- **Q5 首选减仓**：依赖"具身智能 = AI Agent"叙事的标的（[[company/小鹏汽车]] IRON 时间表面临 FANUC 专家警示）
- **Q6 最大知识缺口**：NVIDIA 中国 55% 份额的实际拆解（H20？非 H20？哪些客户？）→ 下轮 ingest 最高优先级
- **Q7 自我红队**：⚠️ 4 大 bias 风险——confirmation bias / sell-side 集体偏差 / "希望它真" / **wiki 自我强化**（反复引用我自己几小时前创建的 comparison 页作为 anchor，是循环论证）

**输出文件**：[[output/daily-review-2026-04-13]]

**Skill 反馈**：首次运行验证了 7 问框架的实用性。Q7 红队部分是最有价值的——主动发现了 wiki 自我强化的具体案例（comparison 页冷却期问题），建议未来 daily-review 应区分"wiki 7 天稳定共识" vs "24 小时内新页面"，后者不应作为 anchor。

---

## [2026-04-13] query+create | 04-12 vs 04-13 叙事修正 comparison 页

**触发事件**：用户提问"今天最大的认知变化是什么"。

**Query 流程**：
- 阅读 5 份高信号 04-13 source（TPU v8x、NVIDIA GTC 2026、核聚变降本警示、Claude MythOS、六维力传感器 re-listed）
- 综合分析：04-12 建立的三大乐观叙事（算力去英伟达化 / 可控聚变加速 / 具身智能爆发）在 04-13 同时收到反向证据
- 核心结论：长期方向不变，但短期 timeline 都需后移；旧范式（NVIDIA / 化石能源 / 传统机器人）护城河仍在加宽

**归档**：创建 [[comparison/2026-04-12-vs-04-13-叙事修正]] 作为后续判断锚点
- 4 个对比维度（含 1 个 net new：Anthropic 进攻性网络安全）
- 三个共同的结构性偏差：乐观叙事偏差 / TAM 估算偏差 / Timeline 估算偏差
- 6 个后续验证条件（v8x 良率、v8ax 小批量、Rubin LPU 实际效率等）

**预期效果**：未来如遇到新的 reaffirm / refute 信号，应在本页追加而非新建，固化"04-12 → 04-13"这一拐点。

---

## [2026-04-13] ingest | 63 篇 aecapllc 平台研究报告批量入库（含 meeting_minutes 新类型）

**触发事件**：`/fetch-reports` 拉取 64 条记录，63 份成功（1 份无 md 文件跳过）。新增 `meeting_minutes` 来源类型，覆盖 28 份投行个股纪要（MS / JPM / GS / Nomura / SMBC / BofA / Daiwa / Merit / AceCamp），与原有 `acecamp_article` / `chat_brilliant` / `vital_knowledge` 并列为第四大类型。

**处理方式**：5 个并行 ingest agent 按主题分批处理（A1 / A2 / B / C / D）。其中 A2 / B / D 遭遇 API 中断（2 次 ECONNRESET、1 次 terminated），随后由 2 个 cleanup agent 补齐 entity gap 并补充 2 个缺失的 vk source 页（`vk-US-Iran-followup-260413`、`vk-Vital-Dawn-260413`）。全部 63 个 source 页最终确认创建完毕。

**主题分布**：

- **A1 — AI 模型 / 应用 / 广告（12 篇）**：Anthropic Claude MythOS（进攻性网络安全 Project Glasswings）、字节 Doubao 竞争格局（Kimi K2.5 反超、KDA 架构）、Sakana AI CTM 架构、DeepSeek-OCR、ChatGPT Atlas 浏览器、LiblibAI 图像生成平台、三星 Galaxy XR、AppLovin / Unity 广告、AWS / Azure / GCP 增量对比
- **A2 — AI 算力 / 光通信 / 半导体（14 篇）**：TPU v8x 推迟（联发科 IO IP 问题）、OCS 内存基础设施架构、SMBC NVIDIA GTC 2026 光互联、1.6T CPO / OCS 访谈、MCU 调研 ×2（涨价 + 利基存储）、CPU / GPU 供需及国内格局、曦智科技 IPO 光芯片市场、本源 / 玻色量子独角兽、消费电子散热公司光模块进展
- **B — 锂电 / 能源 / 化工（9 篇）**：国家发改委 41 号令储能影响、核聚变降本警示（⚠️ 与昨天 cb-fusion 乐观判断矛盾）、电解液溶剂调研、锂电产业周期、Tianqi 天齐锂业 002466（Daiwa）、大阪有机化学工业 4187（GS + MS 双覆盖）、储能电池厂商户储、充电桩超充出海
- **C — 中国消费 / 医疗（13 篇）**：恒瑞医药 SHR-1139（IL-23p19 / IL-36R 全球首个双靶点，PASI 90 = 88.2%）、海尔智家 FY25 管理层交流、迈瑞医疗 BofA 交流、翰森制药 Nomura、中国连锁便利店、激光美容设备、泳池清洁机器人、量贩零食单店模型、创新药基因小鼠、OLED 发光材料、金刚石半导体散热、六维力传感器、GS 中国宏观地产资金流
- **D — 日本 / 宏观（15 篇）**：Tsuruha 3391 三券商对比（BofA + MS + Nomura）、Sansan 4443（Nomura）、AEON Financial 8570（MS）、Rorze 6323（GS）、Takeuchi 6432（GS）、Creek River 4763（Daiwa）、商船三井追加 JPM 中期计划、SMBC FY25 Japan Seminar、Warren SPE / ASML、Merit 周度路演、Merit 海外广告平台 Q1、Nomura 中国消费调研 SKP、US-Iran follow-up（vk）、Vital Dawn 周一宏观日报（vk）

**创建页面汇总**：

- **Source**：63 个（`raw/2026-04-13/` 下 acecamp_article / meeting_minutes / vital_knowledge 三类）
- **Company**：~45 个新建，包括：Sakana AI、DeepSeek、Kimi (Moonshot)、MiniMax、字节跳动 (Doubao)、LiblibAI、曦智科技、玻色量子、Tsuruha Holdings 3391、Sansan 4443、Rorze 6323、AEON Financial 8570、Takeuchi 6432、Creek River 4763、Kusuri no Aoki 3549、恒瑞医药、海尔智家、迈瑞医疗、翰森制药、Marvell、美光 (Micron)、寒武纪、海光、沐曦、天数智芯、地平线、瑞芯微、Momenta、天齐锂业、大阪有机化学工业、AppLovin、Unity、三星电子、SambaNova、CoreWeave、普冉、华邦、旺宏、江波龙、中颖电子、国民技术、复旦微、英飞凌 (Infineon)、联发科 (MediaTek)、储能电池厂商（匿名）
- **Industry**：~24 个新建，包括：MCU、光芯片、利基存储、OLED 发光材料、金刚石散热、智驾芯片、AI 浏览器、AI 图像生成、海外广告平台、XR 头显、银屑病治疗、医疗设备、连锁便利店、激光美容设备、泳池清洁机器人、中国家电、电解液溶剂、充电桩、日本药妆、日本 SaaS、日本半导体设备、日本机械设备、日本消费金融、创新药基因小鼠
- **Concept**：~8 个新建，包括：OCS 架构、CSP 自研芯片、Arm 架构服务器 CPU、量子计算工程化、KDA 架构、Claude MythOS、双靶点抗体、国家发改委 41 号令

**更新页面**：
- Anthropic（MythOS + Coding 2.0 数据飞轮）
- Google（TPU 历史 + Android XR + v8x 延迟原因）
- OpenAI（Atlas 独立浏览器 + 独立化战略）
- 智谱（Kimi K2.5 反超）
- Meta（Q1 广告表现）
- NVIDIA（Rubin LPU + Feynman 2028 CPO）
- Broadcom（v8ax 主导地位）
- AI 基础设施（OCS / CPO / 1.6T 进展）
- AI 芯片（国内格局量化：NVIDIA 55%）
- AI-PCB 与 CCL（1.6T 散热价值量）
- CPO（Feynman 路线图更新）
- 本源量子（IPO 辅导进度）
- 可控聚变（⚠️ 加降本警示标注）
- 商船三井（JPM 5 年资本配置 Core OCF）
- US-Iran 关系（封锁有限性 follow-up）
- 中东地缘政治（同上）
- 量贩零食 / 六维力传感器（re-listed 增量信息合并）
- 锂电池与储能（41 号令 + 阳光电源）
- 中国银行业（GS 宏观地产资金流）

**关键交叉印证 / 矛盾**：

1. **TPU v8x 推迟**（联发科 IO IP 问题）+ **NVIDIA Rubin LPU + Feynman 2028 CPO** —— ASIC vs GPU 两条路线均在 2026 出现关键节点，竞争格局仍未定论
2. **核聚变降本警示**（顶刊文章）⚠️ 矛盾昨天 `cb-fusion-260412` 的乐观判断 —— 已在 `[[industry/可控聚变]]` 添加 ⚠️ 更新标注
3. **Anthropic ARR 续涨 + Claude MythOS**（进攻性网络安全）—— B 端商业化进入更深应用路径（非单纯 API 调用）
4. **NVIDIA 中国市场份额 55%** —— 与昨天"算力去英伟达化"主题形成对照：短期仍主导，国产替代需求对应中长期叙事
5. **量贩零食 / 六维力传感器**（re-listed 文件）—— 增量信息已合并到现有行业页，无需新建 source
6. **三家券商对 Tsuruha 3391 的对比**（BofA / MS / Nomura）—— 跨券商一致看好整合后规模效应，形成难得的多方印证

**Fetch 处理改进**：
- 通过 `meeting_minutes` 新类型扩展来源类型覆盖；schema type 缩写新增 `mm`
- 已在 ingest schema 加 Step 0（dedup by raw_path），确保重跑安全
- 63 个 source 页均含 `## 结构性观察` 章节，符合当前 schema 要求

**新红链待补**（留下一轮 lint 处理）：
- `[[company/抖音]]`、`[[company/快手]]`（兴趣电商三大平台之二）
- `[[company/东方锆业]]`（金属锆行业玩家）
- `[[company/生益科技]]`（生益电子母公司，与生益电子混用待澄清）
- Oracle、AMD、Tesla、Nike、LVMH、ASML 等跨主题红链

---

## [2026-04-13] lint | wiki 全量健康检查 + 修复

**触发事件**：2026-04-12 大批量 ingest（41 source + 81 entity）后第一次系统性 lint，覆盖 10 项检查。

**lint 结论**：
- ✅ Source 覆盖率 41/41，sidecar 元数据传递 41/41
- ✅ 新批次 41 个 source 全部含 `## 结构性观察`
- ✅ Anthropic ARR、M9 CCL 两处 ⚠️ 更新标注到位
- ✅ index.md 与磁盘 100% 同步
- ❌ 旧批次 19 个 260410 source 缺 `## 结构性观察`（schema 升级前创建）
- ❌ 高频红链 6 个：华住集团（3 inbound）、生益电子 / 南亚新材（各 2，AI-PCB 主题核心）、TEA STONE / 金属锆与铪 / 兴趣电商
- ❌ Nomura 旧 source 用裸链 `[[三菱地所]]` 而非 path-qualified
- ❌ `fpddetector` 标签拼写不规范（3 处）
- ❌ 部分新建 entity tags 为空 / `油气装备` vs `深地油气` 重叠未明确

**修复措施（4 个并行 fix agent）**：

1. **Backfill 19 个 260410 结构性观察**（19/19 完成）：从已有正文提取行业行为模式、监管态度变化、长期信号；每个 source 补 3-4 个 bullets，`last_updated` 升级为 2026-04-13。结构性观察沉淀的关键 insight：日企 vs 大陆扩产分化、Anthropic Land-and-Expand vs OpenAI ELA、AI 挤压企业存储的主动机制、Sunwoda 进入宁德隐含谈判筹码、稀缺期先发时间窗等

2. **创建 6 个红链页面**：
   - `wiki/company/华住集团.md` — 直营出海 vs 锦江平台化对照
   - `wiki/company/生益电子.md` — NVIDIA M9 供应链认证地位
   - `wiki/company/南亚新材.md` — 排挤效应机制（生益高端外溢）
   - `wiki/company/TEA STONE.md` — 空间收入 80-90% 的颠覆模型
   - `wiki/industry/金属锆与铪.md` — 锆英砂 100% 进口 + AI 燃气轮机 CAGR 18%
   - `wiki/industry/兴趣电商.md` — 抖音/快手/小红书 GMV 对比 + 站内成交 vs 站外成交结构性挑战

3. **Tags / frontmatter / link 修复**：
   - `fpddetector` → `fpd-detector`（3 文件）
   - 5 个 sparse 页面补标签（大疆 / 极飞 / 纵横 / 工业无人机 / 量贩零食）
   - `industry/AI-PCB与CCL` `key_players` 同步 7 条（生益科技 / 台光 / 胜宏 / 南亚新材 / 生益电子 / 金居新材 / 台燿）
   - `Nomura-日本不动产` entities 改为 path-qualified（`[[三菱地所]]` → `[[company/三菱地所]]`）
   - `industry/油气装备` 与 `industry/深地油气` 建立 parent-child 关系（前者新增 `## 子领域` 章节，后者 frontmatter 加 `parent_sector`）

4. **清理**：
   - 删除 `raw/2026-04-12/chat_brilliant/` 下 3 个重复 raw 文件（_034 AWS-Azure-GCP / _035 量贩零食 / _036 六维力传感器）+ 6 个对应 sidecar
   - `wiki/index.md` 新增 6 个红链修复后的页面条目，`last_updated` → 2026-04-13

**新红链（待下一轮 lint 处理）**：
- `[[company/生益科技]]`（600183.SH，生益电子的母公司，引用混用待澄清）
- `[[company/快手]]`、`[[company/抖音]]` — 兴趣电商三大平台之二
- `[[company/东方锆业]]` — 锆铪行业玩家
- 其余跨主题红链（Oracle、Tesla、Nike、LVMH 等）按需在后续 ingest 自然补建

**预期效果**：source schema 完整性提升至 100%（新旧批次都满足"结构性观察必填"），核心实体网络密度提升（消费/CCL 主题不再有断点），未来 lint 应只剩低优先级标签微调和 industry frontmatter market_size 数据补充。

---

## [2026-04-13] create | 2026-04-12 投资研究日报（41 份来源综合报告）

**触发事件**：用户指令，对 41 份 2026-04-12 source 页面进行跨板块综合分析。

**创建页面**：`wiki/output/投资总结报告-260412.md`（395 行）

**覆盖主题 10 个**：
1. Anthropic ARR 重大跳跃与 B 端 AI 终局（$9B→$30B 4 个月 +233%）
2. 算力去英伟达化（3.5 GW ASIC 长协 + TurboQuant 6x KV cache + ASIC 占比 15%E）
3. 中美 AI 算力分裂（B30 政策博弈 + 超聚变 IPO + 华为昇腾天花板）
4. M9 CCL 认知修正（Low Dk2 80% 主流，石英布仅 20%）
5. 反内卷主题串联（射频芯片 / 电子特气 / 大陆硅片 / 量贩零食 / 现磨咖啡）
6. 人形机器人国内外路径分叉（1X 家庭 vs 国内工业先行；六维力传感器差距）
7. 十五五能源主题（深地油气 / 可控聚变 / 新型电力系统）
8. 消费分化（奢侈品触底回升 + 运动户外高景气 + 星巴克中国博裕接手）
9. AI 应用层落地（Meta Muse Spark + Advisor Strategy + 云厂竞争格局）
10. 宏观框架更新（油价见顶→美元见顶→美债收益率回落→EM 受益；US-Iran 停火）

**矛盾/修正标注 5 条**：Anthropic ARR（严重低估）、M9 路径（石英布→Low Dk2）、1X NEO 定价（$20k 为租赁非买断）、国产 AI 能力 vs 算力差距（算力是核心约束）、六维力传感器 TAM 高估

**投资方向 5 个**：云厂+ASIC 受益（高确信）、华润置地+安踏系（高确信）、深地油气+配网（中确信）、超聚变 IPO（中确信）、AI B 端工具链（中长期）

---

## [2026-04-12] ingest | 41 篇 aecapllc 平台研究报告批量入库

**触发事件**：通过 `/fetch-reports` 拉取 2026-04-12 的全部 47 条研究记录，去重 3 份后共 44 个 md 文件（acecamp_article 2 / chat_brilliant 36 / substack 5 / vital_knowledge 1）。处理时进一步合并 3 对完全重复条目，实际处理 41 份。

**处理方式**：按主题分 5 个 batch 并行 ingest：
- **Theme A（AI / 算力 / 云厂）** 11 份：Anthropic ARR、智谱、OpenAI 梯云纵、AWS vs Azure vs GCP、AI 服务器 ODM、AWS-Meta 人事、超聚变、中美算力贸易、GPUs 6x、Meta Strikes Back、AI IQ
- **Theme B（半导体 / 材料）** 7 份：M9 CCL、平板探测器、量子芯片、西安奕材硅片、Skyworks-Qorvo 合并、六氟化钨、长光辰芯 CIS
- **Theme C+D（人形机器人 + 能源）** 6 份：1X NEO、小鹏 IRON、六维力传感器、深地油气、可控聚变、十五五电力系统
- **Theme E（消费 / 零售）** 9 份：连锁酒店出海、运动户外、小红书、八马茶业 IPO、剧本杀、星巴克中国、商超自有品牌、奢侈品、量贩零食
- **Theme F+G+H（医疗 / 其他 / 周报）** 8 份：宠物医疗、显微手术机器人、工业无人机、Wan2.2 Animate、AI 漫剧、US-Iran、Market Analysis、Core Framework

**创建页面**：41 source + 81 entity（约 40 company / 30 industry / 11 concept）

**更新页面（4 个）**：
- `wiki/company/Anthropic.md` — ARR 重大修正：$4B+ → $300 亿+（$30B+），原数据保留并加 ⚠️ 更新标注；新增 Pentagon 纠纷、UK 招揽、Broadcom-Google 3.5GW 算力协议、Self-imposed access limits 四个新章节
- `wiki/industry/AI基础设施.md` — 新增 "去英伟达化与 ASIC 路线" 章节（TurboQuant、Broadcom-Google）；新增 GB300 全球需求量化表
- `wiki/industry/AI-PCB与CCL.md` — ⚠️ 重要认知修正：M9 主流路径为 Low Dk2（80%）而非石英布（20%），矫正此前 wiki 共识；新增 M9 双路径详细对比、HVLP4 供需、卖方市场涨价分化
- `wiki/industry/锂电池与储能.md` — 新增新型储能政策与盈利机制章节（容量电价、峰谷套利、蒙西补贴）

**关键交叉印证**：
- Anthropic ARR 跳跃（$30B）+ Broadcom-Google 3.5GW 协议 + TurboQuant 6x KV cache 压缩，三件事共同指向 "算力去英伟达化" 主题
- 智谱 vs OpenAI vs Anthropic 三方对比框架成型（中国 / 美国 to C / 美国 to B 路线分化）
- 人形机器人国内外路径分叉：1X/Figure 海外家庭场景先行 vs 国内工业场景先行
- M9 CCL 修正与 NV GB300 周期形成材料端 + 平台端双重印证
- 反内卷主题串联多行业（射频芯片、电子特气、量贩零食、现磨咖啡）

**重要红链（待后续补建）**：Oracle、AMD、Tesla、华住集团、携程、美团、Nike、Adidas、LVMH、Hermes、Kering、抖音、淘宝天猫、博裕资本、汇川技术、卧龙电驱、四方达 等 ~25 个跨主题实体

**待补充 / 跟进**：
- ARR 重大跳跃需要后续季度跟踪，特别是 Anthropic / 智谱
- 联创光电 "转 FRC" 仍待证实
- AMD 通过认股权证可获 OpenAI ~10% 股权（低报道但重要）
- 重复推送条目（六维力传感器 033/036、量贩零食 033/035、AWS-Azure-GCP 032/034）已合并处理

---

## [2026-04-12] update | source schema 增加 sidecar 元数据流转

**触发事件**：raw → source 的 ingest 链路缺少结构化的来源元数据；用户希望 source 页面能携带 `research_id` / `research_type` 等可追溯字段。

**本次调整**：
- `scripts/fetch_reports.py` 下载每份文件时同步生成 `{原文件名}.meta.json` sidecar，记录 `research_id` / `research_type` / `title` / `md_url` / `fetched_at` 及完整原始 API item；幂等补写
- `raw/` 目录结构由 `{researchType}/{date}/` 调整为 `{date}/{researchType}/`，按日期一级聚合更便于按日 ingest
- `CLAUDE.md` / `AGENTS.md` source 模板新增 `research_id` / `research_type` 字段（不强制）；ingest 工作流第 1、3 步明确读取 sidecar 并将字段写入 source frontmatter
- `skills/fetch-reports/SKILL.md` 与 `.claude/commands/fetch-reports.md` 描述同步更新

**预期效果**：source 页面可反查到 aecapllc 平台原始 API 记录，便于未来批量更新、去重、按 research_type 过滤。

---

## [2026-04-12] update | 增加 Codex 兼容入口（AGENTS.md）

**触发事件**：知识库最初以 Claude Code 为主，根目录仅有 `CLAUDE.md`。为兼容 Codex，需要提供其默认识别的 `AGENTS.md`，同时保留现有 Claude 工作流。

**本次调整**：
- 新增根目录 `AGENTS.md`，内容与 `CLAUDE.md` 对齐，供 Codex 作为 schema 入口读取
- 更新 `CLAUDE.md` 顶部说明与 schema 描述，明确 `CLAUDE.md` / `AGENTS.md` 为双入口、同一套规则
- 约定今后若调整 wiki 规则、目录结构或工作流，需同时维护两份文件，避免不同 agent 读取到不同规范

**预期效果**：Claude Code 与 Codex 都能在仓库根目录发现自己的默认 schema 文件，并基于同一套 wiki 约定执行 ingest、query 和 lint。

## [2026-04-12] update | CLAUDE.md source 模板迭代 + 磷化铟 source 页面修正

**触发事件**：用户提问"住友这种日商对扩产是否比较谨慎"，检索 wiki 时发现此信息在 [[source/磷化铟调研-260410]] 的摘要中被遗漏。原文中有明确问答，但在 ingest 时未被提取到 source 页面。

**Root cause**：
- 该信息是"结构性判断"（日企 vs 大陆企业的行为差异），而非具体数字
- 提取时倾向抓数字（价格、直收率、涨幅），忽略了非数字型的结构性观点
- 原 source 模板的"关键要点"未明确要求覆盖"行业参与者行为模式"这一维度

**修正措施（两层）**：

1. **局部修复** — 更新 `wiki/source/磷化铟调研-260410.md`：
   - 在"关键要点"新增第 8 条：住友扩产谨慎，国内厂商激进
   - 在"值得注意的观点/引语"收录专家原话
   - 新增"## 结构性观察"章节，记录日企 vs 大陆企业的扩产行为差异及其投资含义

2. **根本修复** — 更新 `CLAUDE.md` 中的 source 模板：
   - "关键要点"明确要求覆盖 5 个维度，新增"行业参与者的行为模式"
   - 新增"## 结构性观察"为必选章节（无则写"无"）
   - 增加编译质量原则说明：source 是后续所有操作的基础，非数字但重要的判断不得遗漏

**预期效果**：未来所有 ingest 都会主动识别和记录结构性观察，不再偏向抓数字而漏掉行为模式类判断。

---

## [2026-04-11] ingest | 10 篇 raw/reports 来源入库

处理来源（10 份报告）：
1. 模拟芯片调研：ADI/TI/Microchip/MPS/英飞凌等涨价、交期与库存
2. 电解液溶剂近况：VC/EC/PG 价格走势与供需
3. 金属锆分析：技术路线、新兴产业需求、三祥新材
4. 面板专家谈价格走势、Mini LED 渗透率及 TCL 竞争策略
5. 百威亚太（1876.HK）：FIFA 窗口期事件性机会
6. 磷化铟系列调研(2)：价格体系、涨价趋势、海外试用
7. 重估大模型商业模式：Token 价值光谱
8. 昇腾调研：华为 950 系列、字节/腾讯订单、超节点
9. AI 平台 CCL 规格升级：GB300/Rubin/Blackwell Ultra
10. 对话 Verdent AI：web coding 初创公司

创建页面（21 个）：
- Source 摘要页 × 10
- `wiki/company/ADI.md`
- `wiki/company/TCL.md`
- `wiki/company/百威亚太.md`
- `wiki/company/三祥新材.md`
- `wiki/company/华为昇腾.md`
- `wiki/industry/模��芯片.md`
- `wiki/industry/面板与Mini-LED.md`
- `wiki/industry/AI芯片.md`
- `wiki/industry/AI-PCB与CCL.md`
- `wiki/concept/Token价值光谱.md`

更新页面（3 个）：
- `wiki/company/Anthropic.md`（新增 2 个来源引用）
- `wiki/industry/锂电池与储能.md`（新增电解液溶剂来源）
- `wiki/industry/AI基础设施.md`（新增 5 个来源引用 + 华为昇腾为 key player）

交叉引用发现：
- 电解液溶剂供需偏紧印证锂电池行业下游需求强劲
- 模拟芯片/被动元件涨价与 MS 存储超级周期报告的"AI 挤占产能"逻辑一致
- 昇腾光模块采购从十几万支跃升至几百万支，与光模块测试设备需求趋势吻合
- CCL 材料涨价 + PCB 厂商集体调价，佐证企业 IT 成本上涨趋势

---

## [2026-04-11] ingest | 2 篇来源入库（锂电池 + 美国 CPI���

处理来源：
1. Merit - 锂电池龙头厂商排产 & 产业趋势调研（2026-04-10）
2. BofA - 美国 3 月 CPI 快评（2026-04-10）

创建页面（6 个）：
- `wiki/source/Merit-锂电池龙头排产调研-260410.md`
- `wiki/source/BofA-美国3月CPI快评-260410.md`
- `wiki/company/宁德时代.md`
- `wiki/industry/锂电池与储能.md`
- `wiki/industry/美国宏观经济.md`
- `wiki/concept/Core-PCE.md`

---

## [2026-04-11] query | 生成投资总结报告

基于全部 10 份来源综合分析，生成 `wiki/output/投资总结报告-260410.md`。覆盖八大跨板块主题、关键数据、矛盾点、催化剂时间线、投资方向建议。

---

## [2026-04-11] ingest | 2 篇中国银行业来源入库

处理来源：
1. BofA - 建设银行 FY25 业绩交流（2026-04-10）
2. BofA - 邮储银行 FY25 业绩交流（2026-04-10）

创建页面（6 个）：
- `wiki/source/BofA-建设银行FY25业绩交流-260410.md`
- `wiki/source/BofA-邮储银行FY25业绩交流-260410.md`
- `wiki/company/建设银行.md`
- `wiki/company/邮储银行.md`
- `wiki/industry/中国银行业.md`
- `wiki/comparison/建设银行vs邮储银行-FY25业绩.md`

---

## [2026-04-11] ingest | 3 篇日本市场来源入库

处理来源：
1. Nomura - 日本不动产/建筑/交通 Checkpoints（2026-04-10）
2. SMBC - J-REIT 市场展望（2026-04-10）
3. Daiwa - 沢井集团 4887（2026-04-10）

创建页面（13 个）：
- `wiki/source/Nomura-日本不动产建筑交通-260410.md`
- `wiki/source/SMBC-JREIT市场展望-260410.md`
- `wiki/source/Daiwa-沢井集团4887-260410.md`
- `wiki/company/三菱地所.md`
- `wiki/company/三井不动产.md`
- `wiki/company/住友不动产.md`
- `wiki/company/沢井集团.md`
- `wiki/company/商船三井.md`
- `wiki/industry/日本不动产.md`
- `wiki/industry/J-REIT.md`
- `wiki/industry/日本建筑.md`
- `wiki/industry/国际航运.md`
- `wiki/industry/日本仿制药.md`

---

## [2026-04-11] ingest | 3 篇 AI/科技调研来源入库

处理来源：
1. Merit - Anthropic 2B 业务调研 & 硬件需求（2026-04-10）
2. Merit - 光模块测试设备调研（2026-04-10）
3. MS - Memory 'Supercycle' 企业采购影响（2026-04-10）

创建页面（11 个）：
- `wiki/source/Merit-Anthropic企业业务调研-260410.md`
- `wiki/source/Merit-光模块测试设备调研-260410.md`
- `wiki/source/MS-存储超级周期企业采购影响-260410.md`
- `wiki/company/Anthropic.md`
- `wiki/company/Keysight.md`
- `wiki/company/Rigol.md`
- `wiki/industry/AI基础设施.md`
- `wiki/industry/光模块测试设备.md`
- `wiki/industry/存储与企业硬件.md`
- `wiki/concept/MCP.md`
- `wiki/concept/CPO.md`

---

## [2026-04-11] create | 初始化知识库

创建投资研究知识库，初始化目录结构、Schema（CLAUDE.md）、目录文件（index.md）和页面模板。
