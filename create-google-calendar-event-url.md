---
layout: post
title: "Create Google Calendar Event URL"
date: 2023-10-23
description: "Share your event to GCal users in seconds without using it yourself."
image: /images/twitter-bullet-points.png
last_modified_at: 2022-04-25
---


<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.28/moment-timezone-with-data.min.js"></script>

<h2>Create Google Calendar Event Link</h2>

<form id="calendarEvent">
  <label for="event_name">Event Name:</label><br>
  <input type="text" id="event_name" name="event_name" value=""><br>

  <label for="date_time_from">Start Date & Time:</label><br>
  <input type="datetime-local" id="date_time_from" name="date_time_from"><br>

  <label for="date_time_to">End Date & Time:</label><br>
  <input type="datetime-local" id="date_time_to" name="date_time_to"><br><br>

  <label for="timezone">Time Zone:</label><br>
  <select id="timezone">
  </select><br><br>

  <label for="url">Google Calendar URL:</label><br>
  <input type="text" id="url" name="url" value="" disabled><br>

</form>

<button type="button" onclick="copyTextUrl()">Copy 🔗</button><br><br>
<button type="button" id="goToLink">Go to link</button>

<p>Click the "Go to link" after you have filled out the event details to navigate to the google calendar page, or click the copy button to copy the URL!</p>

<script>

// Pre-fill date and time fields
var currentDate = moment().add(1, 'days').startOf('day').add(8, 'hours'); // set time to 8am tomorrow

// Format the date & time according to HTML datetime-local input requirements and users local time zone
var formattedStart = currentDate.format("YYYY-MM-DDTHH:mm");
var formattedEnd = currentDate.add(2, 'hours').format("YYYY-MM-DDTHH:mm");

document.getElementById('date_time_from').value = formattedStart;
document.getElementById('date_time_to').value = formattedEnd;

// Populate timezone dropdown with IANA time zones and their standard text labels
var tzSelect = document.getElementById('timezone');
var timeZones = moment.tz.names();
for (var i = 0; i < timeZones.length; i++) {
    var opt = document.createElement('option');
    opt.value = timeZones[i];
    opt.innerHTML = timeZones[i];
    tzSelect.appendChild(opt);
}

// Set default timezone
tzSelect.value = moment.tz.guess();

document.getElementById("goToLink").addEventListener("submit", function(event){
  event.preventDefault();

  var calendar_url = createLink()

  window.open(calendar_url, '_blank');
});

function createLink(){
  var name = document.getElementById('event_name').value;
  var startTime = document.getElementById('date_time_from').value;
  var endTime = document.getElementById('date_time_to').value;

  var calendar_url = 'https://calendar.google.com/calendar/u/0/r/eventedit?';
  calendar_url += 'text='+encodeURIComponent(name);

  var timezone = document.getElementById('timezone').value;
  formattedStart = moment.tz(startTime, timezone).format('YYYYMMDD[T]HHmmssZ');
  formattedEnd = moment.tz(endTime, timezone).format('YYYYMMDD[T]HHmmssZ');
  calendar_url += '&dates=' + formattedStart + '/' + formattedEnd;
  calendar_url += '&ctz=' + timezone;

  document.getElementById('url').value = calendar_url;

  return calendar_url;
}

async function copyTextUrl() {
  var copyText = document.getElementById("url").value;
  await copyToClipboard(copyText);
}

async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        console.log('Text copied to clipboard');
    } catch (err) {
        console.log('Error in copying text: ', err);
    }
}

document.getElementById('calendarEvent').addEventListener('input', function () {
    createLink();
});
</script>
