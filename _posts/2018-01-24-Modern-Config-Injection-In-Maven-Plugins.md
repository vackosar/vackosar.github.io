---
layout: post
title: "Modern Config Injection In Maven Plugins"
date: 2018-01-24
---

Default Maven injection framework based on Plexus is very limited. No constructor injection, all configuration parameters need to be part of Mojo and supported annotations are very unfamiliar to new comers.

Thankfully there has been effort in Maven to move towards more modern and mainstream injection - [JSR-330 support](https://maven.apache.org/maven-jsr330.html). Lastest Maven versions support usage of annotations like @Inject thanks to underlying Guice injection framework which replaced original Plexus.

However there are still many problems remaining unaddressed. Most painful for me was lack of configuration injection. Without it I could not inject properties into separate components encapsulating their parsing, transformation or composition.

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
    
    private String property1;
    
    ...
}
```

The super class would call a Maven's inner undocumented class ```CompositeBeanHelper``` providing injection even for complex objects like maps.

```java
class RequiredConfigProvider<T> {
    
  ...
  compositeBeanHelper.setProperty(...)
  ... 
}

```

Using above resolves most of the issues with full usage of JSR-330 i.e. Guice injection in Maven plugins.
