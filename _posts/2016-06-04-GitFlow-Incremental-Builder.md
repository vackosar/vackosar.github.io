---
layout: post
title: "GitFlow Incremental Builder"
date: 2016-06-04
---

We had issues with our Maven builds taking too long on a project with messaging micro service architecture at Barclays. After we adopted [git feature branch model called GitFlow](http://nvie.com/posts/a-successful-git-branching-model/) and setting up pre-merge testing policy, it dawned on me that by having develop branch stability guarantee, we could speed up our builds.

Reason for ability to speed up was that most build time was spent by unit testing and most feature branches introduced changes into only a few maven modules. Thus since prior test stability was guaranteed, we could simply test only modules which were affected by introduced changes on given feature branch.

I was able to improve our build time implementing [gitflow-incremental-builder](https://github.com/vackosar/gitflow-incremental-builder). From above it is apparent that I needed access to diff develop-feature and to maven module dependency structure. Former was achieved using JGit and later using Maven Extension mechanism.

