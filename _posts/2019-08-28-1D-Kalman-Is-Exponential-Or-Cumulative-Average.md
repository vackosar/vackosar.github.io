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

Kalman filter [(Kalman 1960 paper)](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf) allows combination of two estimates for a variable: the transition model (e.g. momentum of physical particle) and estimated variance of sensor measurement (outside-the-model measurement uncertainty) to achieve better precision.
In other words, we use the knowledge of the "physics" of the process to predict the future position and then combine that with actual sensor measurement. This gives us higher precision. Additionally, the model can incorporate "control-input", but that will be omitted from below.
Kalman filter, also known as linear quadratic estimation (LQE), is an iterative algorithm, that uses both knowledge of the state motion and noisy measurements to estimate values and variance of unknown variables.


### State, Measurement, and State Estimate

At the time \\( k \\), let:
- the true hidden state be \\( x_k \\),
- the observed measurement be \\( z_k \\),
- the hidden state estimate be \\( m_k \\).


The model has the following components:

### State Transition Model
- the state-transition model (motion model), which maps from previous step to the current estimate: \\( F_k \\)
- the process noise normal variance, which adds the noise of the transition model \\(Q_k \\)
 
These two give us the motion estimate: \\( m_k = F_k x_{k-1} + \mathcal{N}(0, Q_k) \\)
 
### Observation Model
- the observation model, which maps from the current sensor outputs to the estimate: \\( H_k \\)
- the observation noise normal variance, which adds the noise of the sensor outputs: \\( R_k \\)

These two give us the observation estimate: \\( m_k = H_k x_{k-1} + \mathcal{N}(0, R_k) \\)

### Kalman Estimate
[Read other sources for details](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf), but in short:
- Both estimates are combined: \\( m_k = F_k m_{k-1} + K_k (z_k - H_k F_k m_{k-1}) \\)
- with a covariance: \\( P_k = (1 - K_k H_k) (F_k P_{k-1} F_k^\intercal + Q_k) \\)
- and Kalman gain: \\( K_k := (F_k P_{k-1} F_k^\intercal + Q_k) H_k^\intercal \left( H_k (F_k P_{k-1} F^\intercal_k + Q_k) H_k^\intercal + R_k \right)^{-1}  \\)


## Kalman Filter vs Exponential Average vs Cumulative Average
To what Kalman Filter reduces in a dimension 1, when \\( F_k = 1, H_k = 1, R_k = R \\), such that \\( z_k = x_k + N(0, Q_k) \\), and either no process noise ( \\( Q_k = 0 \\) ) or constant process noise ( \\( Q_k = Q \\) )?

This blog post proves that  in 1D with constant measurement uncertainty and process noise asymptotically behaves as:

 - cumulative average in case of zero process noise
 - exponential average in case of non zero process noise
 
The proof relies on Kalman filter asymptotically doesn't depend on initial state. In general since Kalman filter equations are differentiable, it is reasonable to expect that above could be generalized to nearly-constant uncertainty and process noise.


### Constant Measurement Uncertainty, No Process Noise
For the case where \\( Q = 0 \\), the proof relies on a choice of initial value of Kalman variance \\( P_1 = R \\). 

- \\( m_{k+1} = m_k + K_{k+1} (z_{k+1} - m_k) \\)
- \\( P_{k+1} = (1-K_{k+1}) P_k \\)
- \\( K_{k+1} = \frac{P_k}{P_k + R} \\)

\\( P_{k+1} = (1 - K_{k+1}) P_k = \frac{R P_k}{P_k + R} \\)

\\( P_1 := R \\), \\( P_2 = R / 2 \\), \\( P_3 = R / 3 \\), ..., \\( P_k = R / k \\)

\\( K_{k+1} = \frac{R}{k (R / k + R)} = \frac{1}{k+1} \\)

Which gives us recursive equation that match cumulative average equation:
\\( m_{k+1} = m_k + \frac{z_{k+1} - m_k}{k + 1} \\)


We can double-check above proof by plotting the convergence.

<img alt="Proof Kalman 1d with constant measurement uncertainty and no process noise plot" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-without-process-noise-plot.png">


### Constant Measurement Uncertainty, Constant Process Noise

Now we approach the case where \\( Q > 0 \\).
Below is the proof relies on setting initial value of Kalman variance \\( P_0 \\) such that \\( P_k \\) becomes constant for recursive equation to match exponential moving average equation.


- \\( m_{k+1} = m_k + K_{k+1} (z_{k+1} - m_k) \\)
- \\( P_{k+1} = (1-K_{k+1}) (P_k + Q) \\)
- \\( K_{k+1} = \frac{P_k + Q}{P_k + Q + R} \\)


\\( P_{k+1} = (1 - \frac{P_k + Q}{P_k + Q + R}) (P_k + Q) \\) \\( = \frac{P_k + Q + R - P_k - Q}{P_k + Q + R} (P_k + Q) = \frac{R (P_k + Q)}{P_k + Q + R} \\)

Let's select \\( P_0 \\), such that following holds true:

\\( P_0 = \frac{R (P_k + Q)}{P_k + Q + R} \\) \\( \iff P_0^2 + (Q+R) P_0 - RP_0 - QR = 0 \\)

Since  \\( P_0 > 0 \\) and \\( Q > 0 \\), then

\\( \implies P_0 = \frac{-Q + \sqrt{Q^2 + 4 QR}}{2} \\)

Which also leads to constant covariance and Kalman gain:

\\( P_k = P_0 \\), \\( K_{k+1} = K_1 \\)

So we get recursive equation for exponential moving average:

\\( m_{k+1} = K_1 z_{k+1} + (1-K_1) m_k \\)

Plot of the convergence to exponential moving average:

<img alt="Proof Kalman 1d with constant measurement uncertainty and constant process noise plot" style="width: 80%; max-width: 900px" src="/images/2019-08-28-kalman-1d-with-process-noise-plot.png">


## Kalman Filter Applications
Kalman filter can be used in to keep a system in a state of control.
Read more about [application of Kalman filter in PID Controller](/ml/PID-controller-control-loop-mechanism).


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
