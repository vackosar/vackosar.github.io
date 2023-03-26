---
layout: post
title: GitFlow Incremental Builder - Speed up your multi-module Maven build
date: 2016-07-03
categories: software
description: Build only modules that changed compared to the master branch, plus their dependents. Java!
permalink: /:categories/:title
image: /images/eclipse-modules.png
redirect_from:
- /2016/07/03/GitFlow-Incremental-Builder.html
my_related_post_paths:
- _posts/2018-01-24-Modern-Config-Injection-In-Maven-Plugins.md
- _posts/2016-07-22-Obsolete-Branch-Remover.md
- _posts/2018-12-17-My-First-Contribution-To-Major-OSS-Project.md
- _posts/2017-10-28-Spring-Integration-Highlights.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2016-07-28-Functional-Foreach-In-Bash.md
- _posts/2017-06-04-Code-Structure-Principles.md
---

<img title="An example of a multi-module project Eclipse JDT" alt="An example of a multi-module project Eclipse JDT" style="width: 80%; max-width: 900px" src="/images/eclipse-modules.png">

We had issues with our builds taking too long on a project with messaging microservice architecture.
After we adopted [git feature branch model called GitFlow](http://nvie.com/posts/a-successful-git-branching-model/) and setting up pre-merge testing policy, it dawned on me that by having develop branch stability guarantee, we could speed up our builds.

Reason for ability to speed up was that most build time was spent by unit testing and most feature branches introduced changes into only a few maven modules. Thus since prior test stability was guaranteed, we could simply test only modules which were affected by introduced changes on given feature branch.

I was able to improve our build time implementing [gitflow-incremental-builder](https://github.com/vackosar/gitflow-incremental-builder).
You can use it too, it is a permissive open-source plugin.
From above, it is apparent that I needed access to diff develop-feature and to maven module dependency structure. Former was achieved using JGit and later using Maven Extension mechanism.


In this project I used [a modern Guice dependency injection for Maven Plugins](/software/Modern-Config-Injection-In-Maven-Plugins).

## Update 2022-04-03
[Gitflow-incremental-builder](https://github.com/vackosar/gitflow-incremental-builder) is being developed beyond by phenomenal dev [Falko](https://github.com/famod).
The project used [Boundary Control Entity Architecture](/software/Boundary-Control-Entity-Architecture-The-Pattern-to-Structure-Your-Classes).
