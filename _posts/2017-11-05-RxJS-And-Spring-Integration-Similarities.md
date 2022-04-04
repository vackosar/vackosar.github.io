---
layout: post
title: "What Are RxJS And Spring Integration Similarities?"
date: 2017-11-05
description: Understand the frameworks better by comparing their concepts.
category: software
permalink: /:categories/:title
image: /images/spring-logo-9146a4d3298760c2e7e49595184e1975.svg
redirect_from:
- /2017/11/05/RxJS-And-Spring-Integration-Similarities.html
---


RxJS and [Spring Integration](/software/Spring-Integration-Highlights) are similar as former deals with event streams and latter with message streams.
Concepts are defined by other concepts and thus knowing more relations between them can improve ability to work with them. 
Below is a table comparing concepts in both frameworks. 

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


We can see that for most concepts we are able to find almost direct equivalent in the other framework.
For those we cannot, an alternative can be easily introduced.

Read comparison of [Sprint Integration with Java 8 Streams](/software/Spring-Integration-Highlights).
