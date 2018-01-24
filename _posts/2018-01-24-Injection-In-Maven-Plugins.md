---
layout: post
title: "Injection In Maven Plugins"
date: 2018-01-24
---

Default Maven injection framework based on Plexus is very limited. No constructor injection, all configuration parameters need to be part of Mojo and supported annotations are very unfamiliar to new comers.

Thankfully there has been effort in Maven to move towards more modern and mainstream injection - [JSR-330 support](https://maven.apache.org/maven-jsr330.html). Lastest Maven versions support usage of annotations like @Inject thanks to underlying Guice injection framework which replaced original Plexus.

However there are still many problems remaining unaddressed. Most painful for me was lack of configuration injection. For that I implemented custom support using Provider pattern tapping into Maven native configuration injection.

