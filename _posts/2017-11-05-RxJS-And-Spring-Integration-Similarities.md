---
layout: post
title: "RxJS And Spring Integration Concept Similarities"
date: 2017-11-05
---
RxJS and Spring Integration are similar as former deals with event streams and latter with message streams. Below is a table comparing concepts in both frameworks. 

|RxJS          |Spring Integration |Note|
|--------------|-------------------|-----------------------------|
|Stream        |DirectChannel|That is single threaded stream of push strategy.| 
|Observable    |IntegrationFlowDefinition|Part of Spring Integration DSL. Alternatively could be compared to MessageHandlerChain. |
|Subject       |SubscribableChannel (PublishSubscribeChannel)|Both frameworks allow publishing to multiple subscribers|
|filter        |filter    ||
|map           |transform ||
|-             |MessageChannel     |MessageChannels are named connections with additional abilities like queuing.| 
|Operator      |GenericTransformer |Operator is more general than transformer e.g. Router cannot be expressed as transformer. |
|-             |Router    |RxJS can do it with Subject and subscribed filtered streams. |
|ReplaySubject |-         |Similar concept to durable topic| 
|flatMap       |splitter  ||
|delay         |delay     ||  
|take          |-         |Not found probably as Spring Integration is intended maily for channels living throughout the app.|
|buffer        |ReleaseStrategy Aggregator|
|Subject#onNext|Gateway  |Not directly equivalent but both can be used to publish on a method call.|


We can see that for most concepts we are able to find almost direct equivalent in the other framework. For those we cannot, an alternative can be easily introduced.