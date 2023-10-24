---
layout: post
title: "Create Your Google Calendar Event Link in Seconds"
date: 2023-10-23
description: "Share events with Your participants seamlessly without using Google Calendar yourself."
permalink: create-your-google-calendar-event-link-in-seconds
categories: tool
redirect_from: 
  - tool/create-your-google-calendar-event-link-in-seconds
  - create-your-google-calendar-event-link-in-seconds.html
last_modified_at: 2023-10-23
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.28/moment-timezone-with-data.min.js"></script>

Create and share a Google Calendar event link in no time, irrespective of whether or not you have a Google Calendar account. With this tool, you can seamlessly generate a URL for your event and share it with participants. All they need to do after that is to click on the link to add the event to their respective Google Calendars. 

### Key Features:

- No Google Calendar Account Required: With our tool, there’s no need for you to have a Google Calendar account yourself. Simply fill up the form and generate a URL for your event in seconds. 

- Streamlined Calendar Addition for Participants: Once you share the link with your participants, they can add the event to their calendars with just a click. 

- Better Event Recall for Attendees: With the event securely added to their calendars, attendees can keep track of it easily, reducing the risk of forgetting about it.

### How to Use the Event Link Creator?

1. All you need to do is fill out the given form, which comprises fields for the event name, start and end times, and time zone.

2. Then copy the event URL or go directly to the link by clicking on the respective buttons. 

3. Double-check your timezone settings and test the URL with someone.

4. Message me to request more features or report bugs. 

### Start Now
Get started now, and save your time, as well as that of your participants, with our Google Calendar Event Link Creator. Share events and schedules quickly and efficiently, and make sure that all your attendees mark their calendars without fail. Happy event planning!

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

  <label for="url">Your Google Calendar URL Link:</label><br>
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
