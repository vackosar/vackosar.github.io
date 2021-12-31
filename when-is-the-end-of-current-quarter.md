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

<h3>When do calendar quarters start and end?</h3>
<p>A year is divided into 4 quarters: Q1, Q2, Q3, Q4. Each quarter has 3 months. Each quarter has approximately 91 days.</p>

<p><img src="/images/quarters.svg" alt="calendar year quarters visualization circular" style="max-width: 300px"/></p>

<p>See a handy table of quarter start and end dates below. The dates are the same for each year.</p>

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

<h3>Fiscal Year and Fiscal Quarters</h3>
<p>
  Each company or government institution can choose their own fiscal year, a twelve-month period, that is the most suitable to their yearly revenue cycle.
  Fiscal year can differ from calendar year.
  Companies use their fiscal years to submit financial reports, external audits, federal tax filings.
  For example Apple's fiscal year ends its fiscal year on the last Saturday of September.
  What is the fiscal year-end for Microsoft, Amazon, Google, or NVIDIA.
</p>

<table class="table table-striped">
    <thead>
        <tr>
            <th scope="col">
                Company
            </th>
            <th scope="col">
                Fiscal Year End
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Apple</td>
            <td>the last Saturday of September</td>
        </tr>
        <tr>
            <td>Microsoft</td>
            <td>the fifth Saturday of the new calendar year</td>
        </tr>
        <tr>
            <td>Amazon</td>
            <td>December 31</td>
        </tr>
        <tr>
            <td>Alphabet (Google)</td>
            <td>December 31</td>
        </tr>
        <tr>
            <td>NVIDIA</td>
            <td>January 31</td>
        </tr>
    </tbody>
</table>

<p>
A company fiscal year outlines its quarters dates.
That means that fiscal quarters and quarter reporting dates may be different for each company.
But usually they fall at the end of the months and don't cut through them.
</p>

<h3>Historical Origin of Calendar Quarters</h3>
<p>
Calendar quarters approximately match 4 seasons.
Calendar quarters divides approximately match 2 equinox and 2 solstice days, when the plane of Earth's equator maximally aligns or excurses with the center of the Sun's disk (ecliptic).
</p>

<br>
<br>
<h4>Tickerverse - Event-Driven Market Intelligence</h4>
Find new opportunities with <a href="https://tickerverse.com/">event-driven investing on Tickerverse</a>.
<div>
  <a href="https://tickerverse.com/">
    <img style="width: 200px" src="/images/tickerverse-title.svg" alt="Stay on top of important company events">
  </a>
</div>


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


