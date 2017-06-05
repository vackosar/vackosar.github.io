---
layout: post
title: "Code Structure Principles"
date: 2017-06-04
---

This is a quick short intuitive alternative generalized view on code structure principles based on several years of personal experience, Martin Fowler's online posts, Bloch's Effective Java, McConnell's Code Complete and Adam Bien's online posts.      

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

## 2. Distribute Complexity
Code structure is improved by distributing complexity into multiple Code Containers. Local complexity is prioritized over total complexity. 

Code Container complexity is defined by the time needed by programmer to be able to understand, navigate and modify the Code Container.
This time is directly proportional to 
- the number or expressions used to express a Code Container.
- the number of unnamed or badly named Code Container references.
- on total complexity to a lesser extent.

### References
Usually 4-8 lines and cyclomatic complexity 3-7 is considered a good balance.
- "A long method is a good example of this - just looking at the code and my nose twitches if I see more than a dozen lines of java."; https://www.martinfowler.com/bliki/CodeSmell.html
- "Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing"."; https://www.martinfowler.com/books/refactoring.html
- "If you have a good name for a method you don't need to look at the body";  Refactoring: Improving the Design of Existing Code

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