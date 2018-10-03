---
layout: post
title: "Spark and AI Summit"
date: 2018-10-03
---
# LIVE NOW UPDATED!

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


