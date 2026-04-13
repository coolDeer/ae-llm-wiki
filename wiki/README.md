# LLM Wiki 投资研究知识库 — 构建流程与逻辑

> 本文件是 wiki 的架构与流程说明，面向人类阅读。
> Schema 定义（模板、约定、工作流的细节）见根目录 `CLAUDE.md` / `AGENTS.md`。
> 操作日志见 [[log]]，总目录见 [[index]]。

---

## 一、整体架构

```
┌─────────────────────────────────────────────────────────┐
│  人 (你)：提供素材、提问、指导分析方向                  │
│  LLM：所有读写、归档、维护                              │
└─────────────────────────────────────────────────────────┘
                            ↓
┌──────────┬──────────────────────┬───────────────────────┐
│ 第 1 层  │  raw/  (LLM 只读)    │ source of truth       │
│ 原始素材 │  ├─ {YYYY-MM-DD}/    │ 不可变，来源可追溯    │
│          │  │  └─ {researchType}│ md / pdf / docx 均可  │
│          │  │     ├─ *.md       │                       │
│          │  │     └─ *.meta.json│ ← sidecar 元数据      │
└──────────┴──────────────────────┴───────────────────────┘
                            ↓
┌──────────┬──────────────────────┬───────────────────────┐
│ 第 2 层  │  wiki/ (LLM 读写)    │ 8 种结构化 entity     │
│ 知识层   │  ├─ index.md         │ 总目录                │
│          │  ├─ log.md           │ 操作日志              │
│          │  ├─ company/         │ 公司档案              │
│          │  ├─ person/          │ 人物档案              │
│          │  ├─ industry/        │ 行业 / 板块           │
│          │  ├─ thesis/          │ 投资论点              │
│          │  ├─ source/          │ 来源摘要              │
│          │  ├─ comparison/      │ 对比 / 框架           │
│          │  ├─ metric/          │ 关键指标追踪          │
│          │  ├─ concept/         │ 概念术语              │
│          │  └─ output/          │ 分析输出 (slides/reports) │
└──────────┴──────────────────────┴───────────────────────┘
                            ↓
┌──────────┬──────────────────────┬───────────────────────┐
│ 第 3 层  │  CLAUDE.md /AGENTS.md│ Schema：所有规则在此  │
│ Schema   │  (双入口，内容一致)   │ 模板 / 工作流 / 约定  │
│          │  scripts/, skills/   │ 工具链 + slash command│
└──────────┴──────────────────────┴───────────────────────┘
```

**核心思想**：raw 是事实底座，wiki 是结构化解读层，Schema 定义如何在两者之间映射。Schema 是 LLM 的"宪法"——每个 ingest agent 启动时第一件事就是读 `CLAUDE.md`。

---

## 二、数据采集层 (`raw/`)

### 2.1 fetch_reports.py

- 入口：`/fetch-reports [日期]`（slash command → skill → script）
- API：`GET https://api.aecapllc.com/.../research/daily/list?date=...`
- 行为：
  - 遍历 `data[]`，按 `mdReportUrl` 是否非空决定下载 / 跳过
  - 路径：`raw/{date}/{researchType}/{原始文件名}.md`
  - **幂等**：`target.exists()` 跳过重复下载
  - 自动 **URL 百分号编码**（处理 S3 路径里的中文、空格、特殊符号）
- 仅依赖 Python 标准库，无外部依赖

### 2.2 Sidecar 元数据

每份下载文件同目录写一份 `{原文件名}.meta.json`：

```json
{
  "research_id": "69db1f53...",
  "research_type": "acecamp_article",
  "title": "...",
  "md_url": "...",
  "fetched_at": "2026-04-12T22:43:13+08:00",
  "raw": { /* 完整原始 API item */ }
}
```

- 解决 PDF 等二进制格式无法注入 frontmatter 的问题
- ingest 时被 source 页 frontmatter 引用（`research_id` / `research_type` 字段）
- 缺失会自动补写（也是幂等的）

---

## 三、Schema 定义层 (`CLAUDE.md` / `AGENTS.md`)

### 3.1 8 种页面类型 + frontmatter 模板

