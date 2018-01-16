---
title: "Santiago, Chile"
thumbnail: /gallery/santiago_thumb.jpg
layout: scenario
---
Santiago, the capital city of Chile, has a total population of 6 million people in an area of 641
square kilometers, which makes it by far the most populated city of Chile. The city suffers from air
pollution due to emissions from fixed and mobile sources, which particularly in the winter season
concentrate in the Santiago Valley.

The MATSim Santiago scenario was built upon three open data sources:

1.  Car network information from OpenStreetMap,
2.  Public transport supply data in Google Transit Feed Specification (GTFS), and
3.  Travel diaries from Santiago's 2012 Origin-Destination Survey.

In its first part, the simulation video shows the activities of the 1% population being
carried out in each time, where red dots represents “home” activities while blue dots
represents “work”, two of the most important ones. Secondly, the video shows the movement of
the car and public transport vehicles along the network of the scenario.

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/57yHpjfrpUM" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

Different runnable versions of the scenario are available under
<https://svn.vsp.tu-berlin.de/repos/public-svn/matsim/scenarios/countries/cl/santiago/>. It is planned
that the latest version will be continuously improved by MATSim community researchers. Recent
improvements include:

1.  Usage of population expansion factors from the 2012 Origin-Destination Survey to generate a 1%
    and a 10% sample population.
2.  Randomizing activity locations of the expanded agents, using official land registry data.
3.  Generating more variability in the agents’ trip start times, using smartcard transit data
    (known as Bip!).
4.  Integrating tolls on the tolled highways.
5.  Integrating shared taxis (colectivos) into the simulation.

The scenario is typically calibrated with respect to modal split and traffic volumes using
manual and automatic calibration methods.

The sole use of open data sources and the continuous stepwise scenario improvement process
makes MATSim Santiago one of the most complete scenarios that are freely available for
researchers worldwide. It might become a role model for administrations all around the world
to realize the power of open data initiatives when it comes to transparent decisionmaking
and the stimulation of innovation activity in the private sector.

