-- 启用 pgvector 扩展
CREATE EXTENSION IF NOT EXISTS vector;

-- wiki 页面主表
CREATE TABLE IF NOT EXISTS wiki_pages (
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

-- 页面间链接
CREATE TABLE IF NOT EXISTS wiki_links (
    source_path TEXT NOT NULL,
    target_path TEXT NOT NULL,
    context     TEXT,
    PRIMARY KEY (source_path, target_path)
);

-- 原始来源文件
CREATE TABLE IF NOT EXISTS raw_sources (
    id          SERIAL PRIMARY KEY,
    filename    TEXT UNIQUE NOT NULL,
    file_type   TEXT,
    content     TEXT NOT NULL,
    ingested    BOOLEAN DEFAULT FALSE,
    ingested_at TIMESTAMPTZ,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- 索引
CREATE INDEX IF NOT EXISTS idx_pages_type ON wiki_pages(type);
CREATE INDEX IF NOT EXISTS idx_pages_metadata ON wiki_pages USING GIN(metadata);
CREATE INDEX IF NOT EXISTS idx_pages_updated ON wiki_pages(updated_at DESC);
CREATE INDEX IF NOT EXISTS idx_pages_fulltext ON wiki_pages USING GIN(to_tsvector('simple', content));
-- 向量索引（HNSW 适合中小规模，查询快）
CREATE INDEX IF NOT EXISTS idx_pages_embedding ON wiki_pages USING hnsw (embedding vector_cosine_ops);
