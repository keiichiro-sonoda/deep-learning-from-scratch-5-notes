## 正規分布の最尤推定

$$
\mathcal{N}(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

$N$ 個の観測データからなるサンプル $\mathcal{D} = \{x^(1), x^(2), \ldots, x^(N)\}$ が与えられたとする。このときの尤度は

$$
\begin{aligned}
p(\mathcal{D}; \mu, \sigma) &= \prod_{n=1}^{N}\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right) \\
&= \left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^N \prod_{n=1}^{N}\exp\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right) \\
\end{aligned}
$$

となる。対数尤度は

$$
\begin{aligned}
\ln p(\mathcal{D}; \mu, \sigma) &= \ln \left(\left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^N \prod_{n=1}^{N}\exp\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right)\right) \\
&= \ln \left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^N + \ln \prod_{n=1}^{N}\exp\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right) \\
&= N\ln\left(\frac{1}{\sqrt{2\pi\sigma^2}}\right) + \sum_{n=1}^{N}\ln\exp\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right) \\
&= N\ln\left(2\pi\sigma^2\right)^{-\frac{1}{2}} + \sum_{n=1}^{N}\left(-\frac{(x^{(n)}-\mu)^2}{2\sigma^2}\right) \\
&= -\frac{N}{2}\ln2\pi\sigma^2 - \frac{1}{2\sigma^2}\sum_{n=1}^{N}(x^{(n)}-\mu)^2
\end{aligned}
$$

となる。これは $\mu$ の2次関数になっており、$\mu$ の2乗の係数は負の値を取るため、微分が0の場所で最大値を取る。$\mu$ に関して微分すると

$$
\begin{aligned}
\frac{\partial L}{\partial \mu} &= -\frac{1}{2\sigma^2}\sum_{n=1}^{N}\left(-2(x^{(n)}-\mu)\right) \\
&= \frac{1}{\sigma^2}\sum_{n=1}^{N}(x^{(n)}-\mu) \\
\end{aligned}
$$

となる。これを0とおいて解くと

$$
\begin{aligned}
& \frac{1}{\sigma^2}\sum_{n=1}^{N}(x^{(n)}-\mu) = 0 \\
\Leftrightarrow \hspace{1em} & \sum_{n=1}^{N}(x^{(n)}-\mu) = 0 \\
\Leftrightarrow \hspace{1em} & \sum_{n=1}^{N}\mu = \sum_{n=1}^{N}x^{(n)} \\
\Leftrightarrow \hspace{1em} & N\mu = \sum_{n=1}^{N}x^{(n)} \\
\therefore \hspace{1em} & \mu = \frac{1}{N}\sum_{n=1}^{N}x^{(n)}
\end{aligned}
$$

となる。これを $\hat{\mu}$ と置くと

$$
\hat{\mu} = \frac{1}{N}\sum_{n=1}^{N}x^{(n)}
$$

となる。$hat{\mu}$ はサンプル平均である。$ \mu = \hat{\mu} $ とおいて $\sigma$ に関して最大化したい。$ \mu = \hat{\mu} $ のときの対数尤度は

$$
\ln p(\mathcal{D}; \mu = \hat{\mu}, \sigma) = -\frac{N}{2}\ln2\pi\sigma^2 - \frac{1}{2\sigma^2}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2
$$

となる。対数尤度を最大化する $\sigma$ の値も、$\mu$ と同様に解析的に求めることができる。対数尤度の $\sigma$ に関する微分では、$\frac{d}{d\sigma}(\ln 2\pi\sigma^2)$ を計算する必要がある。先に計算しておくと

$$
\begin{aligned}
\frac{d}{d\sigma}(\ln 2\pi\sigma^2) &= \frac{d}{d\sigma}(\ln 2\pi + \ln\sigma^2) \\
&= \frac{d}{d\sigma}(\ln\sigma^2) \\
&= \frac{d}{d\sigma}(2\ln\sigma) \\
&= \frac{2}{\sigma}
\end{aligned}
$$

となる。これを用いて対数尤度を $\sigma$ で微分すると

$$
\begin{aligned}
\frac{\partial}{\partial\sigma}\ln p(\mathcal{D}; \mu = \hat{\mu}, \sigma) &= -\frac{N}{2}\frac{\partial}{\partial\sigma}\left(\ln 2\pi\sigma^2\right) - \frac{\partial}{\partial\sigma}\left(\frac{1}{2\sigma^2}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2\right) \\
&= -\frac{N}{2}\frac{2}{\sigma} - \frac{1}{2}(-2)\sigma^{-3}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 \\
&= -\frac{N}{\sigma} + \frac{1}{\sigma^3}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 \\
\end{aligned}
$$

となる。これを0とおいて解くと

$$
\begin{aligned}
& -\frac{N}{\sigma} + \frac{1}{\sigma^3}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 = 0 \\
\Leftrightarrow \hspace{1em} & \frac{N}{\sigma} = \frac{1}{\sigma^3}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 \\
\Leftrightarrow \hspace{1em} & N\sigma^2 = \sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 \\
\Leftrightarrow \hspace{1em} & \sigma^2 = \frac{1}{N}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2 \\
\therefore \hspace{1em} & \sigma = \sqrt{\frac{1}{N}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2}
\end{aligned}
$$

となる。これを $\hat{\sigma}$ と置くと

$$
\hat{\sigma} = \sqrt{\frac{1}{N}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2}
$$

となる。$\hat{\sigma}$ はサンプル標準偏差である。以上より、正規分布の最尤推定は以下のようになる。

$$
\begin{aligned}
\hat{\mu} &= \frac{1}{N}\sum_{n=1}^{N}x^{(n)} \\
\hat{\sigma} &= \sqrt{\frac{1}{N}\sum_{n=1}^{N}(x^{(n)}-\hat{\mu})^2}
\end{aligned}
$$
