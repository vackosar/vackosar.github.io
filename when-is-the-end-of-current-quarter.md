---
layout: default
title: When is the end of this quarter?
description: Current calendar quarter-end date, and how many days left.
redirect_from: 
  - independent/when-is-the-end-of-current-quarter.html
---

[comment]: <> (permalink: /when-is-the-end-of-current-quarter)

<h1>{{ page.title }}</h1>
<small><i>{{ page.description }}</i></small>
<small>When is the end of the quarter?</small>
<small>When does this quarter ends?</small>
<small>When is quarter-end?</small>

Current quarter <b id='quarterName'>Q1</b> ends on <b id='quarterEnd'>Mar 31</b> in <b id="daysLeft">45</b> days.
<br>

How many days left in this quarter? There are <b id="daysLeft2">45</b> days left in this quarter.<br>
How many days till the end of this quarter? There are <b id="daysLeft3">45</b> days till the end of current quarter.<br>
What quarter are we in now? Current quarter is <b id='quarterName2'>Q1</b>.

<p><img src="/images/quarters.svg" alt="quarters visualization circular" style="max-width: 300px"/></p>
<small>A year is divided into 4 quarters. Each has 3 months.</small>

<h3>When do calendar quarters start and end?</h3>
<small>See a handy table of quarter start and end dates below. The dates are the same for each year. Each quarter has approximately 91 days.</small>

<table class="table table-striped">
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
<br>
Are your colleagues and friends isolated and not belonging?
Automate weekly one-on-one video-calls for your group to: increase belonging, support idea cross-pollination, & reduce isolation!
Try <a href="https://RandomMeets.com">RandomMeets now</a>!


<script>

    document.getElementById('quarterName').innerText = 'Q' + getQuarter().toString();
    document.getElementById('quarterName2').innerText = 'Q' + getQuarter().toString();
    document.getElementById('quarterEnd').innerText = getQEnd().toLocaleDateString();
    document.getElementById('daysLeft').innerText = daysLeftInQuarter().toString();
    document.getElementById('daysLeft2').innerText = daysLeftInQuarter().toString();
    document.getElementById('daysLeft3').innerText = daysLeftInQuarter().toString();

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
      return Math.floor((qEnd - d) / 8.64e7) + 1;
    }
    
</script>


