---
title: Symbolic vs Connectionist Machine Learning
description: Reason without hallucinations in large language models by hybridizing neural networks with code.
categories: ml
date: 2023-03-23
last_modified_at: 2023-06-11
image: /images/symbols-patterns-hybrids.png
layout: post
permalink: /:categories/:title
video: aByQezRCJUE
my_related_post_paths:
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2024-02-20-Synthetic-Data-for-LLM-Training.md
- _posts/2021-04-27-dreamcoder-ai-wake-sleep-program-learning.md
- _posts/2023-08-25-How-Deep-Neural-Networks-Learn.md
- _posts/2022-04-10-googles-pathways-language-model-and-chain-of-thought.md
- _posts/2023-12-17-If-I-Brainstorm-Am-I.md
- _posts/2022-09-11-Embeddings-in-Machine-Learning-Explained.md
---

{% include load_video.html %}

Today I would like to tell you what is **increasingly becoming popular in large language models**. What I think will be a future of this field that could potentially provide some things I think are missing for us perhaps to get to the **artificial general intelligence**. As defined, maybe as a system that can do as many things as, for example, an average person in 2022.


## Large Language Model's Hallucinations and Poor-Reasoning

{% include image.html src="/images/large-language-models-hallucinations-and-poor-reasoning.png" alt="large-language-models-hallucinations-and-poor-reasoning" %}

What are the **missing things in current systems**? So now we burn through a gajillion, it’s like trillions of floating point operations with all these multiplications and we still get **hallucinations** and we still get quite **poor reasoning capabilities**. And there are approaches reducing these judgement deficiencies, but something still seems to be missing.

Yes, it’s true that humans as well hallucinate. For example, you may have a **false memory**, so maybe you don’t remember everything perfectly. For example, if there is a crime, oftentimes the people have actually different accounts.


### How Humans Reduce Hallucinations and Improve Reasoning

We already developed approaches how to deal with these issues. We write down **symbols** and into the symbols we can even encode **rules**. And the rules can operate on the symbols and it’s like a perfect system. It was super successful in understanding the world because we used it to create **mathematics**, which was used for **accounting, physics, and engineering**.

Because we can write things down and they don’t disappear, they stay the same. It’s an **immutable storage**. We can also think about the things multiple times. And another thing that perhaps is also important is that we can **act in the world** and so we can **sample new data** and learn new things from experience.


These **successful symbolic tools** were then later used to develop computer programs which are also rules, which operate on symbols. So the same way we actually built these computers which take something that's **crystal perfect** and it can produce something that's still crystal perfect. And while all at the same time this seems to be missing in the **language model**, this sort of aspect is not quite there.

## Symbolic vs Connectionist Methods Comparison
{% include image.html src="/images/intuition-symbolic-vs-connectionist.png" alt="intuition-symbolic-vs-connectionist" %}

What are the differences between the systems that we have? The **current large language models** have great capabilities, we can use it for many things, but they have also issues. And so if we can compare what I'm talking about, these **symbolic approaches**, that use these symbols and rules, with what we have, which is like dominant results in current times.

So on one hand we have these **symbols and rules**, and on the other hand we almost have something like **feelings and intuitions**.

On one hand we have something that is able to find **patterns in huge amounts of data**. And on the other hand, we have something where we **can put in a great rule set** that will work not matter how big is the input.

**Mathematics is a symbolic method**. In maths, you can take equations and you can input an x and the **x can go to infinity**. And the equation will still work. It will still be great. While in the **neural networks**, this is not quite possible. You have always some kind of limitation. So always you are somewhere between **minus one and plus one**. And so you can’t really do something like this.

**Large language models are neural networks**. These neural networks take some floating point numbers, and they do some **matrix operations**, maybe a couple of extra operations on top of that. They produce vectors, like arrays of numbers, which form the [inner representation of the model (embeddings)](/ml/Embeddings-in-Machine-Learning-Explained). On the other hand, in **efficient algorithmic computations, we have hard (discreet) symbols**, which are very different.

On the connectionist side, we have **neural networks and gradient boosting**, while on the **symbolic side**, we have **[decision trees](/ml/Neural-Network-Pruning-Explained)**. For example, you can see one on the top right. Decision trees operate only in the inputs, which is very interpretable and simple. And they have different capabilities and are used in specific type of situations.

The analogy can be extended also to: **Statistical models** on the connectionist side vs **computational models** on the symbolic side. And parametric vs non-parametric models.


## Problems with Symbolic Rule-based Expert Systems

