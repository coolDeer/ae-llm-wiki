# 数据库操作文档

LLM Wiki 的 PostgreSQL 实例通过 Docker Compose 管理，配置文件位于 `infra/`。

## 目录结构

```
infra/
├── docker-compose.yml   # Docker Compose 配置
└── init.sql             # 首次启动时自动执行的建表脚本
```

## 前置条件

- Docker Desktop 已安装并运行
- 端口 `5432` 未被占用（如被占用，修改 `docker-compose.yml` 中的端口映射）

## 首次启动

```bash
cd infra
docker compose up -d
```

首次启动会：
1. 拉取 `pgvector/pgvector:pg16` 镜像（约 500MB）
2. 创建持久化 volume `pgdata`
3. 执行 `init.sql`，创建扩展、表、索引
4. 容器进入 healthy 状态（约 5-10 秒）

### 验证启动成功

```bash
docker ps --filter name=llm-wiki-db
```

输出应包含 `Up X seconds (healthy)`。

```bash
docker exec llm-wiki-db psql -U wiki -d llm_wiki -c "\dx" -c "\dt"
```

应看到 `vector` 扩展和三张表（`wiki_pages`、`wiki_links`、`raw_sources`）。

---

## 日常操作

### 启动 / 停止

```bash
cd infra

# 停止（保留数据）
docker compose stop

# 启动已存在的容器
docker compose start

# 重启
docker compose restart
```

### 进入数据库 shell

```bash
docker exec -it llm-wiki-db psql -U wiki -d llm_wiki
```

常用 psql 命令：

| 命令 | 说明 |
|------|------|
| `\dt` | 列出所有表 |
| `\dx` | 列出已安装的扩展 |
| `\d wiki_pages` | 查看表结构 |
| `\di` | 列出所有索引 |
| `\du` | 列出用户 |
| `\l` | 列出所有数据库 |
| `\q` | 退出 |

### 查看日志

```bash
# 实时日志
docker logs -f llm-wiki-db

# 最近 100 行
docker logs --tail 100 llm-wiki-db
```

### 查看资源占用

```bash
docker stats llm-wiki-db --no-stream
```

---

## 备份与恢复

### 备份

```bash
# 完整备份（包含结构 + 数据）
docker exec llm-wiki-db pg_dump -U wiki llm_wiki > backup-$(date +%Y%m%d).sql

# 仅备份数据（使用自定义格式，体积更小）
docker exec llm-wiki-db pg_dump -U wiki -Fc llm_wiki > backup-$(date +%Y%m%d).dump
```

### 恢复

```bash
# 从 SQL 文件恢复
cat backup-20260412.sql | docker exec -i llm-wiki-db psql -U wiki -d llm_wiki

# 从自定义格式恢复
docker exec -i llm-wiki-db pg_restore -U wiki -d llm_wiki --clean < backup-20260412.dump
```

### 导出特定表

```bash
# 只导出 wiki_pages 表
docker exec llm-wiki-db pg_dump -U wiki -t wiki_pages llm_wiki > wiki_pages.sql
```

---

## 维护操作

### 重建向量索引（当向量数据发生大量变化时）

```sql
REINDEX INDEX idx_pages_embedding;
```

### 分析查询性能

```sql
EXPLAIN ANALYZE
SELECT path, title
FROM wiki_pages
WHERE to_tsvector('simple', content) @@ plainto_tsquery('simple', '宁德时代');
```

### 查看表大小

```sql
SELECT
    relname AS table_name,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
    pg_size_pretty(pg_relation_size(relid)) AS data_size,
    pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) AS indexes_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### VACUUM（回收空间 + 更新统计信息）

```sql
VACUUM ANALYZE wiki_pages;
```

---

## 销毁与重建

### 停止并删除容器（保留数据）

```bash
cd infra
docker compose down
```

### 完全清理（删除数据）

⚠️ **此操作会永久删除所有数据，不可恢复**

```bash
cd infra
docker compose down -v   # -v 删除 volume
```

之后重新 `docker compose up -d` 会从空库开始。

---

## 连接数据库（应用代码）

### Python

```python
import psycopg
from psycopg.rows import dict_row

conn = psycopg.connect(
    "postgresql://wiki:wiki_dev_pass@localhost:5432/llm_wiki",
    row_factory=dict_row,
)

with conn.cursor() as cur:
    cur.execute("SELECT COUNT(*) AS n FROM wiki_pages")
    print(cur.fetchone())
```

### 带 pgvector 支持

```python
import psycopg
from pgvector.psycopg import register_vector

conn = psycopg.connect("postgresql://wiki:wiki_dev_pass@localhost:5432/llm_wiki")
register_vector(conn)

with conn.cursor() as cur:
    # 向量相似度查询
    query_vec = [0.1, 0.2, ...]  # 1536 维
    cur.execute(
        "SELECT path, title FROM wiki_pages "
        "ORDER BY embedding <=> %s LIMIT 10",
        (query_vec,),
    )
    for row in cur.fetchall():
        print(row)
```

### Node.js

```javascript
import pg from 'pg';

const client = new pg.Client({
  connectionString: 'postgresql://wiki:wiki_dev_pass@localhost:5432/llm_wiki',
});

await client.connect();
const result = await client.query('SELECT COUNT(*) FROM wiki_pages');
console.log(result.rows);
```

---

## 故障排查

### 容器启动失败

```bash
docker logs llm-wiki-db
```

常见原因：
- **端口冲突**：5432 已被本机 PostgreSQL 占用 → 修改 `docker-compose.yml` 的端口映射，或停止本机 PostgreSQL
- **init.sql 语法错误**：查看日志，修复后需要 `docker compose down -v` 重建

### 连接被拒绝

```bash
# 检查容器是否健康
docker ps --filter name=llm-wiki-db

# 从容器内部测试连接
docker exec llm-wiki-db pg_isready -U wiki -d llm_wiki
```

### 查询慢

1. 检查是否用上了索引：`EXPLAIN ANALYZE <query>`
2. 向量查询慢 → 检查 HNSW 索引是否存在：`\di idx_pages_embedding`
3. 全文搜索慢 → 确认 GIN 索引：`\di idx_pages_fulltext`
4. 数据量大 → `VACUUM ANALYZE` 更新统计信息

### 数据看不到

- 确认连接的是正确的数据库：`\l` 查看数据库列表，`\c llm_wiki` 切换
- 确认 Docker volume 未被误删：`docker volume ls | grep pgdata`

---

## 生产环境注意事项

当前配置是**开发环境**，生产部署时需要：

1. **修改密码**：`wiki_dev_pass` → 强密码，通过环境变量或 secret 注入
2. **限制网络访问**：不要暴露 `5432` 到公网，用 VPC 或 SSH tunnel
3. **启用 SSL**：配置 `ssl=on` 并提供证书
4. **定期备份**：crontab 自动 `pg_dump`
5. **资源限制**：在 `docker-compose.yml` 中配置 `deploy.resources.limits`
6. **监控**：接入 Prometheus + postgres_exporter
7. **高可用**：考虑主从复制或托管服务（RDS / Cloud SQL）
