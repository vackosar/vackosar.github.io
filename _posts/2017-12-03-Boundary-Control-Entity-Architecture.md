---
layout: post
title: "Boundary Control Entity Architecture"
date: 2017-12-03
---

Boundary-Control-Entity (BCE) architecture or Entity-Control-Boundary (ECB) is a package structure for sorting classes. I think it is very useful and natural way to structure classes, which goes well with modularized architecture. One creates one BCE package structure per a micro-service, feature or module having ideally between 9 to 30 classes.  

## Overview
BCE is distinct from Multitier architecture in that it does not see some outside systems as backend and some as frontend. It has single category of outside systems. Sometimes BCE is being compared to MVC architecture where Model ~ Entity and View ~ Boundary. 

The package structure is often visualized as tree onion layers, where the most outer layer is Boundary, central is Control and inner is Entity. The Boundary layer contains classes responsible for all communications with systems outside application runtime. Control represents all logic that doesn't fit well into boundary. Entity contains data structures which are allowed to have some behaviour.

## Feature vs Technical structuring

I am very much for structuring, modularization and encapsulation according to end result features. However often after separation per major features on sub 30 classes level, I think it is more practical to structure according to technical behaviour. Thus I suggest to use BCE architecture which represents that.    

## Dependency Rule
Sometimes an additional dependency rule is being added to BCE: Classes can depend on other classes only within same layer or in one more inner layers. I personally found that this rule practical mainly thanks to modern tools like annotations e.g. annotation on Entity class can reference a serialization class residing in Control.

## Repository Placement Dilemma
It was a dilemma for me where to place a Spring Data repository classes. Repositories do define interaction with database which is outside system placing them into Boundary, but on the other hand they contain application logic, which could be placed as well in Control. Since I gave up on "Dependency Rule" (see above), I think the repository classes belong in Boundary.  

## Example
See below Spring Boot and Spring Data example.

- boundary
  - EventController: REST definition.
  - EventRepository: DB query definition.
- control
  - EventTransformer: Transformation between Entity and Payload.
- entity
  - EventEntity
  - EventPayload


## References
- https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html
- http://www.cs.sjsu.edu/~pearce/modules/patterns/enterprise/ecb/ecb.htm
- http://epf.eclipse.org/wikis/openuppt/openup_basic/guidances/concepts/entity_control_boundary_pattern,_uF-QYEAhEdq_UJTvM1DM2Q.html
- http://jeffreypalermo.com/blog/the-onion-architecture-part-1/