---
layout: post
title: "Easy Online Independence: 1. Mail Backup"
date: 2017-07-05
---

This is first post of a series called "Easy Online Independence" aiming to provide cheap and easy way to increase your independence from current online service giants like Google and Facebook. By independence I mean ability to at any time to stand alone or migrate to another service without major losses.
 
## Mail Backup

Do you wonder what would happen if your mail provider decided to discontinue your service and delete all your mails? Paying or not for the service would you really have any way to restore your messages?

Fortunately there is an easy way to prevent these issues and stand more independently. Steps below are focused on Linux, but you should be able to do the same on other platforms.

### IMAPSize Backup

- Download [IMAPSize](http://www.broobles.com/imapsize/imap-backup.php) win binaries.
- Copy extracted imapsize into your home folder subdirectory ```mkdir ~/imapsize/```.
- Make sure you are using home folder encryption to avoid leaking data.
- Install Wine: ```sudo apt-get install wine ```
- Start and configure imapsize for your provider ```wine imapsize.exe```. Gmail instructions can be found [here](https://support.google.com/mail/answer/7126229?hl=en).
- Start first backup using imapsize gui.
- Configure periodic incremental backups using cron:
  -  ```crontab -e```
  -  ```0 21 * * * cd ~/imapsize && wine imapsize -backup -account=gmail```

### Thunderbird
You can use Thunderbird: 
- To Avoid having to be logged into your service in your browser, which makes giant's tracking easier.  
- For ability to use offline mail. 
- For provider agnostic gui

