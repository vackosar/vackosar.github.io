---
title: Symbolic vs Connectionist Machine Learning
description: Reasoning and reducing hallucinations in large language models by hybridizing with algorithms.
categories: ml
date: 2023-03-23
last_modified_at: 2023-03-25
image: /images/symbols-patterns-hybrids.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2020-06-19-openais-glow-flow-based-model-teardown.md
- _posts/2022-09-16-Tokenization-in-Machine-Learning-Explained.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2022-04-18-how-computers-understood-humans.md
- _posts/2019-06-30-FastText-Vector-Norms-And-OOV-Words.md
---

![symbols patterns hybrids](/images/symbols-patterns-hybrids.png)

Today I would like to tell you what is **increasingly becoming popular in large language models**. What I think will be a future of this field that could potentially provide some things I think are missing for us perhaps to get to the **artificial general intelligence**. As defined, maybe as a system that can do as many things as, for example, an average person in 2022.


## Large Language Model's Hallucinations and Poor-Reasoning

![large-language-models-hallucinations-and-poor-reasoning](/images/large-language-models-hallucinations-and-poor-reasoning.png)

What are the **missing things in current systems**? So now we burn through a gajillion, it’s like trillions of floating point operations with all these multiplications and we still get **hallucinations** and we still get quite **poor reasoning capabilities**. And there are approaches reducing this, but something still seems to be missing.

Yes, it’s true that humans as well hallucinate. For example, you may have a **false memory**, so maybe you don’t remember everything perfectly. For example, if there is a crime, oftentimes the people have actually different accounts.

We already developed approaches how to deal with these issues. We write down **symbols** and into the symbols we can even encode **rules**. And the rules can operate on the symbols and it’s like a perfect system. It was super successful in understanding the world because we used it to create **mathematics**, which was used for **accounting, physics, and engineering**.

Because we can write things down and they don’t disappear, they stay the same. It’s an **immutable storage**. We can also think about the things multiple times. And another thing that perhaps is also important is that we can **act in the world** and so we can **sample new data** and learn new things from experience.


These **successful symbolic tools** were then later used to develop computer programs which are also rules, which operate on symbols. So the same way we actually built these computers which take something that's **crystal perfect** and it can produce something that's still crystal perfect. And while all at the same time this seems to be missing in the **language model**, this sort of aspect is not quite there.

## Symbolic vs Connectionist Comparison
![intuition-symbolic-vs-connectionist](/images/intuition-symbolic-vs-connectionist.png)

What are the differences between the systems that we have? The **current large language models** have great capabilities, we can use it for many things, but they have also issues. And so if we can compare what I'm talking about, these **symbolic approaches**, that use these symbols and rules, with what we have, which is like dominant results in current times.

So on one hand we have these **symbols and rules**, and on the other hand we almost have something like **feelings and intuitions**.

On one hand we have something that is able to find **patterns in huge amounts of data**. And on the other hand, we have something where we can put in a great rule set that will work. And it will work so well that it doesn't matter how big is the input.

**Mathematics is a symbolic method**. In maths, you can take equations and you can input an x and the x can go to infinity. And the equation will still work. It will still be great. While in the **neural networks**, this is not quite possible. You have always some kind of rotation. So always you are somewhere between minus one and one. And so you can’t really do something like this.

Large language models are **neural networks**. These neural networks take some floating point numbers, and they do some matrix operations, maybe a couple of extra operations on top of that. They produce vectors, like arrays of numbers, which form the [inner representation of the model (embeddings)](/ml/Embeddings-in-Machine-Learning-Explained). On the other hand, in computations, we have **hard symbols**, which are very different.

On the connectionist side, we have **neural networks and gradient boosting**, while on the **symbolic side**, we have **[decision trees](/ml/Neural-Network-Pruning-Explained)**. For example, you can see one on the top right. Decision trees operate only in the inputs, which is very interpretable and simple. And they have different capabilities and are used in specific type of situations.


## Problems with Symbolic Rule-based Expert Systems

