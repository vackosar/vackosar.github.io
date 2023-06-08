---
layout: post
title: 'Easy Online Independence: Mail Backup, File Synchronization'
date: 2017-07-05
description: Cheap way to increase your independence from the online giants with Syncthing, mbsync, Thunderbird.
categories: software
permalink: /:categories/:title
redirect_from:
- /2017/07/05/Easy-Online-Independence-1-Mail-Backup.html
my_related_post_paths:
- _posts/2017-12-25-Cheap-And-Tiny-Walking-Desk.md
- _posts/2018-02-25-Creating-Custom-Ubuntu-Web-Link-App.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2016-07-03-GitFlow-Incremental-Builder.md
- _posts/2016-12-26-Flite-Vs-Festival-Vs-Pico2Wave.md
- _posts/2017-02-26-$15-Ebay-USB-Microscope.md
- _posts/2021-07-01-Quilt-data-versioning-review-how-to.md
---



By independence, I mean ability to at any time to stand alone or migrate to another service without major losses.
 
## Mail Backup

Do you wonder what would happen if your mail provider decided to discontinue your service and delete all your mails? Paying or not for the service would you really have any way to restore your messages?

Fortunately there is an easy way to prevent these issues and stand more independently. Steps below are focused on Linux, but you should be able to do the same on other platforms.

### mbsync (Post Update)

Based on a suggestion from a Redditor, I have migrated to this option and updated this post. 
These steps are based on [Arch Linux Wiki](https://wiki.archlinux.org/index.php/Isync) and an older article [GMail IMAP Backup With mbsync on Ubuntu](https://chrisstreeter.com/archive/2009/04/gmail-imap-backup-with-mbsync-on-ubuntu.html).
- Make sure you are using home folder encryption to avoid leaking your mail.
- Create an special password only for mail backup. Google calls these passwords "app passwords".
- Install GPG2 (or plain gpg) to use as password manager: ```sudo apt-get install gpg2```
- Install mbsync (older name: isync): ```sudo apt-get install isync```.
- Generate key: ```gpg2 --quick-gen-key gmail```
- Create mail backup directory: ```mkdir ~/mbsync```
- Encrypt your password by typing it to console followed by enter after executing: ```read pass; echo $pass |gpg2 -e -r gmail -o ~/mbsync/gmail.gpg```
- Test password manager password-less decryption: ```gpg2 -q --for-your-eyes-only --no-tty -d ~/mbsync/gmail.gpg```
- Create mail directories: ```mkdir -p ~/mbsync/gmail/```
- Configure mbsync: ```vi ~/.mbsyncrc```

```
    IMAPAccount gmail
    Host imap.gmail.com
    User <your username>@gmail.com
    SSLType IMAPS
    PassCmd "gpg2 -q --for-your-eyes-only --no-tty -d ~/mbsync/gmail.gpg"

    IMAPStore gmail-remote
    Account gmail

    MaildirStore gmail-local
    Path ~/mbsync/gmail/
    Inbox ~/mbsync/gmail/Inbox

    Channel gmail
    Master :gmail-remote:
    Slave :gmail-local:
    # Exclude everything under the internal [Gmail] folder, except the interesting folders
    Patterns * ![Gmail]* "[Gmail]/Sent Mail" "[Gmail]/Starred" "[Gmail]/All Mail"
    Create Slave
    Sync PullNew
    SyncState *
```

- Run first sync: ```mbsync gmail```.
- Configure incremental backups every 15 mins with extra logging:
  -  ```crontab -e```
  -  ```0,15,30,45 * * * * log="/home/vackosar/mbsync/gmail.log" && { echo "$(date) Starting" && mbsync gmail && echo "$(date) Exiting"; } 1>>"$log" 2>>"$log"```

### Thunderbird
You can use [Thunderbird](https://www.thunderbird.net/) to: 
- avoid being logged in making the giant's tracking easier
- offline mail - read you mail without a connection!
- provider agnostic gui
- backup via manual export to a ZIP file with [ImportExportTools NG addon](https://addons.thunderbird.net/en-us/thunderbird/addon/importexporttools-ng/)


### Win Alternative: IMAPSize Backup (Original Post)

This alternative uses a program running also on Windows. It however uses worse format for email ".eml" and doesn't have other features.

- Download [IMAPSize](http://www.broobles.com/imapsize/imap-backup.php) win binaries.
- Copy extracted imapsize into your home folder subdirectory ```mkdir ~/imapsize/```.
- Make sure you are using home folder encryption to avoid leaking data.
- Install Wine: ```sudo apt-get install wine ```
- Start and configure imapsize for your provider ```wine imapsize.exe```. Gmail instructions can be found [here](https://support.google.com/mail/answer/7126229?hl=en).
- Start first backup using imapsize gui.
- Configure periodic incremental backups using cron:
  -  ```crontab -e```
  -  ```0 21 * * * cd ~/imapsize && wine imapsize -backup -account=gmail```


### File Sync That Supports Android!
[Syncthing](https://syncthing.net/) is a easy to set up self-hosted file synchronization tool similar to Dropbox, but with more options and distributed in its nature.
Syncthing does not do you backups for you. Have your servers distributed geographically or keep a cold backup somewhere else to avoid loss of data. 

#### Syncthing On Linux
On a Linux e.g. debian Raspberry Pi or Ubuntu the installation process is: 
1. install the package `sudo apt install syncthing`
2. set up the automatic startup
3. connect or create a new synced folder
4. configure your sync preferences

#### Syncthing via the App
You definitely should sync a folder to your phone.
ICloud can do this apparently, but to keep your files yours you can use Syncthing.
You don't need to sync huge files, but some small once you definitely should.
Syncthing is now available also [for Android on F-Droid](https://syncthing.net/downloads/), which seems to be very simple to install.
I need to try, so far I use Syncthing via Termux package below.


##### Syncthing on Android with Termux
This options doesn't have options to download only on Wi-Fi.
In Termux the setup is almost the same as in general Linux,
except you will miss your glorious keyboard from your Desktop.

Steps:
1. install [Termux Android app from F-Droid](https://f-droid.org/en/packages/com.termux/). Do not install from Google Play the package there is not maintained anymore.
2. configure connection to your SD card storage so that you can access your files from there
3. connect your keyboard or install [Hacker Keyboard from F-Droid](https://f-droid.org/en/packages/org.pocketworkstation.pckeyboard/)
4. `pkg install syncthing` 
5. setup startup into the background on the Termux app open 
6. link the folders to the SD card where you can access them on demand in the other apps