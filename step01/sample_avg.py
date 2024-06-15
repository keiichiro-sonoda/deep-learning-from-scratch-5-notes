import numpy as np
import matplotlib.pyplot as plt

# シード値を0に設定
# np.random.seed(0)

x_means = []

# サンプルサイズ
# まずはサンプルサイズ1から
N = 1

for _ in range(10000):
    xs = []
    for n in range(N):
        # 一様分布からの乱数
        x = np.random.rand()
        xs.append(x)
    mean = np.mean(xs)
    x_means.append(mean)

# グラフの描画
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# densityとは、ヒストグラムの縦軸を確率密度にするためのオプション
ax.hist(x_means, bins='auto', density=True)
ax.set_title(f'N={N}')
ax.set_xlabel('mean')
# y軸は「確率密度」
ax.set_ylabel('Probability Density')
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(0, 5)
plt.show()
