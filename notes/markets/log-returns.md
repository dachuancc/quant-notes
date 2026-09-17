# 为什么用对数收益率（以及何时不该用）

> **一句话**：对数收益率可加、近似简单收益率、在 GBM 下服从正态——但**组合收益率不可加**。

## 定义

设 $P_t$ 为 $t$ 时刻价格。

**简单收益率**（simple return）：

$$r_t = \frac{P_t}{P_{t-1}} - 1 = \frac{P_t - P_{t-1}}{P_{t-1}}$$

**对数收益率**（log return / continuously compounded）：

$$x_t = \ln\frac{P_t}{P_{t-1}} = \ln(1 + r_t)$$

## 三个关键性质

### 1. 时间可加

多期对数收益率直接相加：

$$\sum_{t=1}^{T} x_t = \ln\frac{P_T}{P_0}$$

而简单收益率不可加：$\prod_{t=1}^{T}(1+r_t) - 1 \ne \sum_{t=1}^{T} r_t$。

这是对数收益率最实用的地方——做时间序列统计时可以直接求和 / 求均值。

### 2. 小量近似

对 $\ln(1+r)$ 做泰勒展开：

$$x_t = \ln(1+r_t) = r_t - \frac{r_t^2}{2} + \frac{r_t^3}{3} - \cdots \approx r_t \quad (|r_t| \ll 1)$$

日频数据 $|r_t| \sim 10^{-2}$，误差 $O(r^2) \sim 10^{-4}$，可忽略。但**大波动时不可忽略**——
例如 $r = 50\%$，$x = 40.5\%$，差近 10 个百分点。

### 3. GBM 下服从正态

若价格服从几何布朗运动 $P_t = P_0 \exp\big((\mu - \tfrac12\sigma^2)t + \sigma W_t\big)$，则

$$x_t \sim \mathcal{N}\!\left(\mu\,\Delta t,\ \sigma^2 \Delta t\right), \quad \text{i.i.d.}$$

这是 Black–Scholes 定价与大量统计推断的出发点。

## 陷阱

1. **组合收益率不可加**
   组合的简单收益率是成分的**加权平均**：$r_p = \sum_i w_i r_i$。
   而对数收益率的加权和 $\sum_i w_i x_i \ne \ln(1 + r_p)$。
   **做组合时先加权简单收益率，再累乘成净值**，不要直接加对数收益率。

2. **年化时 Jensen 不等式**
   $\hat\mu = 252 \cdot \bar{x}$ 是年化对数收益率的无偏估计，但 $e^{\hat\mu} - 1$（年化简单收益率）
   是**有偏**的：$\mathbb{E}[e^{\hat\mu}] \ge e^{\mathbb{E}[\hat\mu]}$。

3. **对称性的错觉**
   对数收益率对涨跌对称（$+x$ 与 $-x$ 抵消），简单收益率不对称（跌 50% 需涨 100% 才回本）。
   哪个"正确"取决于问题：算 PnL 用简单收益率，算风险用对数收益率。

4. **正态假设在尾部失效**
   真实收益率**尖峰厚尾**（fat tails）。用正态算 $\pm 4\sigma$ 的风险会严重低估。

## 关联实现

- `backtest-lab` 的 `engine.py` 用**简单收益率** `prices.pct_change()`——因为要按仓位加权后累乘成净值。
- 估计波动率 / 年化收益时，改用对数收益率口径更自然。

## 参考

- Meucci, *Risk and Asset Allocation*, ch. 2
- 任意时间序列教材的 "stylized facts of asset returns" 章节
