---
layout: default
title: When is the end of this quarter?
description: How many days left in the quarter, the current calendar quarter-end date, and live quarter clock. What is the current quarter?
redirect_from: 
  - independent/when-is-the-end-of-current-quarter.html
---

[comment]: <> (permalink: /when-is-the-end-of-current-quarter)

<h1>{{ page.title }}</h1>
<small><i>{{ page.description }}</i></small>
<small>When is the end of the quarter?</small>
<small>When does this quarter ends?</small>
<small>When is quarter-end?</small>

The current quarter <b id='quarterName'>Q1</b> ends on <b id='quarterEnd'>Mar 31</b> in <b id="daysLeft">45</b> days (<b id="bizDaysLeft">20</b> business days).
<br>

How many days left in this quarter? There are <b id="daysLeft2">45</b> days left in this quarter.<br>
How many business days till the end of this quarter? There are <b id="bizDaysLeft2">45</b> business days till the end of current quarter.
There are <b id="daysYearLeft">183</b> days left in this year.

What quarter are we in? The current quarter is <b id='quarterName2'>Q1</b>.

<style>

#clockContainer {
    position: relative;
    margin: auto;
    width: 250px;
    height: 250px;
    background: url(/images/quarters.svg) no-repeat;
    background-size: 100%;
}
  
#clockArrow {
    position: absolute;
    color: red;
    border-radius: 10px;
    transform-origin: left;
    opacity: 0.8;
    width: 40%;
    left: 50%;
    top: 45%;
}
</style>

<figure class="figure">
    <div id="clockContainer" class="figure-img img-fluid rounded">
      <svg id="clockArrow" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 100" alt>
        <title>Clock arrow</title>
        <defs>
          <marker id="arrowhead" markerWidth="10" markerHeight="7" 
            refX="0" refY="3.5" orient="auto" stroke="red" fill="red">
            <polygon points="0 0, 10 3.5, 0 7" />
          </marker>
        </defs>
        <line x1="0" y1="50" x2="250" y2="50" stroke="red" 
        stroke-width="8" marker-end="url(#arrowhead)" />
      </svg>
    </div>
    <figcaption class="figure-caption">Quarter clock shows calendar year broken into quarters and their months. Red arrow shows current day.</figcaption>
</figure>

<h3>When do calendar quarters start and end?</h3>
<p>What calendar quarter means? A year is divided into 4 quarters: Q1, Q2, Q3, Q4. Each quarter has 3 months.
Each quarter is approximately 91 days long.
Quarterly means once every quarter, which is approximately each 91 days.</p>

<p>See a handy table of calendar quarter start dates (first days) and end dates (last days) below. The dates are the same for each year (2021, 2022, 2023, ...).</p>

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
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Q1</td>
            <td>Jan 1</td>
            <td>Mar 31</td>
            <td>Q1 starts on Jan 1 and ends on Mar 31.</td>
        </tr>
        <tr>
            <td>Q2</td>
            <td>Apr 1</td>
            <td>Jun 30</td>
            <td>Q2 starts on April 1st and ends on June 30th.</td>
        </tr>
        <tr>
            <td>Q3</td>
            <td>Jul 01</td>
            <td>Sep 30</td>
            <td>Q3 starts on July 1st and ends on September 30th.</td>
        </tr>
        <tr>
            <td>Q4</td>
            <td>Oct 1</td>
            <td>Dec 31</td>
            <td>Q4 starts on October 1st and ends on December 31th.</td>
        </tr>
    </tbody>
</table>

<h3>Fiscal Year</h3>
<p>
  Each company or government institution can choose their own fiscal (financial) year, a twelve-month period, that is the most suitable to their yearly revenue cycle.
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
<h3>Fiscal Quarters</h3>

<p>
A company fiscal year outlines its fiscal (financial) quarters dates.
That means that fiscal quarters and quarter reporting dates may be different for each company.
But usually they fall at the end of the months and don't cut through them.
Fiscal or financial quarter takes 3 months, so is approximately 91 days long.
</p>

<h3>Historical Origin of Calendar Quarters</h3>
<p>
Calendar quarters approximately match 4 seasons.
Calendar quarters divides approximately match 2 equinox and 2 solstice days, when the plane of Earth's equator maximally aligns or excurses with the center of the Sun's disk (ecliptic).
</p>

<h3>Request Notifications or Other Features</h3>
Would you like to receive notifications or other features?
Or do you need to consult on topic of software developement or machine learning?
Contact me with button below.

<a class="btn btn-success m-1" style="text-decoration: none;" href="https://us3.list-manage.com/contact-form?u=289873d7958b1bdc1c6dc93b7&form_id=3b80462ee1d82c5a36e447efbfdbe72a">Consult with Vaclav</a>

Do you need [copy and paste bullet points to your Tweets or other places? Grab some here.](twitter-bullet-points-to-copy-paste.md)


<script>
    // set values
    document.getElementById('quarterName').innerText = 'Q' + getQuarter().toString();
    document.getElementById('quarterName2').innerText = 'Q' + getQuarter().toString();
    document.getElementById('quarterEnd').innerText = getQEnd().toLocaleDateString();
    document.getElementById('daysLeft').innerText = daysLeftInQuarter().toString();
    document.getElementById('daysLeft2').innerText = daysLeftInQuarter().toString();
    // document.getElementById('daysLeft3').innerText = daysLeftInQuarter().toString();
    document.getElementById('bizDaysLeft').innerText = getBizDaysLeftInQuarter().toString();
    document.getElementById('bizDaysLeft2').innerText = getBizDaysLeftInQuarter().toString();
    document.getElementById('daysYearLeft').innerText = daysLeftInYear().toString();
daysLeftInYear();


    // set clock
    var dt = new Date();
    var current = new Date(dt.getTime());
    var previous = new Date(dt.getFullYear(), 0, 1);
    var full = new Date(dt.getFullYear() + 1, 0, 1) - previous;
    var arrow_rotation = (current - previous) / full * 360 - 90;
    document.getElementById('clockArrow').style.transform = `rotate(${arrow_rotation}deg)`;

    
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

    function getBizDaysLeftInQuarter(d) {
      d = d || new Date();
      var qEnd = getQEnd(d);
      return getBusinessDatesCount(d, qEnd);
    }

    function getBusinessDatesCount(startDate, endDate) {
        let count = 0;
        const curDate = new Date(startDate.getTime());
        while (curDate <= endDate) {
            const dayOfWeek = curDate.getDay();
            if(dayOfWeek !== 0 && dayOfWeek !== 6) count++;
            curDate.setDate(curDate.getDate() + 1);
        }
        return count;
    }

    function daysLeftInYear(d) {

      d = d || new Date();
      var yEnd = new Date(d);
      yEnd.setMonth(0, 1);
      yEnd.setFullYear(yEnd.getFullYear() + 1)
      yEnd.setHours(0);
      yEnd.setMinutes(0);
      yEnd.setSeconds(0);

      return Math.floor((yEnd - d) / 8.64e7) + 1;
    }

</script>
