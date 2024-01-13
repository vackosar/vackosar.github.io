---
layout: post
title: Modern Config Injection In Maven Plugins
date: 2018-01-24
categories: software
description: Maven Mojo constructor injection of config parameters via Guice JSR-330 support.
permalink: /:categories/:title
redirect_from:
- /2018/01/24/Modern-Config-Injection-In-Maven-Plugins.html
my_related_post_paths:
- _posts/2016-07-03-GitFlow-Incremental-Builder.md
- _posts/2017-10-28-Spring-Integration-Highlights.md
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2016-07-22-Obsolete-Branch-Remover.md
- _posts/2017-06-06-Generic-Class-Name-Signals-Low-Cohesion.md
- _posts/2018-12-17-My-First-Contribution-To-Major-OSS-Project.md
- _posts/2021-03-22-google-product-taxonomy-viewer.md
---



{% include highlight-rouge-friendly.css.html %}

Default Maven injection framework based on Plexus is very limited. No constructor injection, all configuration parameters need to be part of a Mojo and supported annotations are very unfamiliar to new comers.

Thankfully there has been [effort in Maven to towards modern and mainstream injection - JSR-330 support](https://maven.apache.org/maven-jsr330.html). Latest Maven versions support usage of annotations like @Inject thanks to running Guice injection framework under the hood replacing original Plexus.

However there are still many problems remaining unaddressed. Most painful for me was lack of configuration injection. That is lack of replacement for @Parameter annotation. Without it I could not inject properties into separate components encapsulating their parsing, transformation or composition.

Thankfully there is a way to provide custom support using Provider pattern tapping into Maven native configuration injection.

Say you have a configuration of a plugin:

```xml
<plugin>
  ...
  <configuration>
    <property1>value1</property1>
</configuration>
</plugin>
```

Then you would implement a provider:

```java
class Property1Provider extends RequiredConfigProvider<String> {
    
    private String value;
    
    ...
}
```

The super class would call a Maven's inner undocumented class [CompositeBeanHelper](https://github.com/eclipse/sisu.plexus/blob/master/org.eclipse.sisu.plexus/src/org/eclipse/sisu/plexus/CompositeBeanHelper.java) providing injection even for complex objects like maps. I had to instantiate this class via reflaction i.e. ```Class.forName```.

```java
class RequiredConfigProvider<T> {
  // Inject the instance to extract values from. 
  @Inject 
  public RequiredConfigProvider(MojoExecution mojoExecution)
  ...  
  // Filter for a property in plugin configuration.
  mojoExecution.getPlugin().getConfiguration()
  ...
  // Set the value to the child e.g. Property1Provider.
  compositeBeanHelper.setProperty(...)
  ... 
}

```

Using above resolves most of the issues with full usage of JSR-330 i.e. Guice injection in Maven plugins.

## Example Project: GitFlow Incremental Builder
[GitFlow Incremental Builder for Maven, that speeds up you builds by building only git-changed parts](/software/GitFlow-Incremental-Builder), uses a Guice dependency injection for its Maven Plugin.
