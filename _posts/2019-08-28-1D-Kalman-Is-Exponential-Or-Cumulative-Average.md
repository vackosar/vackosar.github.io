---
layout: post
title: "Constant 1D Kalman Filter Is Exponential Or Cumulative Average"
date: 2019-08-28
last_modified_at: 2022-08-27
categories: ml
description: In one dimension and with constant measurement uncertainty and process noise, the filter converges to cumulative average or exponential average.
permalink: /:categories/:title
image: /images/2019-08-28-kalman-1d-without-process-noise-proof.jpg
redirect_from:
  - /2019/08/28/1D-Kalman-Is-Exponential-Or-Cumulative-Average.html
todo: "example implementation"
note: https://www.kalmanfilter.net/kalman1d.html
---

{% include highlight-rouge-friendly.css.html %}
{% include mathjax.html %}

Kalman filter [(Kalman 1960 paper)](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf) also known as linear quadratic estimation (LQE) is an iterative algorithm that uses noisy measurements to estimate values and variance of unknown variables.
The Kalman filter allows combination of two estimates for a variable: the transition model (e.g. momentum of physical particle) and estimated variance of sensor measurement (outside-the-model measurement uncertainty) to achieve better precision.
In other words, we use the knowledge of the "physics" of the process to predict the future position and then combine that with actual sensor measurement. This gives us higher precision. Additionally, the model can incorporate "control-input", but that will be omitted from below.


The state estimate for time \\( k \\) is: \\( x_{k} \\).

The model has the following components:

- the state-transition model (motion model), which maps from previous step to the current estimate: \\( F_k \\)
- the process noise normal variance, which adds the noise of the transition model \\(Q_k \\)
- These two give us the motion estimate: \\( x_k = F_k x_{k-1} + w_k \\)
 
- the observation model, which maps from the current sensor outputs to the estimate: \\( H_k \\)
- the observation noise normal variance, which adds the noise of the sensor outputs: \\( R_k \\)
- These two give us the observation estimate: \\( z_k = H_k x_{k-1} + v_k \\)

The equations are rather complicated, please read the sources, but for short:
- Both estimates are combined: \\( \hat{ x_{k \| k} } = (1 - K_k H_k) \hat{x_{k \| k-1}} + K_k (H_k x_k + v_k) \\)
- With a variance: \\( P_{k \| k} = (1 - K_k H_k) P_{k \| k-1} \\)
- A matrix called Kalman gain: \\( K_k = P_{k\|k-1} H_k^{\intercal} (H_k P_{k\|k-1} H_k^\intercal + R_k)^{-1}  \\)



Kalman filter can be used in to keep a system in a state of control. Read more about [application of Kalman filter in PID Controller](/ml/PID-controller-control-loop-mechanism).

To what Kalman Filter reduces in a single dimension? Let's find out.


## Kalman Filter vs Exponential Average vs Cumulative Average
This blog post proves that [Kalman filter](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf) in 1D with constant measurement uncertainty and process noise asymptotically behaves as:

 - cumulative average in case of zero process noise
 - exponential average in case of non zero process noise
 
The proof relies on Kalman filter asymptotically doesn't depend on initial state. In general since Kalman filter equations are differentiable, it is reasonable to expect that above could be generalized to nearly-constant uncertainty and process noise.


### Constant Measurement Uncertainty, No Process Noise

Below is the proof relies on good choice of initial value of Kalman variance `P0` to simplify recursive equation to match cumulative average equation.

<img alt="Proof Kalman 1d with constant measurement uncertainty and no process noise proof" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-without-process-noise-proof.jpg">

Plot of the convergence.

<img alt="Proof Kalman 1d with constant measurement uncertainty and no process noise plot" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-without-process-noise-plot.png">


### Constant Measurement Uncertainty, Constant Process Noise

Below is the proof relies on setting initial value of Kalman variance `P0` such that `Pk` becomes constant for recursive equation to match exponential moving average equation.

<img alt="Proof Kalman 1d with constant measurement uncertainty and constant process noise proof" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-with-process-noise-proof.jpg">

Plot of the convergence.

<img alt="Proof Kalman 1d with constant measurement uncertainty and constant process noise plot" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-with-process-noise-plot.png">


### Example Implementation

Below is simplistic implementation of Kalman filter in one dimension in Python used to generate plots presented above.

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


# configuration of the Kalman filter
r = 1
q = 0
p = 1
m = 1

# xs is the measure input with noise
xs = []

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
