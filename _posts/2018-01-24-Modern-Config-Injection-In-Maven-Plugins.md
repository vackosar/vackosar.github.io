---
layout: post
title: "Modern Config Injection In Maven Plugins"
date: 2018-01-24
categories: software
description: Simple constructor injection of config params in Maven Plugins can be done.
image: https://raw.githubusercontent.com/vackosar/vackosar.github.io/master/images/glow-drawing.png
permalink: /:categories/:title
redirect_from:
  - /2018/01/24/Modern-Config-Injection-In-Maven-Plugins.html
---

Default Maven injection framework based on Plexus is very limited. No constructor injection, all configuration parameters need to be part of a Mojo and supported annotations are very unfamiliar to new comers.

Thankfully there has been [effort in Maven to towards modern and mainstream injection - JSR-330 support](https://maven.apache.org/maven-jsr330.html). Lastest Maven versions support usage of annotations like @Inject thanks to running Guice injection framework under the hood replacing original Plexus.

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
