---
layout: post
title: "Notes: Prague ML 2018: Day 2: Talks"
date: 2018-03-24
---

# Intro to conference
Organizers mention that the conference is growing rapidly from 300 in 2016. Explains that they value experts opposed to advertizing talks.

Silicon valley - Europe investing AI company CEAi presents their strategy in investing into ai startups, eu talent and connecting to sillicon valley. Notes also that ai favours big players thanks to expensive computation and data.

# Magin in the machine, Google
Google presenter talks generally about genenrally about ML and Googles role in this area.


# Wolfram
Presentation of AutoML features of Mathematica. Significantly simpler to Keras, large library of architectures and exportable to AutoMX Net. Underlying framework is the fastest on the market AutoMx. Should also provide customizability throught api.


# Automating ML

Simplify ML and speedup in company called BigML.

## Bayesian Param Optimization
There are various frameworks looking for optimal structures for given data attempting to automate e.g. skicit.

## Other
metaalearning,hyperbadn

## Benchmarking
broadness of dataasets, select broad metrics

## Submodularity

Param Spaces are the new params. Cannot try all possiblities. 

## Ensuring interaction with user during optimizing
Automation is not enough. We need to also communicatte with the user to provide more data, evaluate, verify, reevaluate contraints or preferences.


# Ebay Recommenders and chat bots

Description of uses cases in Ebay. It seemed that they try to apply everything others do as well.

# Adobe Recommenders

History of recommender systems techniques and strategies.

# Gurantted Display Advertising

Customer needs to show ad to certain number of members of an age group with particular interest.
Sales person needs to be able to estimate price tag for given task.

Use history and make prediction. Decision needs to include: web page, cotext, region, based on info about user, based on his device. One month of logs takes 10minutes to process. 

Users are split into sub groups based on interests and estimation is then performend on them. User split is done using principal component analysis. UsedStreaming pattern discovery in multiple ... paper. 

Collected features, web pages and designeded 1 hour time slot. Based on number of hits in given slots created vectors. Also separated into time series in order to predict distribution across week, and day hour. Predicted then results and performed analysis of the performance. Results were quite acurrate.

# Deep Learning Revolution, Audi
Overview of deep learning and current performance. Style transfer, face transfer, Long Short Term Memory, Self Normalizing Nets (Selu), Two time scale GAN, Reinforcement network. 

# Alquist Chat bot
## 2017
- Recongnize intent.
- Entity recognition. Gather lists and attempt to match those.
- Context
- Dialog manager. Directed graph of topics where driver decides which route to go.
- Db with API to access general info.

## 2018 upgrades
Move from topics to entities. Dialog manager decides based on dialogue acts and entities.

# Quantum Computing
Accelaraates computing for osme tasks e.g. eigenvalues, dialognalization, prime decomposition.


