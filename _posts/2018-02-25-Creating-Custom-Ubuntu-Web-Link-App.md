---
layout: post
title: "Creating Custom Ubuntu Web Link App"
date: 2018-02-25
---

Say you would like to have WhatsApp on Ubuntu as a sandboxed application, but you cannot find any package for that. WhatsApp has a web page, but how to make sure that the page opens with separate application with custom icon and it has no access to your browsing history and cookies?

Solution is below uses Chromium Browser:


```shell
# Download PNG or SVG icon somewhere from the web.
wget https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg

# Copy the icon to proper directory.
sudo cp WhatsApp.svg /usr/share/icons/hicolor/scalable/whatsapp.svg

# Create a desktop file.
cat - > whatsapp.desktop <<END
[Desktop Entry]
Version=1.0
Type=Application
Name=WhatsApp
GenericName=WhatsApp
Icon=/usr/share/icons/hicolor/scalable/whatsapp.svg
Exec=chromium-browser --class whatsapp -user-data-dir=".config/whatsapp" --app=https://web.whatsapp.com
Terminal=false
END

# Install the desktop file.
sudo desktop-file-install whatsapp.desktop 
```

Similar approach can be used with Firefox except option "-P" is used instead of "--app" and "-user-data-dir" option is not needed. It involves a manual step on first startup and one cannot easily remove the tab and address bars. On the other hand it handles icon in better way.

## Desktop File Creator Script

```shell
url="$1"
name="$(echo "$url" |sed -e 's|https://||;s|http://||;s|\.[^.]\+$||;')"
cat - > "$name.desktop" <<END
[Desktop Entry]
Version=1.0
Type=Application
Name=$name
GenericName=$name
Icon=/usr/share/icons/hicolor/scalable/$name.svg
Exec=chromium-browser --class $name -user-data-dir=".config/$name" --app=$url
Terminal=false
END
```



## References

- [https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/](https://www.reddit.com/r/linux/comments/7ivuit/create_firefoxbased_web_apps_for_gnome_and/)
- [https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty](https://superuser.com/questions/1261660/firefox-quantum-ver-57-how-can-i-hide-the-horizontal-tab-bar-with-treesty)
- [https://standards.freedesktop.org/desktop-entry-spec/latest/index.html](https://standards.freedesktop.org/desktop-entry-spec/latest/index.html)

