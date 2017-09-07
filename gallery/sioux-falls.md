---
title: "Sioux Falls, SD, USA"
thumbnail: /gallery/sioux_falls_thumb.png
layout: scenario

image1:
  image: /gallery/sioux_falls_1.jpg
  caption: "Left: road network, transit lines and stops, and buildings. Right: agents performing different activities shown with different colors."
  
---

{% include image.html image=page.image1 %}

Advances in transport demand modeling require the use of well-known test scenarios --- demand and supply descriptions that allow rapid testing, demonstration and comparison of new algorithms, methods, and policies. A simplified road network based on the city of Sioux Falls, South Dakota, became very popular within the transport research community, as it was readily available.

The conventional Sioux Falls scenario presents static origin-destination matrices, as presented in LeBlanc et al. (1975), and is unsuitable for agent-based simulation. Consequently, [Chakirov and Fourie (2014)](http://www.ivt.ethz.ch/vpl/publications/reports/ab978.pdf) transformed the original scenario into an enriched, agent-based scenario with dynamic demand and an integrated public transport system. The new scenario therefore makes it possible to rapidly test the full feature set of the MATSim framework in an integrated fashion.

The scenario aims to provide a realistic, fully dynamic demand with heterogeneous socio-demographic users and a high degree of spatial resolution. Real world survey and land-use data is used to generate a diverse synthetic population and accurate activity locations. The socio-demographic characteristics include age and sex on individual and income on household levels. Car ownership was assigned using the ordered probit model of [Giuliano and Dargay (2006)](http://dx.doi.org/doi:10.1016/j.tra.2005.03.002). The assignment of home and work locations employs land-use and building information, census data from the City of Sioux Falls, South Dakota as well as commonly used static OD-matrices from [LeBlanc et al. (1975)](http://dx.doi.org/doi:10.1287/trsc.9.3.183).

It is important to note that the scenario does not aim to replicate the real City of Sioux Falls, SD, and remains a fictitious test-case scenario.

The developers  acknowledge the City of Sioux Falls GIS division for kindly proving data on the current land-use and Ihab Kaddoura and Benjamin Kickhoefer from TU Berlin, who provided feedback on potential bugs during the scenario generation and testing process. They also thank Prof. Kay Axhausen and Dr. Alexander Erath (IVT, ETH Zurich) for valuable input to the generation of this scenario.

#### Where to find the scenario data

The scenario data ships in MATSim XML format, ready to use, with every checkout of MATSim. See the [Download section](/downloads) for details. After checking out, check matsim/examples/siouxfalls2014/config.xml to see where all the individual scenario components reside.

The original tables used to generate the MATSim XML demand description,  as well as the MATSim input data and the simulation results analyzed in Chakirov and Fourie (2014), can be found on the [Transportation Test Problems page](http://www.bgu.ac.il/~bargera/tntp/) of the Ben-Gurion University of the Negev, maintained by Hillel Bar-gera.


