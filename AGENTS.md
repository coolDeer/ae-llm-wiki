# LLM Wiki 投资研究知识库 — Schema

> 本文件供 Codex 使用，内容与 `CLAUDE.md` 保持同步。
> 若调整 wiki 规则、目录结构或工作流，需同时更新 `AGENTS.md` 与 `CLAUDE.md`。

## 概述

本知识库是一个面向投资研究的 LLM Wiki，用于系统性地整理和维护投资访谈记录、研报、分析报告等素材。LLM 负责所有编辑工作：摘要、交叉引用、归档、维护；用户负责提供素材、提出问题、指导分析方向。

正文语言：中文为主，专业术语（P/E、EBITDA、TAM、ROIC 等）保留英文。

---

## 架构

### 三层结构

| 层 | 目录 | 权限 | 说明 |
| --- | --- | --- | --- |
| 原始素材 | `raw/` | LLM 只读 | 不可变的来源文档，是一切信息的 source of truth |
| Wiki | `wiki/` | LLM 读写 | 结构化 markdown 页面，LLM 创建并维护 |
| Schema | `AGENTS.md` / `CLAUDE.md` | 人 + LLM 共同维护 | 定义 wiki 运作规则，两份文件应保持一致 |

### 目录结构

```text
raw/
└── {YYYY-MM-DD}/                      # 一级目录：拉取/收录日期
    └── {researchType}/                #   二级目录：来源类型（acecamp_article / chat_brilliant / substack / vital_knowledge / report / transcript / filing / article / data ...）
        ├── {原始文件名}.md            #     原始文件（md / pdf / docx / csv ...）
        └── {原始文件名}.md.meta.json  #     sidecar 元数据（research_id / research_type / title / md_url / fetched_at / 完整 raw item）

wiki/
├── index.md         # 总目录（LLM 每次 ingest 后更新）
├── log.md           # 操作日志（仅追加）
├── company/         # 公司档案
├── person/          # 人物档案
├── industry/        # 行业/板块
├── thesis/          # 投资论点
├── source/          # 来源摘要
├── comparison/      # 对比/框架分析
├── metric/          # 关键指标追踪
├── concept/         # 概念术语
└── output/          # 分析输出
    ├── slides/      #   Marp 幻灯片
    └── charts/      #   图表
```

---

## 页面类型与模板

### 1. 公司档案 (Company) — `wiki/company/{公司名}.md`

```yaml
---
type: company
name: 公司全称
ticker: ""          # 交易代码，如 AAPL、600519.SH
exchange: ""        # 交易所
sector: ""          # 所属行业
sub_sector: ""      # 细分行业
market_cap: ""      # 最新市值（含币种和日期）
founded: ""         # 成立年份
hq: ""              # 总部
key_people: []      # 关键人物 wiki link
tags: []
sources: []         # 引用的 source 页面
last_updated: ""
confidence: medium  # high / medium / low
---
```

**正文结构：**
- `## 公司概况`
- `## 商业模式`
- `## 财务摘要` → `### 收入结构` / `### 关键财务指标`（表格：指标 | 最近年度 | 前一年度 | 同比变化）
- `## 竞争格局`
- `## 估值`
- `## 风险因素`
- `## 催化剂`
- `## 关键时间线`
- `## 相关页面`
- `## 引用来源`

### 2. 人物档案 (Person) — `wiki/person/{人名}.md`

```yaml
---
type: person
name: 全名
role: ""            # 当前职位
affiliation: ""     # 所属机构 wiki link
category: ""        # executive | fund_manager | analyst | founder | board_member | other
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 基本信息`
- `## 投资理念 / 管理风格`
- `## 关键观点与语录`（附来源和日期）
- `## 业绩记录`
- `## 相关页面`
- `## 引用来源`

### 3. 行业/板块 (Industry) — `wiki/industry/{行业名}.md`

