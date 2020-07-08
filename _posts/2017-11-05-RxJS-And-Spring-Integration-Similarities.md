---
layout: post
title: "What Are RxJS And Spring Integration Similarities?"
date: 2017-11-05
description: Understand the frameworks better by comparing their concepts.
---


RxJS and Spring Integration are similar as former deals with event streams and latter with message streams.
Concepts are defined by other concepts and thus knowing more relations between them can improve ability to work with them. 
Below is a table comparing concepts in both frameworks. 

|RxJS          |Spring Integration |Note|
|--------------|-------------------|-----------------------------| 
|Observable    |IntegrationFlowDefinition|Part of Spring Integration DSL. Alternatively could be compared to MessageHandlerChain. |
|Subject       |SubscribableChannel (PublishSubscribeChannel)|Both frameworks allow publishing to multiple subscribers|
|Operator      |GenericTransformer |Operator is more general than transformer e.g. Router cannot be expressed as transformer. |
|filter        |filter    |Both filter elements.|
|map           |transform |Both map elements.|
|-             |MessageChannel     |MessageChannels are named connections with additional abilities like queuing.|
|~ Stream      |DirectChannel|Single threaded - push strategy.|
|-             |Router    |RxJS can do it with Subject and subscribed filtered streams. |
|ReplaySubject |-         |Similar concept to durable topic| 
|flatMap       |splitter  |Both split incoming elements into multiple.|
|delay         |delay     |Both delay elements.|  
|take          |-         |Not found probably because Spring Integration is intended mainly for channels living throughout the app.|
|buffer        |ReleaseStrategy Aggregator||
|Subject#onNext|Gateway  |Not directly equivalent but both can be used to publish on a method call.|


We can see that for most concepts we are able to find almost direct equivalent in the other framework. For those we cannot, an alternative can be easily introduced.