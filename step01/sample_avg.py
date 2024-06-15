import numpy as np

# サンプルサイズ
N = 3

xs = []
for n in range(N):
    # 一様分布からの乱数
    x = np.random.rand()
    xs.append(x)

x_mean = np.mean(xs)
print(x_mean)
