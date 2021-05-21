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
- have measured value (process variable) is a time series
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



<input type="checkbox" id="pidOn" /> PID on / off<br>
<input type="checkbox" id="func" /> Sinus / Steps<br>
<canvas id="canvas" width="500" height="150"></canvas>

<script type="application/javascript">
let config = {amplitude: 5, period: 60, pid: false, kp: 0.2, kd: 0, ki: 0.5, func: sin};

function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    let ctx = canvas.getContext('2d');
    let y_middle = canvas.height / 2;
    config.amplitude = y_middle / 4;
    let pix_size = Math.max(Math.min(canvas.width / 50, canvas.height / 50), 1);
    let len = Math.floor(canvas.width / pix_size);
    let values = new Array(len).fill(0);
    let t = 0;
    function tick() {
      values.shift();
      let correction = 0;
      if (config.pid) {
        let prev_error = values[values.length - 1];
        let second_prev_error = values[values.length - 2];
        let derivative = prev_error - second_prev_error;
        let integral = values.reduce((a, b) => a + b, 0)
        correction = prev_error * config.kp + derivative * config.kd + integral * config.ki;
      }
      let new_value = config.func(t++) - correction;
      values.push(new_value);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      values.forEach((value, i) => {
        ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
        ctx.fillRect(i * pix_size, y_middle + value * pix_size, pix_size, pix_size);
      })
    }

    // ctx.fillStyle = 'rgb(200, 0, 0)';
    // ctx.fillRect(10, 10, 50, 50);
    //
    // ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
    // ctx.fillRect(30, 30, 50, 50);

    setInterval(tick, 100);
  }

}

function sin(t) {
  return Math.sin(t++ / config.period * 2 * Math.PI) * config.amplitude
}

function steps(t) {
  if (Math.sin(t++ / config.period * 2 * Math.PI) > 0) {
    return config.amplitude

  } else {
    return - config.amplitude
  }
}

window.addEventListener("load", draw);
document.getElementById('pidOn').addEventListener('change', e => {
  if (e.srcElement.checked) {
    config.pid = true;
  } else {
    config.pid = false;
  }
});

document.getElementById('func').addEventListener('change', e => {
  if (e.srcElement.checked) {
    config.func = steps;
    config.period = 100;
  } else {
    config.period = 60;
    config.func = sin;
  }
});

</script>
