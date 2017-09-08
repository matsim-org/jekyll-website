---
title: "Gauteng, South Africa"
thumbnail: /gallery/gauteng_thumb.png
layout: scenario
  
---

Gauteng is the smallest province in South Africa, accounting for around 2% of the land surface, but contributes more than a third of the country's Gross Domestic Product (GDP). Due to high urbanization (the three metropolitan cities of Johannesburg, Tshwane (Pretoria) and Ekurhuleni form part of Gauteng) the province has around 11 million inhabitants.

<iframe allowfullscreen="" frameborder="0" height="468" mozallowfullscreen="" src="https://player.vimeo.com/video/138598873" webkitallowfullscreen="" width="100%"></iframe>


The scenario is currently built by researchers led by Prof. Johan W. Joubert at the Department of Industrial and Systems Engineering at the University of Pretoria in South Africa. The groundwork for the scenario was laid during a two-month stay of a Master student (Pieter J. Fourie) from South Africa in Berlin during 2008, where the essential steps of preparing the network, travel demand, and traffic counts for validation, were done. Network data and zonal information was imported from GIS Shapefiles. Travel demand is based on census information. In an initial step, only travelers commuting via private car were simulated, leading to the well-recognizable morning and evening rush hours.

The model has since been extended ([Joubert et al., 2010](http://dx.doi.org/10.3141/2168-04)) to include freight agent activity chains, allowing for traffic throughout the day.

Recently the model was used to evaluate the impact of the [Gauteng Freeway Improvement Project (GFIP)](http://www.nra.co.za/gfip/). Specifically, the South African National Roads Agency Limited (SANRAL) was interested in the MATSim capability to model detailed diversion patterns given different road pricing strategies. The video shown starts with the GFIP network shaded as gray.

<iframe allowfullscreen="" frameborder="0" height="468" mozallowfullscreen="" src="https://player.vimeo.com/video/138598870" webkitallowfullscreen="" width="100%"></iframe>

The road pricing scheme modelled here includes various discount structures, for example time-of-day, whether the vehicle is equipped with an eTag, public transport vehicles, and the vehicle class. The population for the toll diversion study included private cars (only home-work-home trips); commercial vehicles (complete activity chains as in [Joubert et al., 2010](http://dx.doi.org/10.3141/2168-04) ); public transport vehicles and external traffic from the original Saturn model used by SANRAL.

From the video one can see the peak spreading as a result of the toll. Specifically, there is an increase in the overall traffic across the province between 05:15 and 06:00 when the pre-peak discount for all vehicle classes ends. The major diversion from the GFIP network is expected from commercial vehicles, and specifically during off-peak periods (see 09:00 - 15:00). One of the reasons is that the secondary road network is less congested during the off-peak period, and is hence available to commercial vehicles as an alternative.

**Files**

- [Poster presented at Winter Simulation Conference (WSC) 2008](http://matsim.org/sites/default/files/scenarios/poster_presented_at_winter_simulation_conference_wsc_2008.pdf) (PDF)
- [Paper presented at Southern African Transport Conference 2010](http://matsim.org/sites/default/files/scenarios/paper_presented_at_southern_african_transport_conference_2010.pdf) (PDF)



