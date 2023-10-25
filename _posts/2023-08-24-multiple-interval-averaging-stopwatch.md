---
layout: post
title: Multiple Interval Averaging Stopwatch
description: Measure multiple time intervals and get average calculated and copy data from a table.
permalink: /multi_interval_stopwatch.html
categories: tool
redirect_from:
- tool/multi_interval_stopwatch
- multi_interval_stopwatch
last_modified_at: 2023-08-24
date: 2023-08-24
image: /images/multi-interval-averaging-stopwatch.png
my_related_post_paths:
- _posts/2023-10-23-create-your-google-calendar-event-link-in-seconds.md
- _posts/2021-05-21-PID-controller-control-loop-mechanism.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2019-08-28-1D-Kalman-Is-Exponential-Or-Cumulative-Average.md
- _posts/2016-07-16-Boost-Jog-Morale-Using-Mil-Cadence.md
- _posts/2022-02-06-twitter-bullet-points-to-copy-paste.md
- _posts/2020-05-03-when-is-the-end-of-current-quarter.md
---


![Multiple Interval Averaging Stopwatch](/images/multi-interval-averaging-stopwatch.png)

<!--
# Averaging Stopwatch

Measure multiple time intervals and get average calculated and copy data from a table.

Write HTML with inlined JS script for stop watch file.
It has a current measured millisecond time, one toggle button for start and stop, one clear button.
It has a table for the time intervals in milliseconds that were measured, where each row can be edited and deleted, and average result output that is updated when the values in the table change by addition, edit, or deletion.
-->


<p>
Need to measure an average time of an event, that may be different every time, but you need to get approximate mean period? Use this tool.
</p>
<p>
This tool has a current measured millisecond time, one toggle button for start and stop, one clear button.
It has a table for the time intervals in milliseconds that were measured, where each row can be edited and deleted, and average result output that is updated when the values in the table change by addition, edit, or deletion.
</p>

<p>
<ul>
  <li>
Performance Testing: Software engineers can utilize this tool to conduct performance testing on different functions of a program by recording the execution time over multiple intervals to find average execution time.
</li>
<li>
Scientific Experiments: The stopwatch can be useful in repeated scientific experiments to measure average time taken in chemical reactions, speed of certain phenomena or other time-based observations.
</li>
<li>
Athlete Training: Coaches could use it to track and measure the average time interval an athlete takes to complete certain drills or exercises over various sessions.
</li>
</ul>
</p>


<h2>
  Current:
  <span id="time">0</span>
  ms
</h2>
<button id="start" onclick="toggleStopwatch()">Start</button>
<button id="clear" onclick="clearStopwatch()">Clear</button>

<table id="timeList">
  <tr>
    <th>Interval [ms]</th>
    <th>Action</th>
  </tr>
</table>

<h2>Average:
  <span id="average">0</span>
  ms
</h2>

<script type="text/javascript">
	let running = false;
	let startTime;
	let timeList = [];
	updateStopwatch();

	function toggleStopwatch() {
		running = !running;

		if (running) {
			document.getElementById('start').innerText = 'Stop';
			startTime = Date.now();
		} else {
			document.getElementById('start').innerText = 'Start';
			let interval = Date.now() - startTime;
			timeList.push(interval);
			addInterval(interval);
			calculateAverage();
		}
	}

	function clearStopwatch() {
		document.getElementById('time').innerText = '0';
		document.getElementById('timeList').innerHTML = '<tr><th>Interval</th><th>Action</th></tr>';
		timeList = [];
		calculateAverage();
	}

	function updateStopwatch() {
		if (running) {
			document.getElementById('time').innerText = Date.now() - startTime;
		}

		setTimeout(updateStopwatch, 10);
	}

	function addInterval(time) {
		let table = document.getElementById('timeList');
		let row = table.insertRow(-1);
		let cell1 = row.insertCell(0);
		let cell2 = row.insertCell(1);
		cell1.innerHTML = '<input type="number" value="' + time + '" onchange="updateInterval(this, ' + (table.rows.length - 2) + ')">';
		cell2.innerHTML = '<button onclick="deleteInterval(' + (table.rows.length - 2) + ')">Delete</button>';
	}

	function deleteInterval(index) {
		document.getElementById('timeList').deleteRow(index + 1);
		timeList.splice(index, 1);
		calculateAverage();
	}

	function updateInterval(input, index) {
		timeList[index] = parseInt(input.value);
		calculateAverage();
	}

	function calculateAverage() {
		let sum = timeList.reduce((a, b) => a + b, 0);
		document.getElementById('average').innerText = timeList.length ? sum / timeList.length : '0';
	}
</script>