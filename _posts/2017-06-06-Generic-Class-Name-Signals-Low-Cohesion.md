---
layout: post
title: Generic Class Name Signals Low Cohesion
date: 2017-06-06
categories: software
description: Why and how to avoid non-specific class names like util, utils, or helper?
permalink: /:categories/:title
redirect_from:
- /2017/06/06/Generic-Class-Name-Signals-Low-Cohesion.html
last_modified_at: 2022-05-08
my_related_post_paths:
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2022-08-03-Strong-Static-Typing-vs-Weak-Dynamic-Typing.md
- _posts/2018-01-24-Modern-Config-Injection-In-Maven-Plugins.md
- _posts/2017-12-03-Boundary-Control-Entity-Architecture--The-Pattern-to-Structure-Your-Classes.md
- _posts/2017-10-28-Spring-Integration-Highlights.md
- _posts/2020-04-08-Python-Context-Manager-With-Statement-Exception-Handling.md
---



I think the best way to explain why util classes are suboptimal is using concept of **cohesion**. 
Cohesion is an important concept, which I also used in my previous post [Code Structure Principles](/software/Code-Structure-Principles).

Let's see [how Wikipedia defines the term:](https://en.wikipedia.org/wiki/Cohesion_(computer_science)):

*In computer programming, cohesion refers to the degree to which the elements inside a module belong together. Thus, cohesion measures the strength of relationship between pieces of functionality within a given module. For example, in highly cohesive systems functionality is strongly related.* 

We can see that the definition uses words: **belongs, relationship, related**.
 
So, how do we give a cohesive class good name? That's easy.
Just describe **the source of the class' cohesion** in a few specific words, and you have it. 
That is, camel case together relationship, belonging or relation of the class members.
In other words, describe what ties the members together instead of describing data or methods the object holds.
  
But what to do if you cannot come up with any short specific description?
It may be because that means that the class is not cohesive, or that there is no good english word.
In the later case some unique short text should suffice, people will remember it over time.


## Util or Helper Class
Going back to "Util" or "Helper" suffix, we can see the problem now.
Util is as generic as it can be. 
Util is basically equivalent to **"class with static methods and no fields that don't do business"**. 
Let's ignore the fact that this already imply [*lack of object orientation*](http://www.yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html).

## Three Reasons for A Bad Class Name
We have three possible cases. The class ...
1. is not cohesive, and it has to be refactored.
2. is cohesive, but is badly named.
3. simulates addition of functionality to a third party external class

The second case the momentum is set towards the worse second case.
Any programmer stumbling upon this class will see it a mere dumping group for generic methods vaguely related to the prefix.

The third case is the only reasonable.
When we cannot change third party libraries, but we still would like to add some functionality on top,
we may create an util class that simulates this modification.
These objects usually have the class on which we operate as a prefix.
Note that, there is a way to add functions to an external class in Scala called [implicit methods](https://www.scala-lang.org/blog/2016/12/07/implicit-function-types.html).


## But this old library has utils!
Most common dependencies in Java using Utils are Apache Commons.
Sometimes it is argued that since they contain Utils classes, then util classes are good design.
However, Apache Commons Util classes were created during the reign of Java 1.3. 
Which was stone age of software development and probably shouldn't be considered a perfect design.
In some cases, their utils classes are limited only to adding methods to classes outside its control in Java Core.
Such a limited use, could perhaps not be so bad.


## But I can find util class easily!
This is a poor argument for making code quality worse. Somehow all other classes are searchable with non generic names.
And when is class used often it is even more important for it to have a good design. 
Also, modern IDEs have a very good search functionality. Instead of "FooUtil" we **search "Foo" or "FooConverter"**. 
Or we look at other places were such functionality may be performed and reuse what we see. 


## Why not name classes based on their data or methods alone?
If we were to name based on data, if would be easy to create duplicate class names.
Naming purely based on methods is insufficient as it ignores the data.
Summarization of the cohesion of the both, partially communicating why the class exists, seems the best thing to do now to me.


## Related Articles And Stack Overflow Discussions

- [Is the word “Helper” in a class name a code smell?](https://stackoverflow.com/questions/2446376/is-the-word-helper-in-a-class-name-a-code-smell#2446499)
- [If a “Utilities” class is evil, where do I put my generic code?](https://stackoverflow.com/questions/3339929/if-a-utilities-class-is-evil-where-do-i-put-my-generic-code)
- [Utility classes are evil?](https://stackoverflow.com/questions/3340032/utility-classes-are-evil)
- [OOP Alternative to Utility Classes](http://www.yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html)
- [Helper Classes Are A Code Smell](https://wayback.archive.org/web/20161205052021/www.robbagby.com/posts/helper-classes-are-a-code-smell/)
- [Kill That Util Class!](http://www.jroller.com/DhavalDalal/entry/kill_that_util_class)
- [Are Helper Classes Evil?](https://blogs.msdn.microsoft.com/nickmalik/2005/09/06/are-helper-classes-evil/)
- [Avoiding Utility Classes](https://github.com/marshallward/marshallward.org/blob/master/content/avoid_util_classes.rst)