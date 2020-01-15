---
layout: post
title: "1D Kalman Is Exponential Or Cumulative Average"
date: 2019-08-28
---

# Abstract
Kalman filter [(Kalman 1960)](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf) also known as linear quadratic estimation (LQE) is an iterative algorithm that uses noisy measurements to estimate values and variance of unknown variables. The Kalman filter allows incorporation of known state space behaviour (e.g. momentum of physical particle) and outside-the-model estimated variance of sensor measurement (measurement uncertainty) and unknown factors (process noise).

This blog post proves that Kalman filter in 1D with constant measurement uncertainty and process noise asymptotically behaves as:

 - cumulative average in case of zero process noise
 - exponential average in case of non zero process noise
 
The proof relies on Kalman filter asymptotically doesn't depend on initial state. In general since Kalman filter equations are differentiable, it is reasonable to expect that above could be generalized to nearly-constant uncertainty and process noise.


# Proofs

## Constant Measurement Uncertainty, No Process Noise

Below is the proof relies on good choice of initial value of Kalman variance ```P0``` to simplify recursive equation to match cumulative average equation.

<img alt="Proof Kalman 1d with constant measurement uncertainty and no process noise proof" style="width: 80%; max-width: 900px" src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-without-process-noise-proof.jpg">

Plot of the convergence.

<img alt="Proof Kalman 1d with constant measurement uncertainty and no process noise plot" style="width: 80%; max-width: 900px" src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-without-process-noise-plot.png">


## Constant Measurement Uncertainty, Constant Process Noise

Below is the proof relies on setting initial value of Kalman variance ```P0``` such that ```Pk``` becomes constant for recursive equation to match exponential moving average equation.

<img alt="Proof Kalman 1d with constant measurement uncertainty and constant process noise proof" style="width: 80%; max-width: 900px" src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-with-process-noise-proof.jpg">

Plot of the convergence.

<img alt="Proof Kalman 1d with constant measurement uncertainty and constant process noise plot" style="width: 80%; max-width: 900px" src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-with-process-noise-plot.png">


# References
- [R. E. Kalman. 1960.  https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf)
- [Kalman filter in one dimension](https://www.kalmanfilter.net/kalman1d.html)
- [A First Look at the Kalman Filter](https://lectures.quantecon.org/py/kalman.html)


# Appendix

## Example Implementation

Below is simplistic implementation used to generate plots presented.
```python
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


r = 1
q = 0
p = 1
m = 1
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

plt.plot(ms, label='kalman filter')
plt.plot(cumulative_avg, label='cumulative avg')
plt.plot(exponential_avg, label='exponential moving avg')
plt.legend()
plt.show()
```
