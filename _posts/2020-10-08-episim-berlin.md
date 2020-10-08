---
layout: post
author: Ricardo Ewert
title: "EpiSim with MATSim"
summary: "With MATSim it possible to simulate the spread of Covid-19"
---


Dear MATSim-Community,

In this post we want to shortly present MATSim-EpiSim of the MATSim group in Berlin. Episim is an open source framework which can be used to simulate, based on MATSim events, an epidemic outbreak. 

In EpiSim we attach an infection model to the already existing mobility model. Agents can infect each other if they are simultaneously in the same facility or vehicle. If two agents have contact, the probability of infection depends on the following parameters:

- duration (comes directly from mobility model)

- contact intensity (depends on room size and air exchange)

- mask usage

- location: indoors or outdoors

For COVID-19, EpiSim uses a disease progression model taken from literature. This means that an infected agent may transition to showing symptoms or requiring hospital or intensive care with certain probabilities and that agents can go into quarantine. 

EpiSim can be used to investigate the effects of non pharmaceutical interventions. These include the reduction of out-of-home activities (for example closing of schools), reduced use of public transport, wearing of masks, contact tracing and reduced disease import. Current simulation results for Berlin can be found here: https://covid-sim.info 

For more details, see the following preprint: [https://doi.org/10.1101/2020.07.22.20160093](https://doi.org/10.1101/2020.07.22.20160093).
 
![Epidemic spread example for Berlin](/gallery/EpiSim_Berlin.png)