```yaml
---
type: industry
name: 行业名称
parent_sector: ""   # 上级板块
market_size: ""     # 市场规模估算
growth_rate: ""     # 增速
key_players: []     # 主要公司 wiki link
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 行业概况`
- `## 市场规模与增长`
- `## 产业链分析`
- `## 竞争格局`
- `## 关键趋势`
- `## 监管环境`
- `## 投资机会与风险`
- `## 相关公司`
- `## 相关页面`
- `## 引用来源`

### 4. 投资论点 (Thesis) — `wiki/thesis/{标题}.md`

```yaml
---
type: thesis
title: 论点标题
target: ""          # 标的 wiki link
direction: ""       # long | short | neutral
conviction: medium  # high | medium | low
status: active      # active | monitoring | closed
date_opened: ""
date_closed: ""
price_at_open: ""
price_at_close: ""
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 核心论点`（一句话总结）
- `## Bull Case`
- `## Bear Case`
- `## 关键假设`
- `## 验证 / 证伪条件`（表格：条件 | 状态 | 最新证据）
- `## 催化剂时间线`
- `## 风险管理`
- `## 持仓逻辑演进`（每次更新记录变化和理由）
- `## 相关页面`
- `## 引用来源`

### 5. 来源摘要 (Source) — `wiki/source/{来源标题}.md`

```yaml
---
type: source
title: 来源标题
source_type: ""     # transcript | report | filing | article | podcast | book | data
author: ""          # 作者/来源机构
date: ""            # YYYY-MM-DD
raw_path: ""        # 指向 raw/ 中原始文件的相对路径
research_id: ""     # 来自 sidecar {raw_path}.meta.json 的 research_id（如有）
research_type: ""   # 来自 sidecar 的 research_type（如 acecamp_article / chat_brilliant / substack ...）
entities: []        # 提及的实体 wiki link
quality: medium     # high | medium | low
tags: []
last_updated: ""
---
```

> **关于 sidecar 元数据**：通过 `scripts/fetch_reports.py` 下载的文件，会在同目录写一个 `{原文件名}.meta.json` 旁路文件，记录 API 返回的 `research_id` / `research_type` / `title` / `md_url` / `fetched_at` 以及完整原始 item。ingest 时先读 sidecar（不存在则留空），把 `research_id` / `research_type` 填入 source 页 frontmatter。sidecar 文件本身不需要 ingest，也不应纳入 wiki 链接。

**正文结构：**
- `## 来源概要`
- `## 关键要点`（编号列表，**必须覆盖以下维度**）：
  1. 核心数据和变化（价格、产能、增速等定量信息）
  2. 关键判断与观点（即使没有具体数字）
  3. **行业参与者的行为模式**（如“日企 vs 大陆企业扩产差异”、“大厂 vs 创业公司决策速度”这类结构性观察容易被忽略，但对判断行业拐点至关重要）
  4. 与市场共识不同的观点（expectation gap）
  5. 时效性信号（前瞻指引、超预期 / 低于预期）
- `## 重要数据点`
- `## 值得注意的观点/引语`（用 blockquote 保留原文，优先收录：管理层表态、专家对结构性问题的判断、反直觉观点）
- `## 结构性观察`（非数字型的长期判断，如竞争对手行为模式、行业参与者心态变化、长期趋势的早期信号；**此章节不得省略，没有则写“无”**）
- `## 与现有知识的关系` → `### 新增信息` / `### 印证之前观点` / `### 矛盾/需修正`
- `## 后续跟进项`
- `## 引用来源`

> **关于 source 编译质量的原则**：source 页面是后续所有 wiki 操作的基础（实体页面更新、日报生成、论点跟踪都基于 source，不会再回读 raw）。提取时容易偏向抓数字而漏掉结构性观点，后者往往才是判断拐点的关键。每次 ingest 前先问自己：这份报告里有没有“非数字但很重要”的判断？不确定时宁可多写，不要省略。

### 6. 对比/框架 (Comparison) — `wiki/comparison/{主题}.md`

