# Skills

本目录存放项目的可复用 skill 定义，作为**规范源**（source of truth）存档，便于团队成员参考、复制或集成到其他工具（如 Claude Code、Claude Desktop、Codex 等）。

## 目录结构

```
skills/
├── README.md                    # 本文件
└── <skill-name>/
    └── SKILL.md                 # skill 规范（frontmatter + 正文）
```

## 现有 skill

| Skill | 用途 | 入口文件 |
|-------|------|---------|
| `fetch-reports` | 从 aecapllc 平台拉取每日研究报告到 `raw/` | [fetch-reports/SKILL.md](fetch-reports/SKILL.md) |

## 与 `.claude/commands/` 的关系

Claude Code 项目级 slash command 必须放在 `.claude/commands/`，因此每个 skill 会有两处副本：

| 位置 | 作用 | 谁在维护 |
|------|------|---------|
| `skills/<name>/SKILL.md` | **规范源**，供团队阅读、复制、集成 | 本目录 |
| `.claude/commands/<name>.md` | Claude Code 实际识别的 slash command | 由 `skills/` 同步而来 |

**约定**：修改 skill 时优先修改 `skills/<name>/SKILL.md`，然后同步到 `.claude/commands/<name>.md`。两份内容应保持一致。

## 如何新增一个 skill

1. 在 `skills/<skill-name>/SKILL.md` 写规范，包含 frontmatter（name、description、argument-hint）和正文（用途、参数、执行步骤、注意事项）
2. 复制一份到 `.claude/commands/<skill-name>.md`，使 Claude Code 的 slash command 生效
3. 若有对应的执行脚本，放到 `scripts/` 下
4. 在本 README 的"现有 skill"表格中登记
