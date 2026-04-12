# 数据库表结构

LLM Wiki 使用 PostgreSQL 16 + pgvector 0.8.2，承载 wiki 页面元数据、全文内容、向量 embedding 及页面间关系。

## 连接信息

| 项 | 值 |
|---|---|
| Host | `localhost` |
| Port | `5432` |
| Database | `llm_wiki` |
| User | `wiki` |
| Password | `wiki_dev_pass`（开发环境） |
| 连接串 | `postgresql://wiki:wiki_dev_pass@localhost:5432/llm_wiki` |

## 扩展

| 扩展 | 版本 | 用途 |
|------|------|------|
| `vector` (pgvector) | 0.8.2 | 向量存储与相似度搜索，支持 HNSW 索引 |
| `plpgsql` | 1.0 | 默认存储过程语言 |

---

## 表结构

### 1. `wiki_pages` — 页面主表

存储所有 wiki 页面的结构化数据，是系统的核心表。

```sql
CREATE TABLE wiki_pages (
    id          SERIAL PRIMARY KEY,
    path        TEXT UNIQUE NOT NULL,
    type        TEXT NOT NULL,
    title       TEXT NOT NULL,
    metadata    JSONB NOT NULL DEFAULT '{}',
    content     TEXT NOT NULL,
    embedding   VECTOR(1536),
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    updated_at  TIMESTAMPTZ DEFAULT NOW()
);
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | SERIAL | 自增主键 |
| `path` | TEXT UNIQUE | 页面路径，如 `company/宁德时代`（不含 `.md` 后缀） |
| `type` | TEXT | 页面类型：`company` / `person` / `industry` / `thesis` / `source` / `comparison` / `metric` / `concept` / `output` |
| `title` | TEXT | 页面标题 |
| `metadata` | JSONB | 从 frontmatter 解析的字段（ticker、sector、tags、sources、confidence 等） |
| `content` | TEXT | Markdown 正文（不含 frontmatter） |
| `embedding` | VECTOR(1536) | 正文的向量表示，用于语义检索 |
| `created_at` | TIMESTAMPTZ | 首次入库时间 |
| `updated_at` | TIMESTAMPTZ | 最后更新时间 |

#### metadata 字段示例

不同类型页面的 `metadata` 字段差异：

```json
// type = 'company'
{
  "ticker": "300750.SZ",
  "exchange": "SZSE",
  "sector": "新能源",
  "sub_sector": "锂电池",
  "market_cap": "",
  "founded": "2011",
  "hq": "福建宁德",
  "key_people": [],
  "tags": ["china", "ev", "battery"],
  "sources": ["source/Merit-锂电池龙头排产调研-260410"],
  "confidence": "medium",
  "last_updated": "2026-04-11"
}

// type = 'source'
{
  "source_type": "transcript",
  "author": "Merit",
  "date": "2026-04-10",
  "raw_path": "raw/transcripts/meeting_minutes/xxx.md",
  "entities": ["company/宁德时代"],
  "quality": "high",
  "tags": ["china", "ev"]
}

// type = 'thesis'
{
  "target": "company/宁德时代",
  "direction": "long",
  "conviction": "high",
  "status": "active",
  "date_opened": "2026-04-11"
}
```

#### 索引

| 索引 | 类型 | 用途 |
|------|------|------|
| `idx_pages_type` | B-tree on `type` | 按类型过滤 |
| `idx_pages_metadata` | GIN on `metadata` | JSONB 字段查询（tags、ticker 等） |
| `idx_pages_updated` | B-tree on `updated_at DESC` | 最近更新排序 |
| `idx_pages_fulltext` | GIN on `to_tsvector('simple', content)` | 全文搜索 |
| `idx_pages_embedding` | HNSW on `embedding vector_cosine_ops` | 向量相似度搜索 |

---

### 2. `wiki_links` — 页面间关系

存储 Obsidian `[[wikilink]]` 构成的页面关系图，用于：
- 主题子图提取（导出某个主题相关的所有页面）
- 孤立页面检测
- 交叉引用完整性检查

```sql
CREATE TABLE wiki_links (
    source_path TEXT NOT NULL,
    target_path TEXT NOT NULL,
    context     TEXT,
    PRIMARY KEY (source_path, target_path)
);
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `source_path` | TEXT | 发起链接的页面 |
| `target_path` | TEXT | 被链接的页面 |
| `context` | TEXT | 链接所在的上下文句子（可选，用于展示） |

