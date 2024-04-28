---
layout: post
title: Simulation of Soft Photon Calorimeter
date: 2011-07-29
description: Understand how an electromagnetic calorimeter works presented at Dubna JINR 2011.
image: /images/sim-of-soft-photon-calorimeter.png
categories: physics
permalink: /:categories/:title
redirect_from:
- /2011/07/29/Simulation-of-Soft-Photon-Calorimeter.html
slides: WT4Pkb7QSug6N
last_modified_at: 2022-04-16
my_related_post_paths:
- _posts/2010-09-05-Transverse-momentum-spectra-and-correlations-in-the-blast-wave-model-with-resonances.md
- _posts/2011-09-24-Feynman-summation-in-finite-dimensional-quantum-mechanics.md
- _posts/2019-08-28-1D-Kalman-Is-Exponential-Or-Cumulative-Average.md
- _posts/2021-10-04-electra-4x-cheaper-bert-training.md
- _posts/2023-10-23-create-your-google-calendar-event-link-in-seconds.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2020-08-21-Brutalist-and-Modernist-Architectures-Collide-at-Sunshine-Plaza-in-Prague.md
---



{% include load_slides.html %}

[Download PDF](/files/soft-photon-calorimeter-jinr-dubna-student-practice.pdf)


### Presented At
2011 JINR, Dubna Student Practice

### Notes

Students
- Vaclav Kosar Czech Technical University in Prague
- Viktor Burian Czech Technical University in Prague
- Andra-Georgia Ibanescu University of Bucharest

Leads
- Igor Rufanov
- Elena Kokoulina
- Vladimir Nikitin

Goals
- To understand photon production and it’s importance for collective phenomena explanations.
- To get familiar with GEANT, PYTHIA, PAW
- To simulate the spectra of photons produced in high energy collisions
- To understand how a electromagnetic calorimeter works.
- To simulate the energy deposition spectra of photons in a calorimeter.

Isotropical with energy distribution:
- capability to measure low energy deposit E < 5 MeV
- the dimension of one cell 4 x 4 x 120 cm 3
- localization of photon σ < 2 cm.

The electromagnetic calorimeter
Red - BGO crystals
Blue - organic scintillator - cutting the charged particles
Green - Veto - energy leakages

In spite of small dimension of detector it allows one to detect low energy photons with small background contribution from high energy particles.
This is achieved due to VETO detector and measurement of location of incoming photons.
Signal of soft photons is detectable for cross section of several mb, according to the simulation.

Generate total momentum of photons in CMS
Generate the direction of photons in CMS
Calculate the photons momentum in LS
Calculate energy of photons in LS



### Authors

- Vaclav Kosar @ CVUT
- Viktor Burian @ CVUT
- Andra-Georgia Ibanescu @ University of Bucharest