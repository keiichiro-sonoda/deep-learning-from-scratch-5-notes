import numpy as np
import matplotlib.pyplot as plt

def normal(x: float, mu: float = 0, sigma: float = 1) -> float:
    """
    正規分布の確率密度関数。

    Args:
        x (float): 確率変数。
        mu (float): 平均。
        sigma (float): 標準偏差。

    Returns:
        float: 確率密度関数の値。
    """
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    return y

# シード値を0に設定
# np.random.seed(0)

fig = plt.figure(figsize=(8, 6))

N = 5

x_sums = []

for _ in range(10000):
    xs = []
    for n in range(N):
        # 一様分布からの乱数
        x = np.random.rand()
        xs.append(x)
    t = np.sum(xs)
    x_sums.append(t)

# 正規分布
x_norm = np.linspace(-2.5, 7.5, 1001)
mu = N / 2
sigma = np.sqrt(N / 12)
y_norm = normal(x_norm, mu, sigma)

# グラフの描画
ax = fig.add_subplot(111)

# densityとは、ヒストグラムの縦軸を確率密度にするためのオプション
ax.hist(x_sums, bins='auto', density=True)
ax.plot(x_norm, y_norm)

ax.set_title(f'N={N}')
ax.set_xlabel('mean')
# y軸は「確率密度」
ax.set_ylabel('Probability Density')
ax.set_xlim(-1, 6)

# 縦の間隔を広げる
fig.subplots_adjust(hspace=0.5)

plt.show()
