import matplotlib.pyplot as plt
import random
from statistics import mean
import pandas as pd


def current_k(p: float) -> float:
    return (p + q) / (p + q + r)


def next_p(p: float, k: float) -> float:
    return (1 - k) * (p + q)


def next_m(m, x, k: float) -> float:
    return m + k * (x - m)


r = 5
q = 2
p = 5
m = 0
ps = []
ks = []
xs = []
ms = []
cumulative_avg = []
exponential_avg = []
count = 50

for i in range(count):
    xs.append(random.gauss(0, 1))


m = xs[0]

for i in range(count):
    k = current_k(p)
    ks.append(k)
    p = next_p(p, k)
    ps.append(p)
    m = next_m(m, xs[i], k)
    ms.append(m)
    cumulative_avg.append(mean(xs[:i+1]))


exponential_avg = pd.Series(xs).ewm(alpha=ks[-1]).mean()


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
