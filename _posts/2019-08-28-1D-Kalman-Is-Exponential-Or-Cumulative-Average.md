---
layout: post
title: "1D Kalman Is Exponential Or Cumulative Average"
date: 2019-08-28
---

# Abstract
Kalman filter [(Kalman 1960)](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf) also known as linear quadratic estimation (LQE) is an iterative algorithm that uses noisy measurements to estimate and variance of unknown variables. The Kalman filter allows incorporation of known state space behaviour (e.g. momentum of physical particle) and outside-the-model estimated variance from measurement sensors.

This blog post proves that Kalman filter in 1D with constant measurement error and process noise asymptotically behaves as:

 - cumulative average in case of zero process noise
 - exponential average in case of non zero process noise
 
The proof relies on Kalman filter asymptotically doesn't depend on initial state. In general since Kalman filter equations are differentiable, it is reasonable to expect that above could be generalized to nearly-constant error and process noise.


# Implementation

Below is simplistic implementation used to generate plots used below.
```python
r = 1
q = 2
p = 3


def current_k(p: float):
    return (p + q) / (p + q + r)


def next_p(p: float, k: float):
    return (1 - k) * (p + q)


ps = []
ks = []

for i in range(10):
    k = current_k(p)
    ks.append(k)
    p = next_p(p, k)
    ps.append(p)
```

# Proofs

## Constant Measurement Error, No Process Noise

Below is the proof relies on good choice of initial value of Kalman variance ```P0``` to simplify recursive equation to match cumulative average equation.
![Proof Kalman 1d with constant measurement error and no process noise proof](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-without-process-noise-proof.jpg)

Plot of convergence of ```Pk``` and ```K(k+1)``` to zero.
![Proof Kalman 1d with constant measurement error and no process noise plot](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-without-process-noise-plot.jpg)


## Constant Measurement Error, Constant Process Noise

Below is the proof relies on setting initial value of Kalman variance ```P0``` such that ```Pk``` becomes constant for recursive equation to match exponential moving average equation.
![Proof Kalman 1d with constant measurement error and constant process noise](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-with-process-noise-proof.jpg)

Plot of convergence of ```Pk``` and ```K(k+1)``` to non zero constant.
![Proof Kalman 1d with constant measurement error and constant process noise plot](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2019-08-28-kalman-1d-with-process-noise-plot.jpg)

# References
- [R. E. Kalman. 1960.  https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf](https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf)
- [Kalman filter in one dimension](https://www.kalmanfilter.net/kalman1d.html)
- [A First Look at the Kalman Filter](https://lectures.quantecon.org/py/kalman.html)
