---
layout: post
title: Create Your Google Calendar Event Link in Seconds
date: 2023-10-23
description: Fill the form or upload your ICS file to share events with Your participants without having Google Calendar yourself.
permalink: create-your-google-calendar-event-link-in-seconds
categories: tool
redirect_from:
- tool/create-your-google-calendar-event-link-in-seconds
- create-your-google-calendar-event-link-in-seconds.html
image: /images/create-google-calendar-event-link.png
last_modified_at: 2023-10-23
my_related_post_paths:
- _posts/2023-08-24-multiple-interval-averaging-stopwatch.md
- _posts/2022-02-06-twitter-bullet-points-to-copy-paste.md
- _posts/2020-05-03-when-is-the-end-of-current-quarter.md
- _posts/2018-02-25-Creating-Custom-Ubuntu-Web-Link-App.md
- _posts/2020-07-12-vr-holiday-in-nature.md
- _posts/2021-03-22-google-product-taxonomy-viewer.md
- _posts/2017-07-05-Easy-Online-Independence-1-Mail-Backup.md
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.28/moment-timezone-with-data.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/ical.js/1.5.0/ical.min.js" defer></script>



![Create Your Google Calendar Event Link in Seconds](/images/create-google-calendar-event-link.png)

Create and share a Google Calendar event link in no time, irrespective of whether you have a Google Calendar account or not. With this tool, you can seamlessly generate a URL for your event and share it with participants. All they need to do after that is to click on the link to add the event to their respective Google Calendars. 

### Key Features:

- No Google Calendar Account Required: With our tool, there’s no need for you to have a Google Calendar account yourself. Simply fill up the form and generate a URL for your event in seconds. 

- Streamlined Calendar Addition for Participants: Once you share the link with your participants, they can add the event to their calendars with just a click. 

- Better Event Recall for Attendees: With the event securely added to their calendars, attendees can keep track of it easily, reducing the risk of forgetting about it.

### How to Use the Event Link Creator?

1. All you need to do is fill out the given form, which comprises fields for the event name, start and end times, and time zone.

2. Then copy the event URL or go directly to the link by clicking on the respective buttons. 

3. Double-check your timezone settings and test the URL with someone.

4. Message me to request more features or report bugs. 


### Common Use Cases

1. Organizing Webinars or Online Training: Creators or educators can utilize this tool to share schedules of their upcoming webinars or online courses, boosting enrolment rates.

2. Scheduling Business Meetings: The tool can be used to generate Google Calendar Event Links for business meetings quickly. Participants can add the event to their calendars with a simple click, improving meeting attendance.

3. Planning Community Events: Organizations can utilize this tool to create links for community events such as fundraisers, charity runs, or social gatherings, ensuring maximum participation.


### Start Now
Get started now, and save your time, as well as that of your participants, with our Google Calendar Event Link Creator. Share events and schedules quickly and efficiently, and make sure that all your attendees mark their calendars without fail. Happy event planning!

<form id="calendarEvent" oninput="createLink()">
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

<h3>Create Event Link From iCalendar ICS File</h3>
<input type="file" id="fileUpload" onchange="parseIcs()">
<div id ="output"></div>

<script>




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


function parseIcs() {
    var fileInput = document.getElementById('fileUpload');
    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
        // Parse ICS file
        var icsFile = ICAL.parse(event.target.result.trim());
        var comp = new ICAL.Component(icsFile);
        var events = comp.getAllSubcomponents('vevent');

        // Output events to HTML
        var outputContainer = document.getElementById('output');
        outputContainer.innerHTML = '';
        var timezone = document.getElementById('timezone').value;
        index = 0;
        events.forEach(function(event) {
            var eventComp = new ICAL.Event(event);
            var listItem = document.createElement('li');

            if (index === 0) { // sets the first event to form inputs
                document.getElementById('event_name').value = eventComp.summary;
                document.getElementById('date_time_from').value = moment.tz(eventComp.startDate.toJSDate(), timezone).format('YYYY-MM-DDTHH:mm');
                document.getElementById('date_time_to').value = moment.tz(eventComp.endDate.toJSDate(), timezone).format('YYYY-MM-DDTHH:mm');
                createLink(); // we need to create the link again with the new values.
            }

            listItem.textContent = 'Event Name: ' + eventComp.summary +
                                  ', Start Time: ' + moment.tz(eventComp.startDate.toJSDate(), timezone).format() +
                                  ', End Time: ' + moment.tz(eventComp.endDate.toJSDate(), timezone).format();
            outputContainer.appendChild(listItem);
            index = index + 1;
        });
    };
    reader.onerror = function(event) {
        console.error("File could not be read! Code " + event.target.error.code);
    };

    reader.readAsText(file);
}



function onLoad() {
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
  
  document.getElementById("goToLink").addEventListener("click", function(event){
    event.preventDefault();
  
    var calendar_url = createLink()
  
    window.open(calendar_url, '_blank');
  });

}
window.addEventListener("load", onLoad);


</script>
