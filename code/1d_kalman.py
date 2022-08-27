import matplotlib.pyplot as plt
import random
from statistics import mean
import pandas as pd


def current_k(p: float) -> float:
    return (p + q) / (p + q + r)


def next_p(p: float, k: float) -> float:
    return (1 - k) * (p + q)


def next_m(m, z, k: float) -> float:
    return m + k * (z - m)


# configuration of the Kalman filter
r = 1
q = 0
p = 1
m = 1

# zs is the measured with noise
zs = []

# variables of the Kalman filter
# variance estimate
ps = []
# kalman gain
ks = []


# m is the smoothed output
ms = []
cumulative_avg = []
exponential_avg = []
count = 50

for i in range(count):
    zs.append(random.gauss(0, 1))


m = zs[0]

for i in range(count):
    k = current_k(p)
    ks.append(k)
    p = next_p(p, k)
    ps.append(p)
    m = next_m(m, zs[i], k)
    ms.append(m)
    cumulative_avg.append(mean(zs[:i + 1]))


exponential_avg = pd.Series(zs).ewm(alpha=ks[-1]).mean()


plt.plot(ks, label='ks')
plt.plot(ps, label='ps')
plt.legend()
plt.show()

plt.plot(ms, label='kalman filter', linewidth=1)
plt.plot(cumulative_avg, label='cumulative avg', linestyle='dashed')
plt.plot(exponential_avg, label='exponential moving avg', linewidth=3, linestyle='dashed')
plt.legend()

plt.savefig('../images/test.png')
plt.show()