```yaml
---
type: comparison
title: 对比标题
entities: []        # 被比较的实体
framework: ""       # 分析框架名称
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 对比概述`
- `## 对比维度`（每个维度一个子章节）
- `## 对比表格`（维度 | A | B | C ...）
- `## 分析结论`
- `## 相关页面`
- `## 引用来源`

### 7. 关键指标 (Metric) — `wiki/metric/{指标主题}.md`

```yaml
---
type: metric
title: 指标标题
entity: ""          # 关联实体 wiki link
frequency: ""       # daily | weekly | monthly | quarterly | annual
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 指标说明`
- `## 数据记录`（表格：日期 | 值 | 来源 | 备注）
- `## 趋势分析`
- `## 相关页面`

### 8. 概念 (Concept) — `wiki/concept/{概念名}.md`

```yaml
---
type: concept
name: 概念名称
aliases: []         # 别名
category: ""        # valuation | accounting | strategy | macro | regulation | other
tags: []
sources: []
last_updated: ""
---
```

**正文结构：**
- `## 定义`
- `## 在投资研究中的应用`
- `## 相关概念`
- `## 引用来源`

---

## Wiki 约定

### 命名规则
- 文件名使用中文，空格用短横线 `-` 代替
- 公司如有常用英文简称可用英文（如 `TSMC.md`、`Tesla.md`）
- 禁止特殊字符：`/ \ : * ? " < > |`

### 链接约定
- 使用 Obsidian wiki link：`[[页面名称]]` 或 `[[页面名称|显示文本]]`
- 跨目录链接：`[[company/腾讯|腾讯]]`
- 正文中首次提及某实体时**必须**加链接
- 每个页面末尾 `## 相关页面` 列出所有关联页面

### 标签约定

frontmatter 中 `tags` 使用 YAML 列表，小写英文，多词用短横线：

| 分类 | 示例 |
| --- | --- |
| 行业 | `semiconductor`, `saas`, `fintech`, `ev`, `biotech`, `consumer` |
| 策略 | `value`, `growth`, `momentum`, `event-driven`, `distressed` |
| 地域 | `china`, `us`, `japan`, `southeast-asia`, `europe` |
| 主题 | `ai`, `deglobalization`, `aging-population`, `energy-transition` |
| 状态 | `needs-update`, `high-conviction`, `contrarian` |

### 引用约定
- 事实性陈述必须标注来源：`（来源：[[source/来源页名]]）`
- 数据点标注来源和时间：`（来源：[[source/XXX]]，2025Q3）`
- 多来源一致时标注主要来源

### 矛盾处理
当新信息与已有内容矛盾时：
1. **不删除**旧信息
2. 在旧信息后添加更新标注：
   > ⚠️ 更新（YYYY-MM-DD）：[新信息内容]（来源：[[source/XXX]]）
3. 重大矛盾在 `log.md` 中记录

---

## 工作流

### Ingest（处理新来源）

用户将新素材放入 `raw/` 后，执行以下步骤：

1. **阅读来源**：仔细阅读 `raw/` 中的原始文件；如同目录存在 `{原文件名}.meta.json` sidecar 也一并读取，从中取出 `research_id` / `research_type` / `title` / `md_url` / `fetched_at` 等元数据备用
2. **与用户讨论**：列出关键要点，确认用户关注的重点
3. **创建来源摘要页**：在 `wiki/source/` 创建摘要页：
   - frontmatter 的 `research_id` 和 `research_type` 如能从 sidecar 取到则填入，没有就留空，不强制
   - `raw_path` 指向原始文件（不是 sidecar）
   - sidecar 文件本身不创建 source 页，也不在 wiki 中链接
4. **更新/创建实体页面**：对来源中每个重要实体：
   - 已有页面 → 更新（添加新信息，标注来源）
   - 没有页面 → 创建新页面
   - 重点关注：新信息是否与已有信息矛盾
5. **更新行业/概念页面**：如涉及行业趋势或重要概念
6. **更新投资论点**：如与任何 `status: active` 的 thesis 相关
7. **更新 index.md**：添加所有新建/更新页面的条目
8. **追加 log.md**：记录本次 ingest
9. **总结**：告知用户本次创建/更新了哪些页面

