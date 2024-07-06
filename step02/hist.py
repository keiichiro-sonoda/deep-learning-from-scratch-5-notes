import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def normal(x: float, mu: float = 0, sigma: float = 1) -> float:
    y = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    return y

path = os.path.dirname(__file__) / Path('height.txt')

# SOCR Data を使用。
# このデータセットには、1993年の香港における18歳の身長のデータが25,000件含まれている。
# ただし、データ自体は実際の調査結果を元に作られた架空のデータ。
xs = np.loadtxt(path)
print(xs.shape) # (25000,)

# サンプルの平均と標準偏差。
mu = np.mean(xs)
sigma = np.std(xs)

print(mu)
print(sigma)

x = np.linspace(150, 190, 1000)
y = normal(x, mu, sigma)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.hist(xs, bins='auto', density=True)
ax.plot(x, y)
ax.set_xlabel('Height(cm)')
ax.set_ylabel('Probability Density')
ax.grid()

plt.show()
