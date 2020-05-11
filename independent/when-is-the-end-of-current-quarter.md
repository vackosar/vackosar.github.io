---
layout: default
title: When is the end of this quarter?
description: Information about the current quarter, when it will end, and how many days are left.
---

<h1>{{ page.title }}</h1>

<h3>Current quarter <b id='quarterName'></b> ends on <b id='quarterEnd'></b> in <b id="daysLeft"></b> days.</h3>
<br>

How many days left in this quarter? <b id="daysLeft2"></b> days.<br>

<p><img src="https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/quarters.svg" alt="quarters visualization" style="max-width: 300px"/></p>

<h3>When the quarters start and end?</h3>
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th scope="col">
                Quarter
            </th>
            <th scope="col">
                Start
            </th>
            <th scope="col">
                End
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Q1</td>
            <td>Jan 1</td>
            <td>Mar 31</td>
        </tr>
        <tr>
            <td>Q2</td>
            <td>Apr 1</td>
            <td>Jun 30</td>
        </tr>
        <tr>
            <td>Q3</td>
            <td>Jul 01</td>
            <td>Sep 30</td>
        </tr>
        <tr>
            <td>Q4</td>
            <td>Oct 1</td>
            <td>Dec 31</td>
        </tr>
    </tbody>
</table>

<br>
<br>
Not enough time to train new employees? Try <a href="https://quizrecall.com">Quizrecall training automation</a>.


<script>

    document.getElementById('quarterName').innerText = 'Q' + getQuarter().toString();
    document.getElementById('quarterEnd').innerText = getQEnd().toLocaleDateString();
    document.getElementById('daysLeft').innerText = daysLeftInQuarter().toString();
    document.getElementById('daysLeft2').innerText = daysLeftInQuarter().toString();

    function getQuarter(d) {
      d = d || new Date();
      var m = Math.floor(d.getMonth()/3) + 1;
      return m > 4? m - 4 : m;
    }
    
    function getQEnd(d) {
      d = d || new Date();
      var qEnd = new Date(d);
      qEnd.setMonth(qEnd.getMonth() + 3 - qEnd.getMonth() % 3, 0);
      qEnd.setHours(0);
      qEnd.setMinutes(0);
      qEnd.setSeconds(0);
      return qEnd;
    }
    
    function daysLeftInQuarter(d) {
      d = d || new Date();
      var qEnd = getQEnd(d);
      return Math.floor((qEnd - d) / 8.64e7);
    }
    
</script>


