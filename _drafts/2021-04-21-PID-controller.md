---
layout: post
title: "PID Controller"
date: 2021-05-21
categories: ml
image: /images/pid-controller.webp
description: Proportional–integral–derivative controller produces feedback to reduce measured error in the next step.
permalink: /:categories/:title
---

{% include mathjax.html %}

<figure class="figure">
    <img
        class="figure-img img-fluid rounded"
        src="/images/pid-controller.webp"
        alt="PID controller" />
</figure>

### When to use PID controller?
- measured value (process variable) is a time series
- ideal value (setpoint) is known
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

### Demo
- grey dots represent setpoint
- blue represents unchanged output
- red represents controlled output
- try changing the input function

<input type="checkbox" id="func" />&nbsp; sine input function<br>
<canvas id="canvas" width="500" height="150"></canvas>

<script type="application/javascript">
let config = {amplitude: 5, period: 60, pid: false, kp: 0.2, kd: 0, ki: 0.5, func: steps};

function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    let ctx = canvas.getContext('2d');
    let y_middle = canvas.height / 2;
    config.amplitude = y_middle / 4;
    let pix_size = Math.max(Math.min(canvas.width / 50, canvas.height / 50), 1);
    let len = Math.floor(canvas.width / pix_size);
    let values = new Array(len).fill(0);
    let correctedValues = new Array(len).fill(0);
    let integral = correctedValues.reduce((a, b) => a + b, 0)
    let t = 0;
    function tick() {
      let new_value = config.func(t++)
      values.shift();
      values.push(new_value);

      let prev_error = correctedValues[correctedValues.length - 1];
      let second_prev_error = correctedValues[correctedValues.length - 2];
      let derivative = prev_error - second_prev_error;
      integral = integral + prev_error;
      let correction = prev_error * config.kp + derivative * config.kd + integral * config.ki;
      let correctedValue = new_value - correction;
      correctedValues.shift();
      correctedValues.push(correctedValue)



      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'grey';
      values.forEach((value, i) => {
        ctx.fillRect(i * pix_size, y_middle + 0 * pix_size, pix_size / 2, pix_size / 2);
      })

      ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
      values.forEach((value, i) => {
        ctx.fillRect(i * pix_size, y_middle + value * pix_size, pix_size, pix_size);
      })

      ctx.fillStyle = 'rgb(200, 0, 0)';
      correctedValues.forEach((value, i) => {
        ctx.fillRect(i * pix_size, y_middle + value * pix_size, pix_size, pix_size);
      })
    }

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

document.getElementById('func').addEventListener('change', e => {
  if (e.srcElement.checked) {
    config.func = sin;
  } else {
    config.func = steps;
  }
});

</script>
