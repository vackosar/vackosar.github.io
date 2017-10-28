# Spring Integration Uncommon and Advanced Features


# Intro
Spring integration Intended for enterprise message-driven architectures and implements patterns descirbed in Enterprise Integration Patterns. This document consists of highlights of interesting parts of Spring Integration documentation.
 
## Goals:
- Provide a simple model for implementing complex enterprise integration solutions.
- Facilitate asynchronous, message-driven behavior within a Spring-based application.
- Promote intuitive, incremental adoption for existing Spring users. 

# Comparison with functional programming

|| Spring Integration || 

  

# Uncommon patterns

## Aggregator
Combines multiple messages from single input channel into a single Message. Is statefull as messages have to wait in message store for each other. Most common usage is for messsages to wait until a matching message (e.g. by correlation id) arrives or timeout. Is in a way opposite or Splitter.

### Resequencer
Suspends certain message group and sends them out ordered correctly. Default implementation uses groups by header attribute correlation id and sequences by header attribute sequence number. 

### Scatter-Gather
Sends a message to multiple recipients and then aggregates the replies. Recipients are registered via channel. Replies are gathered from a single reply channel.

### Thread Barrier

Suspends a message flow thread until some other asynchronous event occurs

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

### Channel Datatype 
Strong typing can be used on channel level as well: ```<int:channel id="numberChannel" datatype="java.lang.Number"/>```

### Channel Types

- DirectChannel: Default channel type. Single thread executes handler on the receiver side.
- QueueChannel: Sender publishes to queue. Messages are queued until consumers will consume them. Allows multiple consumers.
- PriorityChannel: QueueChannel with a priority.
- RendezvousChannel: Blocks sender until receiver consumes.
- ExecutorChannel: Multithreaded variant of DirectChannel.
- Scoped Channel: Allows limiting scope the channel.

## Messaging Bridge

Connects two Message Channels or Channel Adapters usually providing some flow controlling functionality. For example connecting JMS with Email. 

## Metrics: Time-Based Average Estimates

Other than expected the framework also offers Time-Based Average Estimates i.e. averages over messages are reflected less into result the further in the past messages arrived.
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
- Stops all inbound MessageProducer s (that are not OrderlyShutdownCapable).
- Waits for any remaining time left, as defined by the value of the long parameter passed in to the operation.
- Calls afterShutdown() on all OrderlyShutdownCapable components.