{% include image.html src="/images/problems-with-symbolic-rule-based-expert-systems.png" alt="problems-with-symbolic-rule-based-expert-systems" %}

These algorithms, these computer programs, these rules, were actually used to be, it was a dominant approach in machine learning, in **artificial intelligence in the 1980s**. And it seemed like if this is going to work, if we are just, you know, **AGI is just around the corner**, right? We are going to have it, like, tomorrow. And then there started to be issues. It wasn't progressing anymore. And so what these systems were doing, what was the approach back then? And why it collapsed?

Back then, the approach was that you would have even, like, dedicated hardware, like the one on the right, and you would write for your problem. You would **collect a group of experts** that would understand the domain. You would also have the **programmers that would be able to actually write the rules**. And after enough effort, you would build up the experts system, which would be acceptable in some cases. But it was expensive. It was very difficult to update. If something changed, it would fall apart.

In some domains, if you think about it, the experts don't actually really know what they are doing. They don't really know how to describe what they are doing. They have a **tacit knowledge**, which is beyond words, or you would require to construct some new words, or have something **soft in between the words, between the symbols**.

While everything seemed great, the solutions were not able to get to the AGI. The dedicated hardware companies got into big issues where the hardware changed because there were new, more general systems. And also the different sort of approach that was leveraging neural networks, relying on more general hardware, more pop hardware, with more data, was starting to get traction. And **symbolics were mostly abandoned**.


## Connectionist Approaches After 1990s
{% include image.html src="/images/connectionist-approaches-1990-2020.png" alt="connectionist-approaches-1990-2020" %}

Then here came the neural networks. And there, researchers Hinton, Lecun, Bengio, led the neural network revolution in 2010. And this approach became so pervasive that, for example, people were saying, deep learning is just going to solve everything. This is it. We don't need symbolics. This is going to just solve everything.


People started to use **neural networks**, they were using **supervised learning** where you have labels - you know what is the target. And in that case, there was this breakthrough in development of **AlexNet**, where suddenly it was possible to [classify images](/ml/Multimodal-Image-Text-Classification) with very good accuracy on this popular dataset ImageNet. Before this, how would you recognize what's in **the image by using rules?** It seems rather difficult. And it is. It is possible, but it's very difficult and very brittle. On the other hand, **neural networks can statistically find the patterns**.

There were also studies of **language**, and people started to build these **statistical models** of [representing words as these vectors](/ml/how-computers-understood-humans), as this array of floating point numbers.

For example, in 2013, Czech researcher **Mikolov** co-published Word2Vec paper (later also [FastText](/ml/FastText-Vector-Norms-And-OOV-Words)). Word2vec is a method to represent each word as one vector. Then in 2017, **[transformer architecture](/ml/transformers-self-attention-mechanism-simplified)** was able to accept multiple words. These models are able to [represent entire paragraphs of text in context as a vector](/ml/how-computers-understood-humans), and not only each word individually. . In particular, people started predicting (inferring) next word in web-scale datasets and getting high accuracies and high [text compression](/ml/neural-data-compression).

Now we are just in the situation where we also implemented this **reinforcement learning from human feedback (RLHF)**, where we started hiring experts, and we getting dedicated hardware, and **AGI is just behind the corner**, right? **Suddenly it sounds similar to what we already heard**. I mean, are we in 2023 just before another AI winter? Is this really the winning approach, is this the final answer, or do we need to add something more?

**Reinforcement learning from human feedback**, that's a very interesting approach not the same as use of expert before the second AI winter. Now the **experts don't have to actually write super complicated rules, instead they just compare a texts**, and say this text is better than this text. While the experts get **a bigger lever**, and they have a much bigger impact. So this is a much **more cost-effective approach**. We are in a much better situation than before. **Hallucinations** are also reduced with this reinforcement learning from human feedback method. But we will see that you can get much more, like these other approaches that are using symbols.


## Hybridizing Neural Networks with Algorithms

{% include image.html src="/images/hybridizing-neural-networks-and-symbolics.png" alt="hybridizing-neural-networks-and-symbolics" %}

These very scalable **symbolic approaches** of the algorithms and code that's so useful, and it seems to be so missing. It's definitely going to be applied. So what I think is necessary and what's increasingly being applied is **hybridizing both of these approaches** - using both neural networks and symbolic approaches at the same time.

The **language models** already use the symbols. They use symbols as their input and as their output. They are a combination a little bit in this sense. But you can go much further. We can, because the inputs are symbols and outputs are symbols, we can plug in the symbolic algorithms (heuristics).