![problems-with-symbolic-rule-based-expert-systems](/images/problems-with-symbolic-rule-based-expert-systems.png)

These algorithms, these computer programs, these rules, were actually used to be, it was a dominant approach in machine learning, in **artificial intelligence in 1980s**. And it seemed like if this is going to work, if we are just, you know, **AGI is just around the corner**, right? We are going to have it, like, tomorrow. And then there started to be issues. It wasn't progressing anymore. And so what these systems were doing, what was the approach back then? And why it collapsed?

Back then, the approach was that you would have even, like, dedicated hardware, like the one on the right, and you would write for your problem. You would **collect a group of experts** that would understand the domain. You would also have the **programmers that would be able to actually write the rules**. And over some time, you would build up the system, and it would actually work in some case. But it was expensive. It was very hard to update. If something changed, it was kind of a brittle.

In some domains, if you think about it, the experts don't actually really know what they are doing. They don't really know how to describe what they are doing. They a **tacit knowledge**, which is beyond words, or you would require to construct some new words, or have something **soft in between the words, between the symbols**.

While everything seemed great, the solutions were not able to get to the AGI. The dedicated hardware companies got into big issues where the hardware changed because there were new, more general systems. And also the different sort of approach that was leveraging neural networks, relying on more general hardware, more pop hardware, with more data, was starting to get traction. And so symbolics became mostly an abandoned approach.


## Connectionist Approaches After 1990s
![connectionist-approaches-1990-2020](/images/connectionist-approaches-1990-2020.png)

Then here came the neural networks. And there, researchers Hinton, Lecun, Bengio, led the neural network revolution in 2010. And this approach became so pervasive that, for example, people were saying, deep learning is just going to solve everything. This is it. We don't need symbolics. This is going to just solve everything.


People started to use **neural networks**, they were using **supervised learning** where you have labels, so you know what is the target. And in that case, there was this breakthrough in development of **AlexNet**, where suddenly it was possible to [classify images](/ml/Multimodal-Image-Text-Classification) with very good accuracy on this popular dataset, which, you know, before, how would you actually describe rules for images? Like how would you recognize what's in the image by using rules? It seems rather difficult. And it is. It was possible, it would have been not. But it's very difficult and very brittle.

There were also studies of **language**, and people started to build these **statistical models** of [representing words as these vectors](/ml/how-computers-understood-humans), as this array of floating point numbers.

For example, in 2013, there was a paper published in which actually one Czech researcher, whose name is **Mikolov**, participated in the research in a major way. And so this was an approach where you represented each word as one vector. Then over time, in 2017, **[transformers](/ml/transformers-self-attention-mechanism-simplified)**, where you could understand the entire context, where you input multiple words, you could actually understand sort of where you are in the space, not just in case for each word individually, but suddenly you were in some thought space that had many more dimensions, and it was possible to get good results with these. And people started predicting next word in web-scale datasets. We started getting interesting results.

Now we are just in the situation where we also implemented this **reinforcement learning from human feedback**, where we started hiring experts, and we are starting to get dedicated hardware, and **AGI is just behind the corner**, right? **Suddenly it sounds like something we heard before**. I mean, there may be some similarities. Is this really the final approach, or is this the final answer, or do we need to add something more?

**Reinforcement learning from human feedback**, that's a very interesting approach not the same as use of expert before the second AI winter. Now the experts don't have to actually write super complicated rules. Instead they just compare a text, and say this text is better than this text. While the experts get a bigger lever, and they have a much bigger impact. So this is a much more cost-effective approach. We are in a much better situation than before. **Hallucinations** are also reduced with this reinforcement learning from human feedback method. But we will see that you can get much more, like these other approaches of using symbols and being able to actually.


## Hybridizing Neural Networks with Algorithms

![hybridizing-neural-networks-and-symbolics](/images/hybridizing-neural-networks-and-symbolics.png)

