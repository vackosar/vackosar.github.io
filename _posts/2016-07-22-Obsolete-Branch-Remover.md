---
layout: post
title: "Obsolete Branch Remover"
date: 2016-07-22
categories: software
description: Having many branches left behind, abandoned, never deleted? How do you deal with them? We had same problem and I developed a automated DevOps solution.
permalink: /:categories/:title
redirect_from:
- /2016/07/22/Obsolete-Branch-Remover.html
---

Obsolete branch occurs, when dev doesn't delete branch and forgets about it. Obviously simplest obsolete branches to remove are the merged branches. Those doesn't contain any commits, that would be missing on develop or master branch. Unmerged branches contain extra commits both in repository and on author's local. If author doesn't care about a branch for long then the commits are probably not very valuable. Thus repository should not be burdened with such obsolete branches.

Using above reasoning I've provided [git-obsolete-branch-removal](https://github.com/vackosar/git-obsolete-branch-remover) to automatically remove obsolete branches. And we were happy ever after.