| 类型 | 目录 | 关键 frontmatter |
|---|---|---|
| company | `wiki/company/` | name, ticker, sector, market_cap, key_people, sources, confidence |
| person | `wiki/person/` | name, role, affiliation, category |
| industry | `wiki/industry/` | name, parent_sector, market_size, growth_rate, key_players |
| thesis | `wiki/thesis/` | title, target, direction, conviction, status, date_opened |
| source | `wiki/source/` | title, source_type, date, raw_path, **research_id**, **research_type**, entities, quality |
| comparison | `wiki/comparison/` | title, entities, framework |
| metric | `wiki/metric/` | title, entity, frequency |
| concept | `wiki/concept/` | name, aliases, category |

每种类型有**固定的正文章节模板**——例如 source 页**必须**包含 `## 关键要点`（覆盖 5 维度）+ `## 结构性观察`（必填，没有则写"无"）。

### 3.2 命名 / 链接 / 标签 / 引用约定

- **文件名**：中文为主，空格用 `-`，禁止 `/ \ : * ? " < > |`
- **wiki link**：Obsidian 格式 `[[页面名]]` 或 `[[company/腾讯|腾讯]]`，跨目录用路径前缀
- **标签**：YAML list，小写英文，多词用 `-`（如 `ai-chip`, `china`）
- **引用**：所有事实陈述 → `（来源：[[source/页名]]）`
- **矛盾处理**：不删除旧信息，加 `⚠️ 更新（YYYY-MM-DD）：...（来源：[[source/...]]）`

---

## 四、四大工作流

### 4.1 Ingest（处理新素材）

```
0. 去重检查 (必做)
   └─ grep wiki/source/*.md 中 raw_path 字段
      └─ 命中 → ⊝ 跳过；未命中 → 继续

1. 阅读来源
   ├─ Read raw/...md (或 pdf/docx)
   └─ Read 同目录 {原文件名}.meta.json sidecar
      └─ 提取 research_id / research_type / title / fetched_at

2. 与用户讨论 (可跳过 if 用户已批量授权)
   └─ 列出关键要点，确认重点

3. 创建 source 页
   ├─ 文件名：{type-short}-{topic}-{date}.md
   ├─ frontmatter 含 raw_path + research_id + research_type
   └─ 正文：5 维度关键要点 + ## 结构性观察 (必填)

4. 更新 / 创建实体页
   ├─ 已有 → update (追加新数据 + ⚠️ 矛盾标注)
   └─ 没有 → create (按模板)

5. 更新行业 / 概念页 (若涉及)
6. 更新 active thesis (若相关)
7. 更新 wiki/index.md
8. 追加 wiki/log.md
9. 总结 (告知用户做了什么)
```

**幂等性**保证：步骤 0（dedup by raw_path）+ entity 页 "已存在则更新"。

### 4.2 Query（回答问题）

```
1. 读 index.md → 定位相关页
2. 读相关页 → 综合
3. 回答 + 引用 source
4. 判断是否归档 → 创建 comparison/output 页
5. 识别知识缺口 → 告诉用户
```

### 4.3 Lint（健康检查）

10 项检查：

1. Source 覆盖率（raw 文件 vs source 页 raw_path）
2. Sidecar 元数据传递率
3. `## 结构性观察` 必填章节
4. 红链统计（被引用但未创建的页面）
5. 孤立页面（无入站链接）
6. 标签一致性
7. 跨页矛盾
8. Frontmatter 完整性
9. 链接完整性
10. index.md 与磁盘同步

输出报告 → 用户决定是否修复 → 修复结果追加 log.md。

### 4.4 Synthesis（投资总结报告）

```
读 N 份 source → 提取跨主题模式 → 写 wiki/output/投资总结-{date}.md
```

固定结构：摘要 / 跨板块主题 / 数据速查 / 矛盾与修正 / 催化剂时间线 / 投资方向 / 待跟进。

---

## 五、关键设计决策

