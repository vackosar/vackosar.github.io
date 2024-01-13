---
layout: post
title: Boundary Control Entity Architecture Pattern
image: /images/bce.svg
categories: software
description: BCE is a source code structure pattern sometimes called ECB, EBC, Hexagonal, Onion, Clean architecture, or MVC.
date: 2017-12-03
last_modified_at: 2022-06-06
permalink: /:categories/:title
redirect_from:
- /2017/12/03/Boundary-Control-Entity-Architecture.html
- /software/Boundary-Control-Entity-Architecture
my_related_post_paths:
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2016-07-03-GitFlow-Incremental-Builder.md
- _posts/2023-10-29-Encoder-only-Decoder-only-vs-Encoder-Decoder-Transfomer.md
- _posts/2022-05-20-bits-per-byte-and-bits-per-character.md
- _posts/2017-10-28-Spring-Integration-Highlights.md
- _posts/2017-06-06-Generic-Class-Name-Signals-Low-Cohesion.md
- _posts/2020-05-11-BentoML-vs-Cortex.dev--ML-Serving-Showdown.md
---



Boundary-Control-Entity (BCE) is also called Entity-Control-Boundary (ECB), Entity-Boundary-Control (EBC), Hexagonal, Onion, or The Clean Architecture (Clean Code book).
Boundary-Control-Entity architecture is effectively directory (package) structure pattern for sorting classes.
It is an alternative to Three-tier architecture. It is very simple and natural way to structure classes, which goes well with modularized architecture. 
One creates one BCE package structure per a microservice, feature or module having ideally between 9 and 30 classes.  

{% include image.html src="/images/bce.svg" alt="Boundary Control Entity architecture" %}


## BCE Explained
BCE is distinct from the multi-tier architecture in that it does not see some outside systems as backend and some as frontend.
It has single category of outside systems.

{% include image.html src="/images/actor-boundary-control-entity.svg" alt="actor entity boundary control example" %}

The package structure is often visualized as tree onion layers, or as a hexagonal layers, where the most outer layer is Boundary, central is Control and inner is Entity.
- Boundary is an interface to the outside world. It contains classes responsible for all communications with systems outside application runtime. It contains configuration, and establishing external connections. You may choose to place all API objects here as well and separate internal domain objects into entity package to avoid accidentally changing the API.
- Control represents all logic that doesn't fit well into Boundary. It contains algorithms, SQL Queries.
- Entity contains data structures which are allowed to have some behaviour. It contains domain objects with basic functionalities.

{% include image.html src="/images/onion-actors-boundary-control-entity.svg" alt="Onion of Actors, Boundary, Control, Entity" %}


## Three-tier vs Boundary Control Entity Architecture
Three-tier architecture the much more common than Boundary Control Entity architecture.
Three-tier architecture is recommended by Marin Fowler under name of [Presentation, Domain, Data](https://martinfowler.com/bliki/PresentationDomainDataLayering.html).
Three-tier architecture is composed of presentation layer, application layer, data access layer.
BCE splits domain objects from the data access layer and merges the rest with presentation layer:
- BCE Domain = domain objects (from the data access layer)
- BCE Boundary = presentation - data access without domain objects
- BCE Control = application layer


## BCE vs MVC
Boundary-Control-Entity (BCE) can be compared to Model-View-Controller (MVC) architecture.

MVC is composed of:
- Model: Represents the data and business logic of the system, similar to the Entity component in BCE.
- View: Represents the presentation layer, responsible for displaying the data from the model to the user. It is similar to the Boundary component in BCE, focusing on user interfaces.
- Controller: Acts as an intermediary between the model and the view, handling user input and updating the model and view accordingly. It is similar to the Control component in BCE.

Key concepts have analogous function:
- Model ~ Entity
- View ~ Boundary
- Controller ~ Control

View in MVC is specifically user web view in the presentation layer.
MVC is more commonly used in web development and user interface design, while BCE can be applied more broadly to various types of software systems, including those without a user interface.
BCE focuses more on the system-actor interactions and MVC emphasizing the separation between the presentation layer and the underlying data and logic.


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


## Continue: The Cuts Across Your Architecture
Localize Related, Inline over Extract, Specific over Generic
BCE does not tell you everything, there are priciples that cuts across the BCE architecture.
[Learn about code structure principles - Localize Related, Inline over Extract, Specific over Generic](/software/Code-Structure-Principles).


## Other sources
- [Gitflow Incremental Builder uses BCE pattern architecture](https://github.com/gitflow-incremental-builder/gitflow-incremental-builder/tree/master/src/main/java/com/vackosar/gitflowincrementalbuild)
- [Down to earth Adam Bien's video on BCE](https://www.youtube.com/watch?v=grJC6RFiB58)
- [Uncle Bob's post - bit more ivory towerish](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
