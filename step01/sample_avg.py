import numpy as np
import matplotlib.pyplot as plt

# シード値を0に設定
# np.random.seed(0)

fig = plt.figure(figsize=(8, 6))

for i, N in enumerate([1, 2, 4, 10]):
    x_means = []

    for _ in range(10000):
        xs = []
        for n in range(N):
            # 一様分布からの乱数
            x = np.random.rand()
            xs.append(x)
        mean = np.mean(xs)
        x_means.append(mean)

    # グラフの描画
    ax = fig.add_subplot(2, 2, i + 1)

    # densityとは、ヒストグラムの縦軸を確率密度にするためのオプション
    ax.hist(x_means, bins='auto', density=True)
    ax.set_title(f'N={N}')
    ax.set_xlabel('mean')
    # y軸は「確率密度」
    ax.set_ylabel('Probability Density')
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0, 5)

# 縦の間隔を広げる
fig.subplots_adjust(hspace=0.5)

# figフォルダにsvgで保存
# ブラウザなどで確認できる
plt.savefig('fig/sample_avg.svg')

plt.show()
