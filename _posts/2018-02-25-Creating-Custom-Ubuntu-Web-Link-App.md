---
layout: post
title: How To Create Custom Ubuntu Web Link App
date: 2018-02-25
description: Turn any web page into an Ubuntu application and prevent the web owner from tracking you around the web.
categories: software
permalink: /:categories/:title
image: /images/2018-02-25-ubuntu-search-whatsapp.png
redirect_from:
- /2018/02/25/Creating-Custom-Ubuntu-Web-Link-App.html
my_related_post_paths:
- _posts/2017-07-05-Easy-Online-Independence-1-Mail-Backup.md
- _posts/2016-11-04-Drone-Hackathoning.md
- _posts/2016-12-26-Flite-Vs-Festival-Vs-Pico2Wave.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2023-01-24-fill-versions-from-python-environment.md
- _posts/2018-09-23-Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync.md
- _posts/2017-07-15-Restore-Missing-Punctuation-with-Keras-Convolutional-Text-Punctuator.md
---



Say you would like to have WhatsApp on Ubuntu as a **sandboxed application**, but you cannot find any package for that.
WhatsApp has a **web page**, but how to make sure that the page opens as separate application and its provider **cannot track you** on other pages or hack access to your login or history?

Two step solution below uses Chromium browser.

*Note: If you don't need sandbox protection you can simply click in Chromium: ``` More tools -> Add to desktop```. ([Thanks Hacker News suggestor](https://news.ycombinator.com/item?id=16458165#16458634).)*

## Results

![Search](/images/2018-02-25-ubuntu-search-whatsapp.png)
![Taskbar](/images/2018-02-25-ubuntu-taskbar-whatsapp.png)

## Instructions

- Create a desktop file ```whatsapp.desktop``` containing following:
```shell
[Desktop Entry]
Version=1.0
Type=Application
Name=WhatsApp
GenericName=WhatsApp
#Icon=/usr/share/icons/hicolor/scalable/whatsapp.svg
Exec=chromium-browser --class whatsapp -user-data-dir=".config/whatsapp" --app="https://web.whatsapp.com"
Terminal=false
```

- Install desktop file executing:
```
sudo desktop-file-install whatsapp.desktop 
```

*Note 1: You can also install the desktop file without admin rights for current user only: ```cp whatsapp.desktop ~/.local/share/applications/```.*

*Note 2: Do not use command above unchanged in commandline. It relies on being executed in home directory to store its profile in ```.config```. I found no easy way to add ```$HOME``` reference into a desktop file.*

## Custom Icon
Download and uncomment the Icon line to have icon displayed in Ubuntu search (launcher). However, Chrome will override Taskbar icon with the page icon upon load. This lowers your Taskbar icon resolution, but on the other hand simplifies the process.

Custom Taskbar as well as search (launcher) icons are supported on Firefox.


## Firefox Support 
Firefox has advantage in that it doesn't override your custom icon in the Taskbar, however requires manual profile creation step and manual removal of address bar.
- Replace Exec line with following:
```
Exec=firefox --class whatsapp -P whatsapp https://web.whatsapp.com
```
- Perform manual step of [creating Firefox profile](https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles) on first startup.
- Optional: [Remove the tab and address bar).](https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty)

## Other Suggested Apps

- Google Calendar
- Gmail
- Youtube
- Facebook
- Google Tasks

## Web Link App Creator Script

You can speed up the web link app creation using following script. It also creates a command into ```$HOME/bin``` such that you can add that app into startup. It takes two arguments: 
- url: Url of the app starting with https or http.
- name: Name of the app used for search and commandline.

```shell
#!/bin/sh -xue

url="$1";
if [ "$#" = "1" ]; then
	name="$(echo "$url" |sed -e 's|https://||;s|http://||;s|\.[^.]\+$||;')";
elif [ "$#" = "2" ]; then
	name="$2";
else
	echo 'Too many arguments. Usage: url [name]';
	exit 1;
fi

command="$HOME/bin/$name";
cat - > "$command" <<END
#!/bin/sh -ue
chromium-browser --class "$name" -user-data-dir="$HOME/.config/$name" --app="$url";
END
chmod u+x "$command";

desktopFile="$HOME/.local/share/applications/$name.desktop";

cat - > "$desktopFile" <<END
[Desktop Entry]
Version=1.0
Type=Application
Name=$name
GenericName=$name
#Icon="$HOME/.local/share/icons/$name.svg"
Exec="$command"
Terminal=false
END
```

## References

- [HN discussion of this post](https://news.ycombinator.com/item?id=16458165#16458634)
- [Web Link Apps on Android on F-Droid (by someone else)](https://f-droid.org/packages/com.tobykurien.webapps/)
- [Parallel project partially inspired by this post (by someone else)](https://quang.im/webcatalog)
- [https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/](https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/)
- [https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty](https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty)
- [https://standards.freedesktop.org/desktop-entry-spec/latest/index.html](https://standards.freedesktop.org/desktop-entry-spec/latest/index.html)



