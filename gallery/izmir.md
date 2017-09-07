---
title: "Izmir, Turkey"
thumbnail: /gallery/izmir_thumb.png
layout: scenario

image1:
  image: /gallery/izmir_1.jpg
  caption: "Satellite view of Izmir, Turkey"

image2:
  image: /gallery/izmir_2.jpg
  caption: "Three gulf crossing scenarios for Izmir, Turkey"
    
---
{% include image.html image=page.image1 %}

A simulation for existing urban transportation, and three simulations for gulf crossing scenarios, for Izmir, Turkey are made using MATSim. Simulation results for existing urban transportation are compared to count station results to determine verification ratios. Simulation results for gulf crossing scenarios are used to determine the effects of different scenarios to existing traffic.

{% include image.html image=page.image2 %}

Road network is converted from OpenStreetMap and modified manually. Analyzed TAZs, land use and urban automobile traffic data is obtained from Izmir Metropolitan Municipality transportation master plan. Izmir urban traffic is distributed to 47 internal zones according to land use information.

Best gulf crossing scenario is determined using simulation results, choosing the crossing which has minimum negative effects (increasing volume) to links which it is connected to and maximum positive effects (decreasing volume) to links which are at upper limits of their capacities, taking infrastructural investment requirements into consideration.

#### Research paper

- MATSim-T Urban Traffic Simulation for Izmir, TURKEY. MUTLU, M. Metin, Graduation Thesis in Civil Engineering. 
Supervisor: ALVER, Yalçın, Assistant Prof. Dr., February 2010

