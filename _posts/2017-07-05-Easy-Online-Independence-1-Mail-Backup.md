---
layout: post
title: "Easy Online Independence: 1. Mail Backup"
date: 2017-07-05
---

This is first post of a series called "Easy Online Independence" aiming to provide cheap and easy way to increase your independence from current online service giants like Google and Facebook. By independence I mean ability to at any time to stand alone or migrate to another service without major losses.
 
## Mail Backup

Do you wonder what would happen if your mail provider decided to discontinue your service and delete all your mails? Paying or not for the service would you really have any way to restore your messages?

Fortunately there is an easy way to prevent these issues and stand more independently. Steps below are focused on Linux, but you should be able to do the same on other platforms.

### mbsync (Post Update)

Based on a suggestion from a Redditor, I have migrated to this option and updated this post. 
These steps are based on [Arch Linux Wiki](https://wiki.archlinux.org/index.php/Isync) and an older article [GMail IMAP Backup With mbsync on Ubuntu](https://chrisstreeter.com/archive/2009/04/gmail-imap-backup-with-mbsync-on-ubuntu.html).
- Make sure you are using home folder encryption to avoid leaking your mail.
- Create an special password only for mail backup. Google calls these passwords "app passwords".
- Install GPG2 to use as password manager: ```sudo apt-get install gpg2```
- Generate key: ```gpg2 --quick-gen-key gmail```
- Encrypt your password by typing it to console followed by enter after executing: ```read pass; echo $pass |gpg2 -e -r gmail -o ~/mbsync/gmail.gpg```
- Test password manager password-less decryption: ```gpg2 -q --for-your-eyes-only --no-tty -d ~/mbsync/gmail.gpg```
- Install mbsync (older name: isync) ```sudo apt-get install isync```.
- Create mail directories ```mkdir -p ~/mbsync/gmail/```
- Configure mbsync ```vi ~/.mbsyncrc```

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

- Run first sync ```mbsync gmail```.
- Configure incremental backups every 15 mins:
  -  ```crontab -e```
  -  ```0,15,30,45 * * * * mbsync gmail```

### Thunderbird
You can use Thunderbird: 
- To Avoid having to be logged into your service in your browser, which makes giant's tracking easier.  
- For ability to use offline mail. 
- For provider agnostic gui


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
