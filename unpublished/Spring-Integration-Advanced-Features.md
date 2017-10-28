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

### Messaging Bridge

Connects two Message Channels or Channel Adapters usually providing some flow controlling functionality. For example connecting JMS with Email. 

## JDBC Message Store

