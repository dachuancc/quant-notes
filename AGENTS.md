# AGENTS.md — quant-notes

给 AI 编码助手（pi 等）的项目上下文。**开始改动前，先读 `docs/ROADMAP.md`（进度与下一步）
和 `docs/DECISIONS.md`（已定的约定）。**

## 这是什么

量化研究的**数学 / 统计笔记**仓库。纯 Markdown（带 LaTeX），无运行时依赖。
与 [`backtest-lab`](https://github.com/dachuancc/backtest-lab) 互为表里：**notes 讲原理，代码给实现**。

## 技术栈

- Markdown + LaTeX 公式（GitHub 原生支持 `$...$` / `$$...$$`）
- 唯一的"代码"是 `scripts/check_links.py`（索引一致性校验）与其测试
- 依赖与虚拟环境用 `uv` 管理（仅 dev 依赖 pytest）

## 目录结构

```
README.md                 # 索引目录（笔记的唯一入口）
notes/
├── math/                 # 概率、随机过程、线性代数
├── statistics/           # 估计、假设检验、时间序列
├── markets/              # 收益率性质、微观结构
├── strategies/           # 动量、均值回归、因子
├── backtesting/          # 陷阱、过拟合、walk-forward
└── derivatives/          # 期权定价、蒙特卡洛
scripts/check_links.py    # 校验 README 索引与笔记文件一致
tests/                    # 上述校验器的测试
```

## 常用命令

```bash
uv sync
uv run pytest                          # 索引一致性测试（改动后必须全绿）
uv run python scripts/check_links.py   # 单独跑索引校验
```

## 写作约定

- **每篇笔记固定结构**：一句话结论 → 定义/公式 → 性质 → **陷阱** → 关联实现 → 参考。
- 中文为主 + 英文术语；公式用 LaTeX。
- **新增笔记必须同时在 `README.md` 目录里加链接**，否则 CI 失败（见 D2）。
- **验证要有明确结论**：提交前跑 `pytest` + `scripts/check_links.py`，并实际渲染检查一遍公式与链接。
  **没有验证 = 没写完**。
- 文件名用英文小写连字符（`log-returns.md`），标题用中文。

## 提交信息规范

| 类别 | 格式 | 例子 |
|---|---|---|
| 新增 / 更新笔记 | `笔记: <主题>` | `笔记: 补充分层风险平价推导` |
| 其他 | `<类型>: 简述`（`文档`/`工具`/`配置`/`修复`/`测试`） | `文档: 调整目录分类` |

- 用中文，主题行简短，不以句号结尾；一次提交只做一件事。

## 当前状态

见 `docs/ROADMAP.md`「当前状态」——唯一状态真相。已收录 **3 篇**笔记，测试基线 4 个用例。

## 红线

- **不搬运受版权保护的内容**：教科书原文、付费研报、他人课程笔记一律不得整段复制；
  只写自己的理解，引用须注明出处。
- **不虚构结论**：笔记里的数字要么来自公开可查的文献，要么来自自己可复现的计算。
- **不堆砌 AI 生成的通用常识**：宁可留 TODO，也不写没有自己思考的填充内容。
