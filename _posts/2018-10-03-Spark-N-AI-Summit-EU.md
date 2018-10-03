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
