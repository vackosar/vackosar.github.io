## Meta Notes

Sound wasnt very good. considering this is a concert room I suspect not good setup of the reproductors rather than problem wiht the space.


## Inverse Reinforcement Learning

Learning reward function usually and not the policy function. In general it is very difficult, since the agents can have long term strategies. Experimented with in self-driving cars.


## Anomaly detection in health care

- outlires and rare events.
- observe all metrics at once and monitor outliing results.
- training anomaly detenction is usually hard due to small amout of anomalies
- clustering
- via prediction where anomalies are prediction divergence
- frequentist: the most common values are not anomalies
- wave function collapse algo modified for time series of multiple values (collecting tiles and fitting them to the observed values)


## Topological Approaches for Unsupervised Learning 

2 dim manifold is a line. Since we have only datapoints we use simplexes ie. we connect those points that are close together.
Cyril: Manifold learning.
Applied Topology book
@leland_mcinnes


## Horovod async learning

Better make device bigger than model or cut the model to small pieces.
Problem with param server async learning is that server is bottle neck.
All reduce model is popular and has variants of inter-learner-node communication: p2p, hierarchical.
Horovod is faster than old Tensorflow but there comparable performant distributed learning now in new Tensorflow.

