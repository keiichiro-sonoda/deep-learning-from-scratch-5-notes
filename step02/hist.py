import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

path = os.path.dirname(__file__) / Path('height.txt')

# SOCR Data を使用。
# このデータセットには、1993年の香港における18歳の身長のデータが25,000件含まれている。
# ただし、データ自体は実際の調査結果を元に作られた架空のデータ。
xs = np.loadtxt(path)
print(xs.shape) # (25000,)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.hist(xs, bins='auto', density=True)
ax.set_xlabel('Height(cm)')
ax.set_ylabel('Probability Density')
ax.grid()

plt.show()
