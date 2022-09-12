---
layout: post
title: Spring Integration Highlights - message driven architecture
date: 2017-10-28
categories: software
description: Get familiar with Spring Integration implementation of Enterprise Integration Patterns and compare it to Java 8 Streams and RxJS.
image: /images/spring-logo-9146a4d3298760c2e7e49595184e1975.svg
permalink: /:categories/:title
redirect_from:
- /2017/10/28/Spring-Integration-Highlights.html
- /2017/11/05/RxJS-And-Spring-Integration-Similarities.html
my_related_post_paths:
- _posts/2017-12-03-Boundary-Control-Entity-Architecture--The-Pattern-to-Structure-Your-Classes.md
- _posts/2018-01-24-Modern-Config-Injection-In-Maven-Plugins.md
- _posts/2018-12-17-My-First-Contribution-To-Major-OSS-Project.md
- _posts/2017-07-05-Easy-Online-Independence-1-Mail-Backup.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
---



Spring integration is intended for enterprise message-driven architectures. It implements patterns described in the Enterprise Integration Patterns book. This document consists of highlights of interesting parts of [Spring Integration documentation](https://docs.spring.io/spring-integration/docs/current/reference/html/index.html).
 
## Spring Integration Comparison to Other Frameworks


### Spring Integration vs Java 8 Streams
Message driven architectures have many similar abstractions to functional programming. See for example comparison with Java 8 Streams. 

<table class="table table-striped">
    <thead>
        <tr>
            <th>Spring Integration</th>
            <th>Java 8 Streams</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Chain</td>
            <td>Pipeline</td>
        </tr>
        <tr>
            <td>Filter</td>
            <td>filter function</td>
        </tr>
        <tr>
            <td>Transformer</td>
            <td>map function</td>
        </tr>
        <tr>
            <td>Splitter</td>
            <td>flatMap</td>
        </tr>
    </tbody>
</table>

One of main differences between is treatment of time e.g. Java 8 Streams don't have equivalent method to Delayer. Java 8 Streams are not normally integrating with outside systems and are to finish immediately. 

### Spring Integration vs RxJS

RxJS and Spring Integration are similar as former deals with event streams and latter with message streams.
Concepts are defined by other concepts and thus knowing more relations between them can improve ability to work with them.
Below is a table comparing concepts in both frameworks. We can see that for most concepts we are able to find almost direct equivalent in the other framework.
For those we cannot, an alternative can be easily introduced.

<table class="table table-striped">
    <thead>
        <tr>
            <th>RxJS</th>
            <th>Spring Integration</th>
            <th>Note</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Observable</td>
            <td>IntegrationFlowDefinition</td>
            <td>Part of Spring Integration DSL. Alternatively could be compared to MessageHandlerChain.</td>
            <td></td>
        </tr>
        <tr>
            <td>Subject</td>
            <td>SubscribableChannel (PublishSubscribeChannel)</td>
            <td>Both frameworks allow publishing to multiple subscribers</td>
            <td></td>
        </tr>
        <tr>
            <td>Operator</td>
            <td>GenericTransformer</td>
            <td>Operator is more general than transformer e.g. Router cannot be expressed as transformer.</td>
            <td></td>
        </tr>
        <tr>
            <td>filter</td>
            <td>filter</td>
            <td>Both filter elements.</td>
            <td></td>
        </tr>
        <tr>
            <td>map</td>
            <td>transform</td>
            <td>Both map elements.</td>
            <td></td>
        </tr>
        <tr>
            <td>-</td>
            <td>MessageChannel</td>
            <td>MessageChannels are named connections with additional abilities like queuing.</td>
            <td></td>
        </tr>
        <tr>
            <td>~ Stream</td>
            <td>DirectChannel</td>
            <td>Single threaded - push strategy.</td>
            <td></td>
        </tr>
        <tr>
            <td>-</td>
            <td>Router</td>
            <td>RxJS can do it with Subject and subscribed filtered streams.</td>
            <td></td>
        </tr>
        <tr>
            <td>ReplaySubject</td>
            <td>-</td>
            <td>Similar concept to durable topic</td>
            <td></td>
        </tr>
        <tr>
            <td>flatMap</td>
            <td>splitter</td>
            <td>Both split incoming elements into multiple.</td>
            <td></td>
        </tr>
        <tr>
            <td>delay</td>
            <td>delay</td>
            <td>Both delay elements.</td>
            <td></td>
        </tr>
        <tr>
            <td>take</td>
            <td>-</td>
            <td>Not found probably because Spring Integration is intended mainly for channels living throughout the app.</td>
            <td></td>
        </tr>
        <tr>
            <td>buffer</td>
            <td>ReleaseStrategy Aggregator</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Subject#onNext</td>
            <td>Gateway</td>
            <td>Not directly equivalent but both can be used to publish on a method call.</td>
            <td></td>
        </tr>
    </tbody>
</table>

## Aggregator
Combines multiple messages from single input channel into a single Message. Is stateful as messages have to wait in message store for each other. Most common usage is for messages to wait until a matching message (e.g. by correlation id) arrives or timeout. Is in a way opposite or Splitter.

## Resequencer
Suspends certain message group and sends them out ordered correctly. Default implementation groups by header attribute correlation_id and sequences by header attribute sequence_number. 

## Scatter-Gather
Sends a message to multiple recipients and then aggregates the replies. Recipients are registered by listing their channels. Replies are gathered from a single reply channel.

## Thread Barrier

Suspends a message until correlating message arrives on separate channel or times out sending message to discard channel.

```
<int:barrier id="barrier1" input-channel="in" output-channel="out"
        correlation-strategy-expression="headers['myHeader']"
        output-processor="myOutputProcessor"
        discard-channel="lateTriggerChannel"
        timeout="10000">
</int:barrier>

<int:outbound-channel-adapter channel="release" ref="barrier1.handler" method="trigger" />
```

### Claim Check
Hides temporarily part of a message. Hidden data is stored separately and later claimed to be returned.

```
<int:claim-check-in id="checkin"
        input-channel="checkinChannel"
        message-store="testMessageStore"
        output-channel="output"/>
        
<int:claim-check-out id="checkout"
        input-channel="checkoutChannel"
        message-store="testMessageStore"
        output-channel="output"/>
```

## Channel Configuration

### Channel Modes

- Point to Point: Default
- Publish, subscribe

### Channel Types

- DirectChannel: Default channel type. Single thread executes handler on the receiver side.
- QueueChannel: Sender publishes to queue. Messages are queued until consumers will consume them. Allows multiple consumers.
- PriorityChannel: QueueChannel with a priority.
- RendezvousChannel: QueueChannel using Blocking Queue for multithreaded submission. Blocks sender until receiver consumes.
- ExecutorChannel: Multithreaded subscribable variant of DirectChannel.
- Scoped Channel: Allows limiting scope of the channel.

## Messaging Bridge

Connects two Message Channels or Channel Adapters usually providing some flow controlling functionality. For example connecting JMS with Email. 

## Metrics: Time-Based Average Estimates

Other than usual metrics the framework also offers interesting averaging method Time-Based Average Estimates. Averages corresponding to older messages are reflected less into the result.
For example ```S(n) = sum(i=0 to n) exp(-i/M) x(i)/ sum(i= 0 to n) exp(-i/M)``` where ```x(i)``` is an average for a time slot ```i```.  

## Monitoring: Integration Graph
Provides access to an application’s runtime object model which can, optionally, include component metrics.
Example:
```
{
  "contentDescriptor": {
    "providerVersion": "4.3.0.RELEASE",
    "providerFormatVersion": 1.0,
    "provider": "spring-integration",
    "name": "myApplication"
  },
  "nodes": [
    {
      "nodeId": 1,
      "name": "nullChannel",
      "stats": null,
      "componentType": "channel"
    },
    {
      "nodeId": 2,
      "name": "errorChannel",
      "stats": null,
      "componentType": "publish-subscribe-channel"
    },
    {
      "nodeId": 3,
      "name": "_org.springframework.integration.errorLogger",
      "stats": {
        "duration": {
          "count": 0,
          "min": 0.0,
          "max": 0.0,
          "mean": 0.0,
          "standardDeviation": 0.0,
          "countLong": 0
```

## Message History

Stores ids of components that were visited by the message in the message's header.
```
[{name=sampleGateway, type=gateway, timestamp=1283281668091},
 {name=sampleChain, type=chain, timestamp=1283281668094}]
```

## Message Store
Stores messages into configured persistent or in-memory storage including using JDBC and MongoDb.

## Orderly Shutdown

Stop the application in an orderly manner. MBean exporter provides a JMX operation stopActiveComponents. Allows implementing custom shutdown behaviour of beans that implement OrderlyShutdownCapable.

- Calls beforeShutdown() on beans implementing OrderlyShutdownCapable. 
- Stops any active channels, such as JMS- or AMQP-backed channels.
- Stops all MessageSources.
- Stops all inbound MessageProducer's (that are not OrderlyShutdownCapable).
- Waits for any remaining time left, as defined by the value of the long parameter passed in to the operation.
- Calls afterShutdown() on all OrderlyShutdownCapable components.
