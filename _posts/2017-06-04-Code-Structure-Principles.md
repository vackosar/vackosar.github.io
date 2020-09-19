---
layout: post
title: "How To Structure Code: Localize Related, Inline Over Extract, Minimize Visibility"
date: 2017-06-04
category: software
description: A short alternative view on code structure principles based on several years of personal experience, Martin Fowler's online posts, Bloch's Effective Java, McConnell's Code Complete and Adam Bien's online posts.
permalink: /:categories/:title
redirect_from:
  - /2017/06/04/Code-Structure-Principles.html
---

However, as with all the rules, do not put the horse before the caret.
Don't optimize code structure too early, and don't be too stringent.
Focus more on the specifics of your problem than on generics offered by the ivory tower books.

Sections:
- [Code Containers](#code-containers)
- [1. Localize Related](#1-localize-related)
- [2. Inline over extract](#2-inline-over-extract)
- [3. Minimize Visibility](#3-minimize-visibility)

Code structure cuts across the architecture. Learn about dead-simple architecture called [Boundary-Control-Entity here](https://vaclavkosar.com/software/Boundary-Control-Entity-Architecture).

## Code Containers
Code Containers is a term used in this post to refer to a instance of a level of hierarchy into which code can be sorted.

In Java, code is sorted into following hierarchy:
- function or field
- class
- package
- maven module
- micro-service


## 1. Localize Related

Code structure is improved by sorting Code Containers which are related into single higher hierarchy Code Container.

Related Code Containers are defined by following:
- Related Code Containers often use same Code Containers.
- Programmers are able to learn to often anticipate membership of unfamiliar Code Container in Related Code Containers.
- Deployment lifecycle, stability and monitoring are often the same for Related Code Containers.
- Same programmers often work on the same Related Code Containers.

### Examples

#### Related Methods
Functions ```a``` and ```b``` both call function ```c```, thus they are related. Because they are related they are placed into higher container ```A```.

```java
 class A {
   
   int a(int v) {
     return c(v)*2;
   }
   
   int b(int v) {
     return c(v)*3;
   }
   
   private int c(int v) {
     return v + 1;
   }
 }
```

#### Related Classes

Both classes import same class ```B```. In absence of other restrictions they can be placed within same package as ```B```. 
```java
import B;
class A { }
```

```java
import B;
class C { }

```

#### Related Packages
Related packages which are used by two different modules are can be placed into one common Maven module. This module can be then used as Maven dependency. 

#### Micro-service as a Maven module
Micro-services in Java are defined by a Maven module. Final micro-service executable jar then usually contains the defining module jar and all its dependencies.
 
## References
- Real world objects often fulfill the criteria. Particularly the second one. Real world objects are recommended as first candidates for object creation ("Find Real-World Objects"; Code Complete)
- "Classes that contain strongly related functionality are described as having strong cohesion, and the heuristic goal is to make cohesion as strong as possible."; Aim for Strong Cohesion; Code Complete
- "Coupling describes how tightly a class or routine is related to other classes or routines."; Keep Coupling Loose, Code Complete.
- "Try to create modules that depend little on other modules."; Keep Coupling Loose, Code Complete.
- "in reality, they are little more than convenient carrying cases for loosely related collections of data and routines."; Class Foundations: Abstract Data Types (ADTs), Code Complete
- [Generic Class Name Signals Low Cohesion](https://vackosar.github.io/2017/06/06/Generic-Class-Name-Signals-Low-Cohesion.html)

## 2. Inline over Extract

I used to have a section referencing Martin Fowler and divide and conquer strategy about keeping methods short and low complexity.
But since then I came around to view of the productive programmers like [Carmack](http://number-none.com/blow/john_carmack_on_inlined_code.html) and [Jonathan Blow](https://youtu.be/JjDsP5n2kSM). 
After testing the idea myself, I do think that longer methods are more productive than lots of small methods.
Extracting small methods makes the code less transparent, harder to refactor, and harder to write.
A complexity is better exposed attempted to be hidden.

>  The function that is least likely to cause a problem is one that doesn't exist, which is the benefit of inlining it.

### Example
USD rate below is extracted into a separate Code Container - into a field. Replacing magic value with named field increases human readability.
While method ```transformToUsd``` is simplified, the class itself becomes more complex. This exemplifies prioritizing local complexity over total complexity. 
```java
class CurrencyAmountTransformer {
    
    private double USD_RATE = 1.2;
    
    double transformToUsd(double amount) {
        return USD_RATE * amount;
    }
    
}
```

## 3. Minimize Visibility
Code structure is improved by minimizing visibility of lower level Code Structures across higher level Code Structures boundaries.

### References

- "A method is not used by any other class. Make the method private."; https://refactoring.com/catalog/hideMethod.html

### Examples

#### Field Hiding
Field ```USD_RATE``` is not visible outside class ```CurrencyAmountTransformer```.
```java
class CurrencyAmountTransformer {
    
    private double USD_RATE = 1.2;
    
    double transformToUsd(double amount) {
        return USD_RATE * amount;
    }
    
}
```

#### Class Hiding
Java allows classes that can be imported only within given package.

#### Maven Modules Don't Allow Hiding
Unfortunately Maven modules don't provide restriction of visibility of dependency modules only within given Module. All dependencies of a dependency will also become dependencies of a dependent. 

#### Micro-Service API
 
Micro-services usually publish only minimal API which can be used to interact with it. 

## Continue: The Dead-Simple Architecture
Code structure cuts across the architecture. [Learn about a dead-simple architecture called Boundary-Control-Entity here](/software/Boundary-Control-Entity-Architecture).
