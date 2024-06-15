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

x = np.linspace(-10, 10, 1000)

# 平均値を動かす
y0 = normal(x, mu=-3)
y1 = normal(x, mu=0)
y2 = normal(x, mu=5)

# 標準偏差を動かす
y3 = normal(x, sigma=0.5)
y4 = normal(x, sigma=1)
y5 = normal(x, sigma=2)

fig = plt.figure(figsize=(8, 8))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(x, y0, label=r'$\mu=-3$')
ax1.plot(x, y1, label=r'$\mu=0$')
ax1.plot(x, y2, label=r'$\mu=5$')

ax2.plot(x, y3, label=r'$\sigma=0.5$')
ax2.plot(x, y4, label=r'$\sigma=1$')
ax2.plot(x, y5, label=r'$\sigma=2$')

ax1.legend()
ax1.grid()
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Mean')

ax2.legend()
ax2.grid()
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Standard deviation')

plt.show()
