---
type: source
title: Merit 公开路演：周度调研重点更新
source_type: transcript
author: Merit Research
date: "2026-04-13"
raw_path: "raw/2026-04-13/meeting_minutes/260413 - Merit 公开路演：周度调研重点更新_260413100921.md"
research_id: "69dc544c96aab61ca8ce4456"
research_type: meeting_minutes
entities:
  - "[[industry/锂电池与储能]]"
  - "[[company/Anthropic]]"
  - "[[company/Google]]"
  - "[[company/Amazon]]"
  - "[[company/Meta]]"
  - "[[company/Microsoft]]"
quality: high
tags:
  - ai
  - semiconductor
  - cloud
  - biotech
  - china
  - energy-storage
last_updated: "2026-04-13"
---

## 来源概要

Merit Research 的周度公开路演，涵盖前沿 AI 模型趋势（Anthropic/Meta/国内大模型）、AI 算力产业链（Google 非 HBM LPU、NCP 价值、立讯精密光模块）、北美超大规模云厂商排序调整、A 股制造业（金盘科技/阳光电源）及生物医药（大型药企分析/国内创新药），锂电池产业链亦有涉及（阳光电源储能业务）。

## 关键要点

1. **核心数据**：
   - Anthropic 今年预计为 AWS 贡献约 280 亿美元收入（增量约 220-230 亿美元），占 AWS 全年增量收入 50%+
   - Google 非 HBM LPU：中性情景 2028 年出货 1000 万颗，Marvell 增量 EPS 约+0.7；乐观情景 3500 万颗，增量 EPS+3.5
   - 立讯精密进入谷歌光模块供应链：2026/2027 年收入假设 5.3/25.2 亿美元（5%/10% 份额），对应净利润增量 1.6/7.5 亿美元
   - 阳光电源全年利润预期 106-107 亿元，对应 PE 约 16.5 倍
   - CoreWeave vs Northern Data：2027 年 EBIT PE 均约 9-10 倍

2. **关键判断**：
   - Hyperscaler 推荐排序：Amazon > Google > Meta > Microsoft
   - Anthropic 新模型编码能力跃升（60 → 80+ 分，GPT-3.5→GPT-4 级别的飞跃），通过蒸馏技术可将 Opus 4.6 级 API 成本降至现有 1/10
   - Microsoft 核心 Office 业务面临 Agent 颠覆风险比预期更快
   - 国内头部模型厂商正从纯开源转向部分闭源（商业化压力）

3. **行业参与者行为模式**：
   - 算力极度短缺下，原本滞销的 AWS Trainium 芯片被 Anthropic 采用训练（部分参与），Trainium 3 已提前售罄——这是需求侧倒逼"次优方案"快速落地的典型
   - NCP（中立云厂商）在模型公司需求爆发中议价能力提升，合同条款改善；CoreWeave 近期连续签大单验证了这一趋势
   - 国内大模型厂商（阿里、智谱、Minimax）部分核心模型转为闭源——在算力紧缺背景下，开源模型被海外免费部署但原厂商无法获益的矛盾已无法持续

4. **与市场共识不同的观点**：
   - 市场对 Microsoft Azure Q1 增速有较高预期，Merit 认为 Azure 将明显弱于 AWS 和 GCP（对 Anthropic 敞口小，DC 产能 Q1 上线晚）
   - Google 编码能力市场认为落后，Merit 认为是前期投入倾斜不足，GI/O 大会将发布 Agent 产品，追赶速度被低估

5. **时效性信号**：
   - Meta Q1 广告增长好于预期（预计接近 20%，市场预期十几）
   - Google 非 HBM LPU 预计 2027 年 H2 开始出货
   - 锂电相关：阳光电源 Q1 环比将显著改善，Q2 欧洲高价订单交付 + PowerTitan 3.0 发布

## 重要数据点

| 主题 | 数据 | 备注 |
|------|------|------|
| AWS 来自 Anthropic 的增量收入 | ~220-230亿美元 | 2026年预测 |
| Trainium 3 | 已提前售罄 | 算力需求倒逼 |
| NCP CoreWeave 2027 EBIT PE | ~9x | 对比 NBS ~10x |
| 立讯精密光模块 2027 净利贡献 | ~7.5亿美元 | 10%份额假设 |
| 光模块测试设备市场规模 | 200亿元 | 预计2027年全球 |
| 阳光电源2026利润预期 | 106-107亿元 | PE~16.5x |
| Meta Q1 广告增速 | 接近20% | 市场预期十几 |

## 值得注意的观点/引语

> "算力本身再次成为行业发展的明确瓶颈，全行业正积极寻求突破资源限制的方案。"

> "Anthropic 新模型编码能力评分从 60 分提升至 80 分以上，是在 TPU v7 或 Blackwell 级别硬件集群上训练出的首个模型，能力提升巨大。"

> "微软的核心 Office 业务正面临比预期更快的来自 Agent 的颠覆，Copilot 本身的增长无法完全对冲此风险。"

## 结构性观察

1. **算力短缺重塑超大规模云厂格局**：当 Anthropic 需求溢出导致 AWS 将"NCP 式 GPU 租赁"变成核心收入来源时，传统 IaaS 毛利模型被打破（GPU 租赁利润率低于原生云服务）。这意味着 AWS 的 AWS 的收入增速可能超预期，但利润率可能低于预期——这是对 AWS margin 预测的关键修正。

2. **编码能力飞跃的产业链影响**：模型编码能力从 GPT-3.5 跃升至 GPT-4 级别，叠加蒸馏降本，将直接加速"AI 工程师辅助编程"的规模化落地。与此同时，"顶尖专家反馈"比"用户使用量"更关键的洞察，意味着数据飞轮逻辑在编码赛道部分失效——这对认为"用户规模=护城河"的估值逻辑是一个挑战。

3. **锂电储能（阳光电源）困境中的结构性看点**：Q4 miss 掩盖了结构性亮点——PowerTitan 3.0 可降本 12%，800V 高压直流可能开启 AIDC 配储新市场（若 AI 数据中心储能需求落地）。这两条增长曲线需要 2026 年产品发布后跟踪验证，但估值已足够安全边际（PE ~16.5x）。

## 与现有知识的关系

### 新增信息

- Merit Hyperscaler 排序调整逻辑（Amazon > Google > Meta > Microsoft）
- Google 非 HBM LPU 产业链机会量化（Marvell + Astera Labs 增量 EPS）
- 国内大模型从开源转闭源的战略转变
- 立讯精密进入谷歌光模块供应链

### 印证之前观点

- 与[[industry/锂电池与储能]]中阳光电源储能业务逻辑一致
- 与[[company/Anthropic]]算力需求高增长观点一致

### 矛盾/需修正

- 无

## 后续跟进项

1. Google I/O 大会 Agent 产品发布情况
2. AWS Q1 实际收入及利润率
3. 立讯精密谷歌光模块订单落地进展
4. 阳光电源 PowerTitan 3.0 商业化节奏

## 引用来源

- 原始文件：`raw/2026-04-13/meeting_minutes/260413 - Merit 公开路演：周度调研重点更新_260413100921.md`