> 对于超过 50 页的大型文档（如完整年报），分章节处理，每处理一部分与用户确认后再继续。

### Query（回答问题）

1. **阅读 index.md**：找到可能相关的页面
2. **阅读相关页面**：深入阅读与问题相关的 wiki 页面
3. **综合回答**：基于 wiki 内容回答，附引用
4. **判断是否归档**：如果回答具有长期价值（分析、对比等）：
   - 在 `wiki/comparison/` 或 `wiki/output/` 创建新页面
   - 更新 index.md 和 log.md
5. **识别知识缺口**：发现需要但未收集的信息时告知用户

### Lint（健康检查）

用户要求 lint 或定期维护时：

1. 检查**孤立页面**：无入站链接的页面
2. 检查**过时信息**：超过 30 天未更新的 active thesis 页面
3. 检查**页面间矛盾**：不同页面对同一事实的不一致描述
4. 检查**缺失页面**：被链接但尚未创建的页面（红色链接）
5. 检查**标签一致性**：标签拼写是否统一
6. 检查**来源覆盖**：`raw/` 中是否有未 ingest 的文件
7. 检查**财务数据时效**：标注超过当前季度的数据
8. **建议补充**：基于当前内容建议应追加收集的信息
9. 更新 `log.md`：记录 lint 结果

---

## 输出格式

### Markdown 页面（默认）
标准 Markdown + YAML frontmatter，兼容 Obsidian。

### Marp 幻灯片
在 `wiki/output/slides/` 创建，frontmatter 包含 `marp: true`，用 `---` 分隔幻灯片。

### 数据表格
优先使用 Markdown 表格，以兼容 Dataview 插件。

---

## Obsidian 配置建议

### 推荐设置
- Files and links > Default location for new attachments: `raw/assets/`
- Files and links > Use `[[Wikilinks]]`: ON
- Files and links > New link format: Relative path to file

### 推荐插件
- **Dataview**：对 frontmatter 做动态查询（见下方示例）
- **Templater**：使用 `templates/` 中的模板快速创建页面
- **Marp Slides**：预览 Marp 幻灯片
- **Calendar**：按日期导航 log

### Graph View 着色建议

| 组 | 路径过滤 | 颜色 |
| --- | --- | --- |
| 公司 | `path:wiki/company` | 蓝色 |
| 人物 | `path:wiki/person` | 绿色 |
| 论点 | `path:wiki/thesis` | 红色 |
| 行业 | `path:wiki/industry` | 橙色 |
| 来源 | `path:wiki/source` | 灰色 |
| 对比 | `path:wiki/comparison` | 紫色 |
| 指标 | `path:wiki/metric` | 黄色 |

### Dataview 查询示例

**所有公司（按更新时间倒序）：**
```dataview
TABLE ticker, sector, market_cap, confidence, last_updated
FROM "wiki/company"
WHERE type = "company"
SORT last_updated DESC
```

**活跃投资论点：**
```dataview
TABLE target, direction, conviction, status
FROM "wiki/thesis"
WHERE type = "thesis" AND status = "active"
SORT conviction DESC
```

**最近 20 条来源：**
```dataview
TABLE source_type, date, quality
FROM "wiki/source"
WHERE type = "source"
SORT date DESC
LIMIT 20
```

**按标签筛选公司：**
```dataview
LIST
FROM "wiki/company"
WHERE contains(tags, "ai")
```

---

## 重要原则

1. **来源至上**：所有 wiki 内容必须可追溯到 `raw/` 中的来源
2. **增量更新**：每次只更新有新信息的部分，不重写整页
3. **保留历史**：不删除旧信息，标注更新
4. **交叉引用**：积极建立页面间链接
5. **标注不确定性**：不确定的信息明确标注 confidence level
6. **中文为主**：正文中文，专业术语保留英文
7. **实用导向**：每个页面应对投资决策有实际参考价值