> 注：`target_path` 不一定存在于 `wiki_pages` 中——被链接但未创建的页面（红色链接）也会被记录，用于 lint 时发现缺失页面。

---

### 3. `raw_sources` — 原始文件登记

记录 `raw/` 目录下的所有原始素材文件，是 ingest pipeline 的输入队列。

```sql
CREATE TABLE raw_sources (
    id          SERIAL PRIMARY KEY,
    filename    TEXT UNIQUE NOT NULL,
    file_type   TEXT,
    content     TEXT NOT NULL,
    ingested    BOOLEAN DEFAULT FALSE,
    ingested_at TIMESTAMPTZ,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | SERIAL | 自增主键 |
| `filename` | TEXT UNIQUE | 相对路径，如 `raw/reports/69d917787fe7887cc45c16a2.md` |
| `file_type` | TEXT | `transcript` / `report` / `filing` / `article` 等 |
| `content` | TEXT | 原文内容 |
| `ingested` | BOOLEAN | 是否已经被 ingest 成 wiki 页面 |
| `ingested_at` | TIMESTAMPTZ | ingest 完成时间 |
| `created_at` | TIMESTAMPTZ | 入库时间 |

---

## 常用查询示例

### 按类型列出页面

```sql
SELECT path, title, metadata->>'last_updated' AS updated
FROM wiki_pages
WHERE type = 'company'
ORDER BY updated_at DESC;
```

### 按标签筛选

```sql
SELECT path, title
FROM wiki_pages
WHERE metadata->'tags' ? 'ai'
ORDER BY updated_at DESC;
```

### 活跃投资论点

```sql
SELECT path, title,
       metadata->>'target' AS target,
       metadata->>'direction' AS direction,
       metadata->>'conviction' AS conviction
FROM wiki_pages
WHERE type = 'thesis'
  AND metadata->>'status' = 'active'
ORDER BY (metadata->>'conviction') DESC;
```

### 全文搜索

```sql
SELECT path, title,
       ts_rank(to_tsvector('simple', content), plainto_tsquery('simple', '宁德时代 排产')) AS rank
FROM wiki_pages
WHERE to_tsvector('simple', content) @@ plainto_tsquery('simple', '宁德时代 排产')
ORDER BY rank DESC
LIMIT 10;
```

### 向量相似度搜索

```sql
SELECT path, title,
       1 - (embedding <=> $1::vector) AS similarity
FROM wiki_pages
WHERE embedding IS NOT NULL
ORDER BY embedding <=> $1::vector
LIMIT 10;
```

### 混合搜索（向量 + 全文）

```sql
SELECT path, title,
       (1 - (embedding <=> $1::vector)) * 0.6
       + ts_rank(to_tsvector('simple', content), plainto_tsquery('simple', $2)) * 0.4
       AS score
FROM wiki_pages
WHERE embedding IS NOT NULL
ORDER BY score DESC
LIMIT 10;
```

### 主题子图提取（一层扩展）

```sql
-- 给定一个起始页面，找出所有直接关联的页面
WITH seed AS (
    SELECT 'industry/日本不动产' AS path
),
direct_links AS (
    SELECT target_path AS path FROM wiki_links
    WHERE source_path IN (SELECT path FROM seed)
    UNION
    SELECT source_path FROM wiki_links
    WHERE target_path IN (SELECT path FROM seed)
)
SELECT p.*
FROM wiki_pages p
WHERE p.path IN (SELECT path FROM direct_links)
   OR p.path IN (SELECT path FROM seed);
```

### 孤立页面检测（lint）

```sql
SELECT p.path, p.title
FROM wiki_pages p
LEFT JOIN wiki_links l ON l.target_path = p.path
WHERE l.target_path IS NULL
  AND p.type NOT IN ('index', 'log');
```

### 缺失页面（红色链接）

```sql
SELECT DISTINCT l.target_path
FROM wiki_links l
LEFT JOIN wiki_pages p ON p.path = l.target_path
WHERE p.path IS NULL;
```

### 待 ingest 的原始文件

```sql
SELECT filename, file_type, created_at
FROM raw_sources
WHERE ingested = FALSE
ORDER BY created_at DESC;
```
