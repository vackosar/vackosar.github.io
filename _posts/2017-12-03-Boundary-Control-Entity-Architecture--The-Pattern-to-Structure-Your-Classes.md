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

Boundary-Control-Entity (BCE) is also called Entity-Control-Boundary (ECB), Entity-Boundary-Control (EBC), Hexagonal, Onion, or The Clean Architecture (Clean Code book).
Boundary-Control-Entity architecture is effectively directory (package) structure pattern for sorting classes.
It is an alternative to Three-tier architecture. It is very simple and natural way to structure classes, which goes well with modularized architecture. 
ne creates one BCE package structure per a microservice, feature or module having ideally between 9 to 30 classes.  

<p><img src="/images/bce.svg" alt="Boundary Control Entity architecture"/></p>

## BCE Overview
BCE is distinct from the multi-tier architecture in that it does not see some outside systems as backend and some as frontend.
It has single category of outside systems. Sometimes BCE is being compared to MVC architecture where Model ~ Entity and View ~ Boundary. 

![actor entity boundary control example](/images/actor-boundary-control-entity.svg)

The package structure is often visualized as tree onion layers, or as a hexagonal layers, where the most outer layer is Boundary, central is Control and inner is Entity.
- Boundary is an interface to the outside world. It contains classes responsible for all communications with systems outside application runtime. It contains configuration, and establishing external connections.
- Control represents all logic that doesn't fit well into Boundary. It contains algorithms, SQL Queries.
- Entity contains data structures which are allowed to have some behaviour. It contains domain objects with basic functionalities.

![Onion of Actors, Boundary, Control, Entity](/images/onion-actors-boundary-control-entity.svg)

## Functionality Folders vs BCE Structure

I am very much for structuring, modularization and encapsulation according to end result features. However, often after separation per major features on sub 30 classes level, I think it is more practical to structure according to technical behaviour. Thus I suggest to use BCE architecture which represents that.

At the same time, don't be dogmatic and if there are good reasons do what works in the specific case. The BCE could even exist in the sub-folders of a parent folder. The parent folder than can follow service-oriented architecture, where each microservice has its own folder and runtime. Or some of the folder could have to have different names e.g. boundary may have to called "mojo" for example. If BCE doesn't work for you, let me know!

## Dependency Rule
Sometimes an additional dependency rule is being added to BCE: Classes can depend on other classes only within same layer or in one more inner layers.
I personally found that this rule impractical mainly thanks to modern tools like annotations.
For example annotation on Entity class can reference a serialization class residing in Control.

## SQL Queries and Repository Placement Dilemma
Where to place a classes that implement methods to query database? For example Spring Data repository classes in Java?
Repositories do define interaction with database. The dataset is an outside system, which would mean we should be placing them into Boundary.
But on the other hand they contain application logic in a form of a SQL queries, which should be placed in Control package instead.
I place repositories into the Control package.
However, code that deals with connections to the database, retries, transactions, database configuration, belongs to the Boundary.


## BCE Example
For real world example you can have a look at [this version of Gitflow Incremental Builder](https://github.com/gitflow-incremental-builder/gitflow-incremental-builder/tree/a5b310bad88da1ee12f887b77ac153ab20a7699e/src/main/java/com/vackosar/gitflowincrementalbuild), which I founded, but which was developed beyond by phenomenal dev [Falko](https://github.com/famod).
Read more about [Gitflow Incremental Builder here](/software/GitFlow-Incremental-Builder).
For an overview of boundary control entity architecture folder structure:

- boundary/
  - EventController: REST definition.
  - DBConnector: DB configuration, connection
- control/
  - EventTransformer: Transformation between Entity and Payload.
  - EventRepository: DB query definition.
- entity/
  - EventEntity
  - EventPayload
  
  
## BCE Quiz Challenge
Retain what you have just read by taking training quiz generated from this article.<br>
<br>
<a class="btn btn-warning" style="text-decoration: none;" href="https://quizrecall.com/study/public-test?store_id=dc985c9e-6812-41d3-a020-33c4a0340c16">Boundary-Control-Entity Quiz</a>


## Three-tier vs Boundary Control Entity Architecture
Three-tier architecture the much more common than Boundary Control Entity architecture.
Three-tier architecture is recommended by Marin Fowler under name of [Presentation, Domain, Data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html).
Three-tier architecture is composed of presentation layer, application layer, data access layer.
BCE splits domain objects from the data access layer and merges the rest with presentation layer:
- BCE Domain = domain objects (from the data access layer)
- BCE Boundary = presentation - data access without domain objects
- BCE Control = application layer


## Continue: The Cuts Across Your Architecture
Localize Related, Inline over Extract, Specific over Generic
BCE does not tell you everything, there are priciples that cuts across the BCE architecture.
[Learn about code structure principles - Localize Related, Inline over Extract, Specific over Generic](/software/Code-Structure-Principles).


## Other sources
- [Gitflow Incremental Builder uses BCE pattern architecture](https://github.com/gitflow-incremental-builder/gitflow-incremental-builder/tree/master/src/main/java/com/vackosar/gitflowincrementalbuild)
- [Down to earth Adam Bien's video on BCE](https://www.youtube.com/watch?v=grJC6RFiB58)
- [Uncle Bob's post - bit more ivory towerish](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
