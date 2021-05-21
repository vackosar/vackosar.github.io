---
layout: post
title: "PID Controller"
date: 2021-05-21
categories: ml
description: Proportional–integral–derivative controller produces feedback to reduce measured error in the next step.
permalink: /:categories/:title
---

{% include mathjax.html %}

### Where to use PID controller?
- measured value (process variable) is a time series
- there is an ideal value (setpoint)
- need to continuously correct
- can correct via a feedback
- example: cruise control
  - process variable = speed
  - setpoint = ideal speed
  - error = speed minus ideal speed
  - feedback = gas pedal
- is sometimes called three-term controller


### What is PID controller?
- tool to stay close to the ideal (control loop mechanism)
- uses distance from setpoint (error value) to produce feedback
- sum of 3 terms with respect to an error:
  - proportional
  - integral
  - derivative
- mathematical form:
  - error: \\( e(t) \\)
  - proportional coefficient: \\( K_p \\)
  - integral coefficient: \\( K_i \\)
  - derivative coefficient: \\( K_p \\)
  - time: \\( t \\)
  - feedback value: \\( u(t) \\)
  - equation: \\( u(t) = K_p e(t) + K_i \int_0^t e(t) dt + K_d \frac{de(t)}{dt} \\)


