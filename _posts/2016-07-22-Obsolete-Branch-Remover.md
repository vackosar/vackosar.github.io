---
layout: post
title: Obsolete Git Branch Remover Maven Plugin
date: 2016-07-22
categories: software
description: Having many branches left behind, abandoned, never deleted? How do you deal with them? We had same problem and I developed a automated DevOps solution.
permalink: /:categories/:title
redirect_from:
- /2016/07/22/Obsolete-Branch-Remover.html
my_related_post_paths:
- _posts/2016-07-03-GitFlow-Incremental-Builder.md
- _posts/2018-01-24-Modern-Config-Injection-In-Maven-Plugins.md
- _posts/2018-12-17-My-First-Contribution-To-Major-OSS-Project.md
- _posts/2016-11-04-Drone-Hackathoning.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2023-06-16-Forwad-Deployed-Engineer-Technical-Account-Specialist-Role.md
- _posts/2017-06-04-Code-Structure-Principles.md
---



Obsolete branch occurs, when dev doesn't delete branch and forgets about it. Obviously simplest obsolete branches to remove are the merged branches. Those doesn't contain any commits, that would be missing on develop or master branch. Unmerged branches contain extra commits both in repository and on author's local. If author doesn't care about a branch for long then the commits are probably not very valuable. Thus repository should not be burdened with such obsolete branches.

Using above reasoning I've provided [git-obsolete-branch-removal](https://github.com/vackosar/git-obsolete-branch-remover) to automatically remove obsolete branches. And we were happy ever after.