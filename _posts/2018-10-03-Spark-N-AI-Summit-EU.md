---
layout: post
title: "Spark and AI Summit"
date: 2018-10-03
---
# LIVE NOW UPDATED!


# ML Hydrogen
History of Spark origins. Strucutred Streaming is already used extensively. 

## ML Framework of spark

Two challenges communitcation between algos-spark and marring ML gang schedule vs Spark parallel.

- Initial approach: a python UDF applied row by row.
- Vectorized approach: execute a python UDF on batches of rows.

### Execution Models
Tasks are independent and completely paralel with no comms.
Distib ML needs task intercommunication - tasks are not completely parallel.

### Unification by project Hydrogen

- Load phase - independent tasks
- Gang phase - intercommunication
- Sink phase - independent tasks


# Zaharia Talk ML Flow

ML Livecyc:

- collect raw data
- prep data prep 
- train 
- deploy


Facebook, Uber, Google have custom standardization to hte livecycles, but they are limited to a few algos which where hand integrated and tied to companies infrasturct. Spark thus attempts to establish public standard allowing to integrate publically.

Introducing ML Flow:

- works with any ML lib and lan
- cross cloud support
- scales to big data

Example without ML Flow: 
- Running experiments with different params, versions, code changes.
- Dev looses understanding what happend and handing over is impossible.
- ML Flow adoption can track all above info by tracking ML jobs and allows reproduction


# Unified Analytics  

Challenges
- data not ready
- data is siloed
- dsci n deng are siloed

## D-Bricks Delta
Schema enforcement, ACID transactions, query perf, 

3# DBrics fruntime for ML
- LTS for OSS frameworks for ML engines

## Dsci n Deng siloes

eng givs platform to dsci.
dsci codes model scrip
deng deploys

## Example Dataflicks
uses mlflow, delta, ml runtime

issues iwth prediction
mlflow to analyze past perf
revert to older data
find non normalized data was loaded
review trasactions and rerun previous job but with normalized job

# Deep Dive Spark SQL

SQL: Structured Query Language
Schema: name, type, nullability
Structure importance: storage optimization, calc optimization tungsten
Basics


# Comon Stat Pitfalls In Dsci

Car stopping distance:
- L-reg regressing on to the other.
- lin reg speed -> distance or distance -> speed

Treatment A vs B:
- need to control for hard cases to find overall better treatment.
- on the other hand sometimes it is not good idea to control for that

Carboraters and axle ratio:
- non split data has one lin reg
- split has different correlation

Resolution of both is due to causation:
- humans reason via causation
- data may not contain causal info
- correct data inference requires causal model

Car stopping: speed causes stopping distance
Kidney stone size
-> Treatment -> outcome
-> outcome

Blood pH:
- treatment:
  -> pH
  -> outcome

Carbourators:
- Axle Ratio -> cylinders
- Carbourators -> cylinders

Recommended book: The Book Of Why:
- P(Y|X) != P(Y|do(X))


Smoking causal module:
- genes -> cancer; genes -> smoking -> tar -> cancer


Conclusion:
- caucality is critical
- confounding var
- PGM helps
- do calculus clarifies


# SimilarWeb Interaction-Based Feature Extraction

know unique user traffic 
have website when we know the user gender and website when we don't know
due to too many websites and users the problem is large
PCA or matrix factorization did not work
selected feature representing a bucket of gender distribution
projected the problem into that space and was able to resolve the problem
attempting to look at user level prediction was not possible due to large noise


# ABRiS

Integrates Spark with Avro.
Supports structures streaming, schema management, schema retention, Confluent Kafka Avro schemas, 

# OASIS—Collaborative Data Analysis Platform Using Apache Spark

improves over zeppelin: security and scale
extracted data can be vised and shared wihtin team 
will be OSSed soon


# Streaming Random Forrest

- streaming has extra challenges
- output is trained model

Stationary data: data distribution unknown but time static
Non-stat: unknown and time dynamic => features are dynamic

Labeling can be available early, delayed, categorize concept drift

## StreamingRandomForrest

StreamingDecisionTree: standard, intuitively splits seeing even small amount of data
Online bagging:

StreamingLogisticRegressionWithSGD has similar API
Training: 


# Indexing and Ranking via Spark

hard to understand for me personally

click through data
relevance - search term denoting ranking of the search results 

Idea of the method in the talk: 

rank datasets on Elasticsearch using LTR
extract relevance features
boostrap on dataset load time the search
...


# Spatio Temporal Modeling

...

factor analysis (looking for latent variables) - prelimirary regresison
time - auto correlation regression
spatial correlation
time - auto correlation regression
factor analysis (looking for latent variables) - prelimirary regresison

this single iteration across the domains gives good enough results


# Neo4J Morpheus 

Morpheus version of Neo4J.

Graph dbs have growing usage in the industry.
Nodes have name, properties and releationships. Relationships have type, properties.
Neo4J on some backend db like Hadoop, Hive, Spark.
Attempt to create GQL

## Example:

- Load CSV into Hive.
- Create views per realtionships.
- Init Cypher via query on relationships.
- Execute Neo4j graph merge tool.
- Query "match customer interact customerRep where type in cancel".

- Create new graph with same schema 

## Continuation

Graphs and tables can be loaded to Cypher queried and stored back to graph or table. Thus we can compose queries into other quieries. e.g. match socialNetwork sn match person p where p.email = sn.email

Process:
- graph matching: returns results
- graph construction: takes outputs and constructs new querable graph

RDMS vs Graph: nodes may have no props or relationships.

## Conclusion


Cypher: sql for graphs and start of gql
Cypher for spark: runs on spark SQL (dataframe)

