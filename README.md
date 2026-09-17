# quant-notes

**量化研究背后的数学与统计笔记。**

数学与统计是量化的地基。这里记录我在策略研究中对「**为什么**」的理解——
与 [**backtest-lab**](https://github.com/dachuancc/backtest-lab)（**怎么实现**）互为表里：
notes 讲原理，代码给实现。

[![CI](https://github.com/dachuancc/quant-notes/actions/workflows/ci.yml/badge.svg)](https://github.com/dachuancc/quant-notes/actions/workflows/ci.yml)

## 目录

### 📐 数学基础 `math`
> 待写：概率论要点 · 随机过程（鞅 / 布朗运动 / 伊藤引理）· 线性代数与主成分

### 📊 统计与计量 `statistics`
- [**夏普比率的定义与陷阱**](notes/statistics/sharpe-ratio.md) — 为什么夏普 1 也可能毫无意义
> 待写：极大似然与矩估计 · 假设检验与多重比较 · 时间序列（平稳性 / ARMA / GARCH / 协整）

### 📈 市场与收益 `markets`
- [**为什么用对数收益率（以及何时不该用）**](notes/markets/log-returns.md) — 可加性、近似、组合的陷阱
> 待写：收益率的典型事实（厚尾 / 波动聚集）· 市场微观结构 · 流动性与冲击成本

### 🧪 策略 `strategies`
> 待写：时序动量 · 横截面动量 · 均值回归 · 因子模型（Fama–French / BARRA）· 组合优化

### 🔬 回测方法论 `backtesting`
- [**未来函数（Look-ahead Bias）**](notes/backtesting/look-ahead-bias.md) — 最隐蔽的回测错误
> 待写：过拟合与多重检验 · walk-forward 与样本外 · 交易成本建模 · 回测的统计显著性

### 🎲 衍生品 `derivatives`
> 待写：Black–Scholes 推导 · 希腊字母 · 蒙特卡洛定价 · 波动率微笑

## 写作约定

每篇笔记遵循同一结构，便于快速检索：

1. **一句话**结论
2. **定义 / 公式**
3. **性质与直觉**
4. **陷阱**（这一节最重要——多数教科书不讲）
5. **关联实现**（指回 `backtest-lab` 的对应代码）
6. 参考

- 中文为主 + 英文术语；公式用 LaTeX（GitHub 原生支持 `$...$` 与 `$$...$$`）。
- 新增笔记后**必须**在上面的目录里加链接，否则 CI 会失败（见下）。

## 维护

```bash
uv sync
uv run pytest                          # 校验 README 索引与笔记文件一致
uv run python scripts/check_links.py   # 单独跑索引校验
```

## License

[CC BY 4.0](LICENSE) — 欢迎转载，注明出处即可。