These very scalable **symbolic approaches** of the algorithms and code that's so useful, and it seems to be so missing. It's definitely going to be applied. So what I think is necessary and what's increasingly being applied is **hybridizing both of these approaches**. So using both neural networks and symbolic approaches at the same time.

The **language models** already use the symbols. They use symbols as their input and as their output. So they are a combination a little bit in this sense. But you can go much further. We can, because the inputs are symbols and outputs are symbols, we can plug in the systems, we can plug in the algorithms.

One of the simplest ways how you can simulate **reasoning inside of the language models** is when you guide it with a prompt. It always tries to tell you the next word, then go to the next word. So you can guide it by writing it to the prompt. So before deciding this, let's think step by step. And with this, you will actually get improvement immediately. So you are already giving it this multistep process where it can iterate in some algorithmic way and you will get better results.

You can use language models to **fill in templates**. You can ask questions and then predict what word from these allowed words should be here? It just gives me some words and often it gives you the right answer.

**Self-consistency prompting** is another method. You combine again this language model and you request multiple results. In the paper **AlphaCode**, they produce many code samples and then they look, they sample from such samples that cluster together. They are very similar. And from the places where there are lots of similar samples, those actually, it works great if you sample from the biggest cluster the most.

**Toolformer** is another approach, released very recently. Here the language model sees the past, and it can predict the next token. What if it learned to exactly call something outside, but not in some template way? But instead here you can have it freely learn to ask a external function, an API. For example, if there is a question for some sort of calculation, and it sort of writes down some continuation, some text, and you can put a lot of small training sets, you can teach it to call a **calculate function**, which it can use to do the calculation for it. If it's not so good in doing some task, it can learn to call some external tool. It will get the results as into the text and instead of predicting the function output, it would get the output from the tool. It would sort of stop predicting for a couple tokens and get the result. With this you can improve actual performance on dedicated tasks for, you can do some question answering for you, to speed it up and so on.



## Hybrid Symbolic Connectionist Papers

![hybrid-symbolic-connectionist-papers](/images/hybrid-symbolic-connectionist-papers.png)

**AlphaZero**, where you have this chess playing engine, which gets superhuman. How does it do that? So it does learn from playing against itself. That's a very important part. But also the space of all the possible actions in chess. It's too big. It cannot go through everything. It has to go somewhere where it's interesting. How can you do that? You use **neural guided search**, where the network serves as an intuition. And it can sort of think about, okay, now I'm in this position, and I think I could do this. This sounds good, I could play this. And then it can, with self play, sort of go further into the direction, it can evaluate and learn, using this approach very effectively, and it becomes superhuman.

Then there is this **[RETRO transformer](/ml/DeepMinds-RETRO-Transformer-Model)**. So that one, instead of just having everything stored in its parameters, it actually stores as well the database of the training set, and it can retrieve on demand everything it saw during training. And of course, you know, it can generate queries on the internet and can give you the right summary of what you are asking.

I wanted to mention **[DreamCoder](/ml/dreamcoder-ai-wake-sleep-program-learning)**. This is a super intuitive idea of solving complicated coding problems by using libraries. This approach learns to build its own function library. In the first iteration, it solves simpler coding problems, stores the programs it found, and analyzes them using algorithms. It then finds the most interesting functions to remember and stores them in the library. This one combines the search and memory of building this library to solve coding problems.

You may be asking about [integrating images with text models](/ml/Multimodal-Image-Text-Classification)? You can do that as well. The image can be broken down into patches, detect things in the patches, and there is this paper, **ViperGPT**, which can reason on images by getting questions, generating Python code to answer the questions about the image, and then doing a course on the image using this code. It can count how many muffins there are in the image. It synthesizes code, which then calls detection of muffins, and then it just sums how many there are. The summation is simple; it's a couple of instructions, not trillions of matrix multiplications.

