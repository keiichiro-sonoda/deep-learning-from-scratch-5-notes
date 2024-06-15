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

x = np.linspace(-5, 5, 101)
print(x) # [-5.  -4.9 -4.8 ...  5. ]
y = normal(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
