---
layout: post
title: "Obsolete Branch Remover"
date: 2016-07-22
---

Having many branches left behind, abandoned, never deleted? How do you deal with them? We had same problem and I developed a automated DevOps solution.

Obsolete branch occurs, when dev doesn't delete branch and forgets about it. Obviously simplest obsolete branches to remove are the merged branches. Those don't contain any commits, that would be missing on develop or master branch. Unmerged branches contain extra commits both in repository and on devs local. If dev don't cares about them for long than the commits are probably not as valuable. Also common branch moved on and dev probably forgot most of the business knowledge. Thus common repository should not be burdened with such obsolete branches.

Using above reasoning I've implemented [git-obsolete-branch-removal](https://github.com/vackosar/git-obsolete-branch-remover) to provide automatic removal of obsolete branches and we were happy ever after.