---
layout: post
title: "Simulation of Soft Photon Calorimeter"
date: 2011-07-29
description: Understand how an electromagnetic calorimeter works presented at Dubna JINR 2011.
image: /images/sim-of-soft-photon-calorimeter.png
categories: physics
permalink: /:categories/:title
redirect_from:
- /2011/07/29/Simulation-of-Soft-Photon-Calorimeter.html
slides: WT4Pkb7QSug6N
last_modified_at: 2022-04-16
---

{% include load_slides.html %}

[Download PDF](/files/soft-photon-calorimeter-jinr-dubna-student-practice.pdf)

### Authors

- Vaclav Kosar @ CVUT
- Viktor Burian @ CVUT
- Andra-Georgia Ibanescu @ University of Bucharest

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