| 决策 | 理由 |
|---|---|
| **Raw 不可变** | 一切信息可追溯到 source of truth；ingest 只是"解读"，不修改原文 |
| **Sidecar 而非 frontmatter** | 兼容 PDF / docx 等二进制；不污染原文件；统一处理路径 |
| **Source 页是基础**，实体页面引用它而不直接从 raw 提取 | 避免重复读 raw（节省 context），所有"二次解读"集中在 source 页 |
| **结构性观察必填** | 防止 LLM 过度偏向抓数字而漏掉行为模式类判断（这些往往才是判断拐点的关键）|
| **矛盾保留** | 知识演进可见；旧数据是"历史快照"，删除会丢失时间维度 |
| **Wiki link 强制** | 让知识图谱可视化（Obsidian Graph View）+ 防止孤岛 |
| **中文为主，专业术语英文** | 投资研究的术语精度需要英文 (P/E, EBITDA, ARR, ASIC...)，但叙述用中文降低认知成本 |
| **Confidence 标注** | 不确定信息明确标 `low`，避免被当成 ground truth |
| **去重检查 step 0** | 让 ingest 流程幂等，重跑安全，多 agent 并行不冲突 |

---

## 六、多 Agent 并行模式（实际工程）

### 6.1 何时分批

- 单个 ingest 任务 < 5 文件 → 主线程直接做
- 5-15 文件 → 单个 agent
- 15+ 文件 → **按主题分批 + 并行 agent**

### 6.2 分批原则

- 主题边界清晰（AI / 半导体 / 消费 / 日本 / 宏观 ...）
- 实体重叠最小化（避免 race condition）
- 每批 8-15 文件（Sonnet 模型上下文窗口 + tool budget 适中）

### 6.3 Agent prompt 模板

每个 agent prompt 必须包含：

1. 项目根路径（绝对）
2. **明确指令"先读 CLAUDE.md"**
3. 文件清单（绝对路径）
4. 主题范围（让 agent 知道哪些 entity 是 "我的"，哪些是 cross-theme red link）
5. 已有实体清单提示（"check existing first"）
6. 输出格式（结构化 markdown 报告）
7. 不许动 index.md / log.md（主线程合并）

### 6.4 失败恢复

- API 中断 → 已创建的文件不会回滚（增量友好）
- 重试用 cleanup agent，**不重做** source 阶段（dedup 跳过），只补 entity gap
- index / log 由主线程或专门的 merge agent 最后一次性合并

---

## 七、工具链

| 工具 | 用途 |
|---|---|
| `scripts/fetch_reports.py` | 从 aecapllc 拉取每日报告 + 写 sidecar |
| `skills/fetch-reports/SKILL.md` | Skill 入口 |
| `.claude/commands/fetch-reports.md` | Slash command 入口 (`/fetch-reports`) |
| `CLAUDE.md` / `AGENTS.md` | Schema 双入口（Claude Code + Codex）|
| Obsidian (推荐) | 可视化 + Graph View + Dataview 查询 |
| Marp | 导出 slides (`wiki/output/slides/`) |

---

## 八、典型一天的循环

```
早上
└─ /fetch-reports                    ← 拉取昨日 / 今日素材
   └─ 平台未渲染 → 等几小时再跑
      └─ 增量补齐 (download 幂等)

中午
└─ ingest (按主题分 N 个并行 agent)
   ├─ 每个 agent 创建 source + entity
   └─ 失败 → cleanup agent 补 gap

下午
├─ /lint  ← 健康检查
│  └─ 修复高优先级问题 (backfill / 红链 / 标签)
└─ 生成投资总结 wiki/output/投资总结-{date}.md

晚间
└─ /query "今天最大的认知变化是什么"
   └─ 综合 wiki 内容，必要时归档为 comparison
```

---

## 九、可演进方向

1. **Cross-link agent**：ingest 完成后扫今天的 source 页，主动填充 "## 与现有知识的关系" 章节（与历史 source / entity 建立交叉引用）
2. **Schema 加 step 0.5**："读 wiki/index.md 形成 mental map" —— 成本低（一次 Read），关联性显著提升
3. **Daily digest 模板**：用 `wiki/output/daily-{date}.md` 自动化生成投资总结，把昨天 → 今天的 delta 写进去
4. **Thesis 页面体系**：从 source 中提炼"已成型的投资论点"（如"算力去英伟达化"、"反内卷主题串联"）作为 active thesis 跟踪
5. **Lint 自动化**：把 lint 列入 daily cron，结果通过 hook 通知，不需要手动触发
6. **Person 页面**：从 transcripts 中提取专家观点的源头人物（基金经理、行业专家），形成"人物-观点-时间"轴
