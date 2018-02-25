---
layout: post
title: "Creating Custom Ubuntu Web Link App"
date: 2018-02-25
---

Say you would like to have WhatsApp on Ubuntu as a sandboxed application, but you cannot find any package for that. WhatsApp has a web page, but how to make sure that the page opens as separate application with custom icon and has ability to track you or access your login information? Two step solution below uses Chromium browser.

## Instructions

- Create a desktop file ```whatsapp.desktop``` containing following:
```shell
[Desktop Entry]
Version=1.0
Type=Application
Name=WhatsApp
GenericName=WhatsApp
#Icon=/usr/share/icons/hicolor/scalable/whatsapp.svg
Exec=chromium-browser --class whatsapp -user-data-dir=".config/whatsapp" --app=https://web.whatsapp.com
Terminal=false
```

- Install desktop file executing:
```
sudo desktop-file-install whatsapp.desktop 
```

## Custom Icon
Download and uncomment the Icon line to have icon displayed in Ubuntu search. However, Chrome will override it with downloaded page icon upon page load.

## Firefox Support 
Similar approach can be used with Firefox except option "-P" is used instead of "--app" and "-user-data-dir" option is not needed. It involves a manual step on first startup and one cannot easily remove the tab and address bars. On the other hand it handles icons in better way.

## Others Suggested Apps

- Google Calendar
- Gmail
- Youtube
- Facebook
- Google Tasks

## Desktop File Creator Script

You can speed up the desktop file creation with following script:

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
cat - > "$name.desktop" <<END
[Desktop Entry]
Version=1.0
Type=Application
Name=$name
GenericName=$name
#Icon=/usr/share/icons/hicolor/scalable/$name.svg
Exec=chromium-browser --class $name -user-data-dir=".config/$name" --app=$url
Terminal=false
END
```

## References

- [https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/](https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/)
- [https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty](https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty)
- [https://standards.freedesktop.org/desktop-entry-spec/latest/index.html](https://standards.freedesktop.org/desktop-entry-spec/latest/index.html)

