---
layout: post
title: "Creating Custom Ubuntu Web Link App"
date: 2018-02-25
---

Say you would like to have WhatsApp on Ubuntu as a **sandboxed application**, but you cannot find any package for that. WhatsApp has a **web page**, but how to make sure that the page opens as separate application and its provider **cannot track you** on other pages or hack access to your login or history? 

Two step solution below uses Chromium browser.

*Note: If you don't need sandbox protection you can simply click in Chromium: ``` More tools -> Add to desktop```. ([Thanks Hacker News suggestor](https://news.ycombinator.com/item?id=16458165#16458634).)*

## Results

![Search](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2018-02-25-ubuntu-search-whatsapp.png)
![Taskbar](https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/2018-02-25-ubuntu-taskbar-whatsapp.png)

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
- [https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/](https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/)
- [https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty](https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty)
- [https://standards.freedesktop.org/desktop-entry-spec/latest/index.html](https://standards.freedesktop.org/desktop-entry-spec/latest/index.html)



