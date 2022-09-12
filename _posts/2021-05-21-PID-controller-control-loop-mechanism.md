---
layout: post
title: 'PID Controller: A Simple Control Loop Mechanism'
date: 2021-05-21
categories: ml
video: x6sxKHrPA2A
image: /images/pid-controller.webp
description: "Proportional\u2013integral\u2013derivative controller calculates feedback to reduce the error in the next step."
permalink: /:categories/:title
redirect_from:
- /ml/PID-controller
my_related_post_paths:
- _posts/2019-08-28-1D-Kalman-Is-Exponential-Or-Cumulative-Average.md
- _posts/2021-01-02-Feed-Forward-Self-Attendion-Key-Value-Memory.md
- _posts/2022-02-26-SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2016-11-04-Drone-Hackathoning.md
---



{% include load_video.html %}
{% include mathjax.html %}


### When to use PID controller?
- measured value (__process variable__) is a time series
- ideal value (__setpoint__) is known
- can correct via a __feedback__ in the next steps
- tuning (training) data is available
- cannot model of the process
- in non-linear systems may not work
- example: cruise control
  - process variable = speed
  - setpoint = ideal speed
  - error = ideal speed - actual speed
  - feedback = gas pedal


### What is PID controller?
- is sometimes called three-term controller
- tool to stay close to the ideal (__control loop mechanism__)
- uses distance from setpoint (__error__) to produce feedback
  - error = setpoint - process variable
- defined as sum of 3 terms:
  - proportional term
    - current error
    - corrects for error in the previous step
  - integral term
    - sum of errors till now
    - corrects for error in the same direction in the past
  - derivative
    - current derivative of the error
    - can cause instability and not used often
    - or low pass filtering
    - corrects for sudden change in error
- mathematical form:
  - error: \\( e(t) \\)
  - proportional coefficient: \\( K_p \\)
  - integral coefficient: \\( K_i \\)
  - derivative coefficient: \\( K_d \\)
  - time: \\( t \\)
  - feedback value (__control function__): \\( u(t) \\)
  - equation: \\( u(t) = K_p e(t) + K_i \int_0^t e(t) dt + K_d \frac{de(t)}{dt} \\)

### Demo
- grey dots represent setpoint
  - here: constantly zero
- blue represents original process variable
  - uncontrolled process variable
- red represents process variable after corrective feedback
  - here: process variable minus feedback
- try changing the input function
- Find the demo source below

<input type="checkbox" id="configFunc" />&nbsp; sine input function<br>
Kp: <input type="number" id="configKp" /><br>
Kd: <input type="number" id="configKd" /><br>
Ki: <input type="number" id="configKi" /><br>
<canvas id="canvas" width="500" height="150"></canvas>

### [Self-tuning PID using Kalman filter](https://www.sciencedirect.com/science/article/pii/S2405896318304282)
  - [Kalman filter](/ml/1D-Kalman-Is-Exponential-Or-Cumulative-Average) uses linear relationship between measured values
  - to estimate true values and uncertainty
  - in the paper relationship between the PID parameters defines the Kalman filter tuning

### Links to Related Sites
- [HN Discussion](https://news.ycombinator.com/item?id=27318942) of this post
- [PID Without a PhD](https://www.wescottdesign.com/articles/pid/pidWithoutAPhd.pdf) for more details on PID

### Demo Source Code
<textarea id="codeBlock" style="font-size: 10px;" rows="20" cols="80"></textarea>

<script type="application/javascript" id="jsCode">
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
      let new_value = config.func(t++);
      values.shift();
      values.push(new_value);

      let prev_error = - correctedValues[correctedValues.length - 1];
      let second_prev_error = - correctedValues[correctedValues.length - 2];
      let derivative = prev_error - second_prev_error;
      integral = integral + prev_error;
      let correction = prev_error * config.kp + derivative * config.kd + integral * config.ki;
      let correctedValue = new_value + correction;
      correctedValues.shift();
      correctedValues.push(correctedValue);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'grey';
      values.forEach((value, i) => {
        ctx.fillRect(i * pix_size, y_middle + 0 * pix_size, pix_size / 2, pix_size / 2);
      });

      ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
      values.forEach((value, i) => {
        ctx.fillRect(i * pix_size, y_middle + value * pix_size, pix_size, pix_size);
      });

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

document.getElementById('configFunc').addEventListener('change', e => {
  if (e.srcElement.checked) {
    config.func = sin;
  } else {
    config.func = steps;
  }
});


['p', 'i', 'd'].forEach(varname => {
  document.getElementById('configK' + varname).value = config['k' + varname];
  document.getElementById('configK' + varname).addEventListener('keyup', e => {
    let v = +e.srcElement.value;
    if (typeof(v) === 'number') {
      config['k' + varname] = e.srcElement.value;
    }
  });
});

let jsCode = document.createTextNode(document.getElementById('jsCode').innerText);
document.getElementById('codeBlock').appendChild(jsCode);

</script>
