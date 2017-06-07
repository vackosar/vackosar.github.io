---
layout: post
title: "Generic Class Name Signals Low Cohesion"
date: 2017-06-06
---

I find myself often explaining why to avoid generic **non specific class names**. 
The **most often classes suffixed with "Util"** seem to be harder to perceive as non specific.
Even when most classes in project have nice specific name, somehow "Util" suffixed classes seem to be excluded from intuitive naming strategies.

I think the best way to explain why util classes are suboptimal is using concept of **cohesion**. 
Cohesion is an important concept, which I also used in my previous post [Code Structure Principles](/2017-06-04-Code-Structure-Principles.md).

Let's see [how Wikipedia defines the term:](https://en.wikipedia.org/wiki/Cohesion_(computer_science))
> 
    In computer programming, cohesion refers to the degree to which the elements inside a module belong together.[1] Thus, cohesion measures the strength of relationship between pieces of functionality within a given module. For example, in highly cohesive systems functionality is strongly related. 

We can see that the definition uses words: **belongs, relationship, related**.
 
So, how do we give a cohesive class good name? That's easy. Just describe **the source of the class' cohesion** in a few specific words and you have it. 
That is, **camel case together relationship, belonging or relation of the class members**.
  
But what to do if you cannot come up with any short specific description? That is harder as **that means that the class is not cohesive**.

Going back to "Util" suffix, we can see the problem now. Util is as generic as it can be. 
Util is basically equivalent to **"class with static methods and no fields that don't do business"**. 
Let's ignore the fact that this already imply [*lack of object orientation*](http://www.yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html).
Adding class name of class with which common parameter of doesn't make it more specific. **It doesn't describe the source of cohesion** any more.

We have two possible cases:
- The class is cohesive, but is badly named.
- The class is not cohesive and it has to be refactored.

Unfortunately in the first case the momentum is set towards the worse second case.
Any programmer stumbling upon this class **will see it a mere dumping group for generic methods** vaguely related to the prefix.

## Related Articles

- [Is the word “Helper” in a class name a code smell?](https://stackoverflow.com/questions/2446376/is-the-word-helper-in-a-class-name-a-code-smell#2446499)
- [If a “Utilities” class is evil, where do I put my generic code?](https://stackoverflow.com/questions/3339929/if-a-utilities-class-is-evil-where-do-i-put-my-generic-code)
- [Utility classes are evil?](https://stackoverflow.com/questions/3340032/utility-classes-are-evil)
- [OOP Alternative to Utility Classes](http://www.yegor256.com/2014/05/05/oop-alternative-to-utility-classes.html)
- [Helper Classes Are A Code Smell](https://wayback.archive.org/web/20161205052021/www.robbagby.com/posts/helper-classes-are-a-code-smell/)
- [Kill That Util Class!](http://www.jroller.com/DhavalDalal/entry/kill_that_util_class)
- [Are Helper Classes Evil?](https://blogs.msdn.microsoft.com/nickmalik/2005/09/06/are-helper-classes-evil/)
- [Avoiding Utility Classes](https://github.com/marshallward/marshallward.org/blob/master/content/avoid_util_classes.rst)