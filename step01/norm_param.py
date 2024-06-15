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

y0 = normal(x, mu=-3)
y1 = normal(x, mu=0)
y2 = normal(x, mu=5)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.plot(x, y0, label=r'$\mu=-3$')
ax.plot(x, y1, label=r'$\mu=0$')
ax.plot(x, y2, label=r'$\mu=5$')
ax.legend()
ax.grid()
plt.show()
