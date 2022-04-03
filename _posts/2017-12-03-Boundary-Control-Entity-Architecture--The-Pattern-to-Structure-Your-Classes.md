---
layout: post
title: "Boundary Control Entity Architecture: The Pattern to Structure Your Classes"
image: /images/bce.svg
categories: software
description: BCE is a file structure for source code files sometimes with additional dependency restrictions. Example included!
date: 2017-12-03
permalink: /:categories/:title
redirect_from:
  - /2017/12/03/Boundary-Control-Entity-Architecture.html
  - /software/Boundary-Control-Entity-Architecture
---

Boundary-Control-Entity (BCE), or Entity-Control-Boundary (ECB), or Entity-Boundary-Control (EBC) architecture is a directory (package) structure pattern for sorting classes. It is an alternative to layered architecture. It is very simple and natural way to structure classes, which goes well with modularized architecture. One creates one BCE package structure per a microservice, feature or module having ideally between 9 to 30 classes.  

<p><img src="/images/bce.svg" alt="Boundary Control Entity architecture"/></p>

## Overview
BCE is distinct from the multi-tier architecture in that it does not see some outside systems as backend and some as frontend. It has single category of outside systems. Sometimes BCE is being compared to MVC architecture where Model ~ Entity and View ~ Boundary. 

![actor entity boundary control example](/images/actor-boundary-control-entity.svg)

The package structure is often visualized as tree onion layers, where the most outer layer is Boundary, central is Control and inner is Entity. The Boundary layer contains classes responsible for all communications with systems outside application runtime. Control represents all logic that doesn't fit well into boundary. Entity contains data structures which are allowed to have some behaviour.

![Onion of Actors, Boundary, Control, Entity](/images/onion-actors-boundary-control-entity.svg)

## Functionality Folders vs BCE Structure

I am very much for structuring, modularization and encapsulation according to end result features. However, often after separation per major features on sub 30 classes level, I think it is more practical to structure according to technical behaviour. Thus I suggest to use BCE architecture which represents that.

At the same time, don't be dogmatic and if there are good reasons do what works in the specific case. The BCE could even exist in the sub-folders of a parent folder. The parent folder than can follow service-oriented architecture, where each microservice has its own folder and runtime. Or some of the folder could have to have different names e.g. boundary may have to called "mojo" for example. If BCE doesn't work for you, let me know!

## Dependency Rule
Sometimes an additional dependency rule is being added to BCE: Classes can depend on other classes only within same layer or in one more inner layers. I personally found that this rule impractical mainly thanks to modern tools like annotations e.g. annotation on Entity class can reference a serialization class residing in Control.

## Repository Placement Dilemma
It was a dilemma for me where to place a classes used to access database (Spring Data repository classes in Java). Repositories do define interaction with database which is outside system placing them into Boundary, but on the other hand they contain application logic, which could be placed as well in Control. Since I gave up on "Dependency Rule" (see above), I think the repository classes belong in Boundary.  

## Example
For real world example you can have a look at [this version of Gitflow Incremental Builder](https://github.com/gitflow-incremental-builder/gitflow-incremental-builder/tree/a5b310bad88da1ee12f887b77ac153ab20a7699e/src/main/java/com/vackosar/gitflowincrementalbuild), which I founded, but which was developed beyond by phenomenal dev [Falko](https://github.com/famod).
Read more about [Gitflow Incremental Builder here](/software/GitFlow-Incremental-Builder).
For an overview of boundary control entity architecture folder structure:

- boundary/
  - EventController: REST definition.
  - EventRepository: DB query definition.
- control/
  - EventTransformer: Transformation between Entity and Payload.
- entity/
  - EventEntity
  - EventPayload
  
  
## Quiz Challenge
Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=dc985c9e-6812-41d3-a020-33c4a0340c16">Boundary-Control-Entity Quiz</a>

## Continue: The Cuts Across The Architecture
Code structure cuts across the architecture. [Learn about code structure principles here](/software/Code-Structure-Principles).


## Other sources
- [Gitflow Incremental Builder has BCE pattern](https://github.com/gitflow-incremental-builder/gitflow-incremental-builder/tree/master/src/main/java/com/vackosar/gitflowincrementalbuild)
- [Down to earth Adam Bien's video on BCE](https://www.youtube.com/watch?v=grJC6RFiB58)
- [Uncle Bob's post - bit more ivory towerish](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