**Yann Lecun** was big on connectionist approaches, while recently he published a survey paper called **[Augmented Language Models](https://openreview.net/forum?id=jh7wH2AzKK)**. People are also asking, how exactly is the GPT bad? Can we find some set of problems on which the GPT completely fails while humans do great? If you want AGI, you want to be looking for something like this. You don't want to have hundreds of tasks, that's not interesting. For AGI, you have to have something like this. [**Francois Chollet** developed a dataset ARC](https://twitter.com/fchollet/status/1636054491480088823?s=20) on which GPT-3 got zero. GPT-4 is not evaluated yet, but they are developing further models, and we can read about that as well.


## OpenAI and Symbolics

![openai-and-symbolics](/images/openai-and-symbolics.png)

OpenAI are very good at **listening** and quickly improve based on feedback. What are the problems with their system? And right now, what seems to be their view is that this **reinforcement learning from human feedback** will solve most of the problems and will actually get them to **AGI**. So they have **smart researchers**. They know about this, but they think providing these **expert answers** and comparing will get them to AGI. But at the same time, they cannot scale it infinitely, because this is perhaps not enough. Because this reinforcement learning from human feedback equates to **expert labelling**.

The **cost for the labelling** is still not as costly as model training right now, but it's getting harder. As the model gets better at the tasks, it gets harder to evaluate the results. And so now they are thinking about using the **AI to assist** this reinforcement learning approach to help those experts to do the review. And it helps. This approach helps. It's again like iterating. It's **critiquing itself**. So it gets some tasks, and then the machine produces the answer and then criticizes the answer and then tries to improve the answer. And it displays it all to the evaluators, and the evaluators point out even more problems when they get this input. And so the idea would be eventually to have very minimal input, and the machine would be sort of through self-critiquing getting better and better with less input. So getting even **bigger lever to the experts**.


## People and Companies Working on Symbolics

![symbolics-companies-and-people](/images/symbolics-companies-and-people.png)

If you wanted to learn more about this, there are companies and people which publish things in this domain. For example, on Twitter, you can follow **Gary Marcus**, you can follow **Francois Chollet**, and other authors of the papers. Also, what I found interesting is that here in Prague, Czechia, there is also this startup called **Filuta AI**, which they are even explicitly thinking about composing AI, they want to use planning combined with that, with algorithms that can detect, provide these converts from this soft input into some hard symbols, and then do planning for companies. There is this company, **Replit**, which does coding tools. They want to iterate with programmers to have minimal input in creating software. There is also a **Equilibrium technologies**, they use reinforcement learning, but I think it's a little bit related. So you can find resources using the papers, and so on.

I think we will get to the **AGI** and what impact it will have on society. I'm not sure if we can get there. We are obviously improving the results, and this will have a huge impact. Can there be another **AI winter**? I wouldn't dismiss that completely. It's very easy to live in the bubble that everything is working great. What will be the **impact on society**? So here I think that people are now working on so many easy problems and they are not that challenged. I think people have huge abilities that they can achieve much greater things if they are required to.


## Questions and Answers

- Q: What specifically do you use or do in life? This was theoretical, so I would like to know what's involved. This is theoretical.
- A: We do use transformer architecture, because we have vision and language problems, so we use both. There is this collaborative group where you can see what, maybe a list of examples. And we have several things that we solve. It's the recommendation. It's very different, it's pretty much, very much symbolic, I would say, because it's very different sort of problem. And it naturally is more, less neural networks and more like scalable approaches, like symbolic. And yes, we also do similarity between the different types of images, so from search, yes.

- Q: Did you find anything that didn't work? Like, did you want to apply this?
- A: Yes. Well, in the industry, it's a lot about the cost. You have to think about, is it, how fast can I develop this? How expensive is it going to be? And I think it's great. In the previous presentations, it was very much mentioned. So it usually doesn't work in many scenarios. It's a lot about the cost. Like, you can get a huge, super-performance model, but if you cannot pay for it with what it's doing, then you cannot use it. But, yeah, like, hardware is getting cheaper, so, like, it's going to be more and more, like, moving forward.


## Update 2023-03-25

This talk was given on a Cleevio OpenAI meetup just a day before OpenAI announced ChatGPT plugins.