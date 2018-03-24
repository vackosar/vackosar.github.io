---
layout: post
title: "Notes: Prague ML 2018: Day 1: Workshops"
date: 2018-03-23
---
    
Classification of finger prints using Mathematica.


## Intro To Mathematica
Basics of the syntax and usage of the Mathematica program using 14 days trial versions.


## Training

[Fingerprint data](http://academictorrents.com/details/d7e67e86f0f936773f217dbbb9c149c4d98748c6) with labels for finger type and gender.
Network used Inception V3 pretrained Image network. 


### Classify Superfunction
First approach is passing training data to create classifier to [Classify function](https://reference.wolfram.com/language/ref/Classify.html). Mathematica also supports usage of GPU inclusing CUDA framework. With general classifier we can classify with accuracy 83% based on gender, but confusion matrix (Precision/recall?) shows that there were no female finger prints predicted, which in incorrect. The data probably is skewed towards male.

# Gesnim

## Bag Of Words
Bag of words. Counting words in documents.


documents

1 ,2 ,3
cat| 1 | 0 | 0 | 3
dog| 0| 1| 

~ embedding * docs


Many possible decompositions. For example eigen vector decomposition. Done for compression purposes. 
We get latent singular decomposition (vectors of singular value decomposition.)

LSI model. Example choose 300 topics leading to 300 dimensinal space.



## Word2Vec

basics explained and examples using gensim framework


## Fast text

basics - using subword segments - ngrams.