One of the simplest ways how you can simulate **reasoning inside a language model** is by [guiding it with a prompt](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM). The model always infers distribution over the next word, then it selects one, and go to the next word. You can create a sort of momentum towards a solution by writing [an instruction prompt](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM) "let's **think step by step**". By allowing the model to generate and read its own "thoughts", you get an improvement in accuracy of the final answer. This is a multistep process, a [chain of though](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM), where the model can review what it inferred in a bit of algorithmic computational model way to get better results.

You can **fill in templates (forms)** with language models. You just ask what word from these allowed words should be here? It just gives me some words and often it gives you the right answer.

[**Self-consistency prompting**](/ml/Prompting-Techniques-That-Sqeeze-The-Best-Out-of-Your-LLM) is another method in which request multiple results using the chain-of-thought method. In the paper **[AlphaCode](https://arxiv.org/abs/2203.07814)**, they produce many code samples, and they sample from the most common samples. From similar samples that cluster together. And from the places where there are lots of similar samples, those actually, it works great if you sample from the biggest cluster the most.

**[Toolformer](https://arxiv.org/abs/2302.04761)** is large language model tool-augmentation method, published in 2023. Because the language model sees the past, and it can predict the next token. What if it learned to generate a call to something outside? Toolformer learns how to ask an external function, an API interface. For example, if Toolformer needs a arithmetic calculation, then you can teach it to call a **calculator function**. This external system which it can use to do the calculation precisely and return the result. Language models are not so good for calculation tasks, but you can train them to call some external tool. The calculator results are appended the text context. With Toolformer you can improve performance on tasks in which information search or a program execution helps.

Also [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) which recursively plans tasks, and performs them, is gaining traction.



## Hybrid Symbolic Connectionist Papers

{% include image.html src="/images/hybrid-symbolic-connectionist-papers.png" alt="hybrid-symbolic-connectionist-papers" %}

**[AlphaZero](https://arxiv.org/pdf/1712.01815.pdf)**, where you have this chess playing engine, which gets superhuman. How does it do that? So it does learn from playing against itself. That's a very important part. But also the space of all the possible actions in chess. It's too big. It cannot go through everything. It has to go somewhere where it's interesting. How can you do that? You use **neural guided search**, where the network serves as an intuition. And it can sort of think about, okay, now I'm in this position, and I think I could do this. This sounds good, I could play this. And then it can, with self play, sort of go further into the direction, it can [evaluate and learn](https://www.inference.vc/alphago-zero-policy-improvement-and-vector-fields/), using this approach very effectively, and it becomes superhuman.

Then there is this **[RETRO transformer](/ml/DeepMinds-RETRO-Transformer-Model)**, which instead of just having everything stored in its parameters, it actually stores as well the database of the training set, and it can retrieve on demand everything it saw during training. And of course, you know, it can generate queries on the internet and can give you the right summary of what you are asking.

I wanted to mention **[DreamCoder](/ml/dreamcoder-ai-wake-sleep-program-learning)**. This is a super intuitive idea of solving complicated coding problems by using libraries. This approach learns to build its own function library. In the first iteration, it solves simpler coding problems, stores the programs it found, and analyzes them using algorithms. It then finds the most interesting functions to remember and stores them in the library. This one combines the search and memory of building this library to solve coding problems.

You may be asking about [integrating images with text models](/ml/Multimodal-Image-Text-Classification)? You can do that as well. The image can be broken down into patches, detect things in the patches, and there is this paper, **[ViperGPT](https://viper.cs.columbia.edu/)**, which can reason on images by getting questions, generating Python code to answer the questions about the image, and then doing a course on the image using this code. It can count how many muffins there are in the image. It synthesizes code, which then calls detection of muffins, and then it just sums how many there are. The summation is simple; it's a couple of instructions, not trillions of matrix multiplications.

**Yann Lecun** was big on connectionist approaches, while recently he published a survey paper called **[Augmented Language Models](https://openreview.net/forum?id=jh7wH2AzKK)**. People are also asking, how exactly is the GPT bad? Can we find some set of problems on which the GPT completely fails while humans do great? If you want AGI, you want to be looking for problems like this. You don't want to have hundreds of same tasks, that's not interesting. For this reason [**Francois Chollet developed a dataset ARC**](https://twitter.com/fchollet/status/1636054491480088823?s=20) on which GPT-3 got zero score. GPT-4 is not evaluated yet, but they are developing a new version of the dataset.


## OpenAI and Symbolics

{% include image.html src="/images/openai-and-symbolics.png" alt="openai-and-symbolics" %}

OpenAI as an organization are very good at listening and **quickly improving based on feedback**. What are the problems with their system? And right now, what seems to be their view is that this **reinforcement learning from human feedback** will solve most of the problems and will get them to **AGI**. They have **smart researchers** and know these arguments, but they think providing these **expert comparisons with RLHF** will get them to AGI. But at the same time, they cannot scale this infinitely, because this solution requires to **expert labelling**.

The **cost for the labelling** is still not as high as the model training right now, but it's getting harder day by day. As the model gets better at the tasks, it gets harder to evaluate the results. And so now they are thinking about using the **AI to assist** this reinforcement learning approach to help those experts to do the review. They are using the model to **[critique itself](https://arxiv.org/abs/2206.05802)** (or [self-reflect](https://arxiv.org/pdf/2303.11366.pdf)). The machine is assigned as task, and then it produces an answer, and then it criticizes the answer, and then tries to improve the answer based on the criticism. And it displays it all to the evaluators, and the evaluators point out even more problems when they get this input. And so the idea would be eventually to have very minimal input, and the machine would be improving of through increasingly automated self-critiquing. Getting better and better with less and less input from humans. This gives even **bigger lever to the experts**.


## People and Companies Working on Symbolics

{% include image.html src="/images/symbolics-companies-and-people.png" alt="symbolics-companies-and-people" %}

If you wanted to learn more about this, there are companies and people which publish things in this domain. For example, on Twitter, you can follow **[Gary Marcus](https://twitter.com/GaryMarcus)**, you can follow **[Francois Chollet](https://twitter.com/fchollet)**, and other authors of the papers. Also, what I found interesting is that here in Prague, Czechia, there is also this startup called **[Filuta AI](https://filuta.ai/)**, which they are even explicitly thinking about composing AI, they want to use planning combined with that, with algorithms that can detect, provide these converts from this soft input into some hard symbols, and then do planning for companies. There is this company, **Replit**, which does coding tools. They want to iterate with programmers to have minimal input in creating software. There is also a **[Equilibre technologies](https://www.equilibretechnologies.com/)**, they use reinforcement learning, but I think it's a little bit related. So you can find resources using the papers, and so on.

I think we will get to the **AGI** and what impact it will have on society. I'm not sure if we can get there. We are obviously improving the results, and this will have a huge impact. Can there be another **AI winter**? I wouldn't dismiss that completely. It's very easy to live in the bubble that everything is working great. What will be the **impact on society**? So here I think that people are now working on so many easy problems and they are not that challenged. I think people have huge abilities that they can achieve much greater things if they are required to.


## Questions and Answers

- Q: What specifically do you use or do in life? This was theoretical, so I would like to know what's involved. This is theoretical.
- A: We do use transformer architecture, because we have vision and language problems, so we use both. There is this collaborative group where you can see what, maybe a list of examples. And we have several things that we solve. It's the recommendation. It's very different, it's pretty much, very much symbolic, I would say, because it's very different sort of problem. And it naturally is more, less neural networks and more like scalable approaches, like symbolic. And yes, we also do similarity between the different types of images, so from search, yes.

- Q: Did you find anything that didn't work? Like, did you want to apply this?
- A: Yes. Well, in the industry, it's a lot about the cost. You have to think about, is it, how fast can I develop this? How expensive is it going to be? And I think it's great. In the previous presentations, it was very much mentioned. So it usually doesn't work in many scenarios. It's a lot about the cost. Like, you can get a huge, super-performance model, but if you cannot pay for it with what it's doing, then you cannot use it. But, yeah, like, hardware is getting cheaper, so, like, it's going to be more and more, like, moving forward.


## A Warning from Socrates

"Their trust in writing, produced by external characters which are no part of themselves, will discourage the use of their own memory within them. You have invented an elixir not of memory, but of reminding; and you offer your pupils the appearance of wisdom, not true wisdom, for they will read many things without instruction and will therefore seem [275b] to know many things, when they are for the most part ignorant and hard to get along with, since they are not wise, but only appear wise."
(source: [Plato, Phaedrus](https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0174%3Atext%3DPhaedrus%3Apage%3D275#:~:text=For%20this%20invention%20will%20produce,their%20own%20memory%20within%20them.))


## Update 2023-03-25

This talk was given on a [Cleevio OpenAI meetup on 2023-03-22](https://youtu.be/9TdvsdFX0O0?t=5348) just a day before OpenAI announced ChatGPT plugins.


## Update 2023-04-20

AutoGPT became extremely popular Github project.