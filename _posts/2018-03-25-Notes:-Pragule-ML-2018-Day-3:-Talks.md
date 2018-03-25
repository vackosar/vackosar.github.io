---
layout: post
title: "Notes: Prague ML 2018: Day 3: Talks"
date: 2018-03-25
---

# Deploying Text ML in a Bank
Analyzer of news and legal data.

## Before
search for a name together with keywords.
Use top k results.

## New ML approach
Merlon intelligence 
goal: ranking, remove false positives, 
baseline: split into sentences, search for entities and co-occuring keywords.
Rnn trained performed well even on small amount of data and further training improves results even more.
Needed to use unsupervised: ladder networdsk, sequence leaarning.
Tensorflow. traning with python, prediction with scala.


# Calibrating Browsing Data, Jumpstart
There are many biases in browsing data. Major one is sampling bias.
Analyzing user interaction with websites using Spark. LSA topic modeling is unsupervised algo. Clustering users per group gives nicely clustered results.

User clustering using hierarchical clustering. The clustering is not used in production pipeline.

Identify groups and then assign corrective weights to avoid sampling bias.
For example we dont know no of people interested in politics, we do know only number of people visiting a website.


# Social Good at Cloud Scale, Microsoft
Implemented libs shared on Github.
`
## Libya
Measuring aid impact in Libya from distance avoiding biased media.
Use multiple sources, Twitter,  FAcebok, RSS.
Proceeesss PySpark. Tag sentiment, location, keywords. Display heatmaps.
Mapbox, autotranslation, Comproimise app for entity logging, Databricks on Azure may improve perf. In future use GraphL.

## Ghana
Tracking mining in Ghana. Transfer learning as a service. Kubernetes, Redis.

## X
Cognitive Services, FaceNet, Face_recognition.
Facerecog with DLusing convnet feaature maps to produces  vectors of facial featutres. Comparing featuree vectors using L2.


# Optimizing data center, DHL
Modeling overall satifaction based on bayesian networks.


# Spaceknow

## Indexes on Bloomberg
Estiamting gdp of african countries based on light index.
Estimating china industry based on satelite images.

# O2

Using word2vec on cell ids tracked from opt in customers (cell2vec). Used 100dim.


# Data Programming, CEAi

Important is to have proper versioning and tools in data science.
Example: Snorkel tool is useful notebook based on Zeppelin.

Data Version Control is versioning tool for data used a plugin for Git for reproducibility and sharing.

Private platfrom Sensei is platform for solving common problems with versioning and so on. It aims to link code, output and input data which would be all backed up. Sensei would also like to add automatic hyperparam optimization, annotators, active learning.
