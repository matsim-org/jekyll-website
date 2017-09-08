---
title: "Quito, Ecuador"
thumbnail: /gallery/quito_thumb.png
layout: scenario

image1:
  image: /gallery/quito_img1.jpg
  caption: "Percent of People With Driver's Licenses by Age Group"
  source: "MATSim.org"

image2:
  image: /gallery/quito_img2.jpg
  caption: "Quito Traffic Density Levels"
  
  
---

The Metropolitan District of Quito (DMQ) is Ecuador's capital where currently more than two million people are living. It has grown quickly in recent years, causing traffic congestion and pollution. Our research integrates evolutionary computation, public and private mobility and emission simulation and data mining tools to gain a better understanding of complex mobility problems in the city.

The geographical area of study is the business district which covers approximately 5×8 km2. A first scenario dealt with the optimization of 70 traffic signals with 20.000 agents moving in two main trips. The plans are designed so that all the agents move first from each home location to different points along the zone. The network comes from OpenStreetMap and includes the primary and secondary pathways, represented in total by 8192 links. The evolutionary algorithm (EA) together with MATSim found the optimal signal setting of the DMQ Scenario, minimizing average travel time. 

We implemented several genetic operators and designed and tested several experiments to find a proper configuration that allows fluid traffic flow through proper coordination between signals. Using data mining techniques, we group the optimal solutions in clusters. Finally, we analyze the effects of traffic signal settings in respect to the environmental impact using the output data from the MATSim emission module.

{% include image.html image=page.image1 %}

A second approach examines traffic density levels in urban transportation. The EA searches the combinations of a number of private/public transport users, capacity and headways of Bus Rapid Transit (BRT) of five main corridors on DMQ Scenario. The traffic density is influenced by the proportions of the population that use public (NPt) and private transportation and implies a bi-level optimization problem. Different proportions and configurations impact the traffic density, travel time and fuel consumption. Those criteria are in conflict with each other; we developed a framework to minimize simultaneously the three objectives, coupling a multi-objective EA with MATSim.

{% include image.html image=page.image2 %}

We acknowledge the support of Shinshu University (Japan) and Senescyt (Ecuador). Thanks to Senozon for the [visualising software](http://via.senozon.com/). 

<iframe allowfullscreen="" frameborder="0" height="607" mozallowfullscreen="" src="https://player.vimeo.com/video/210737965" webkitallowfullscreen="" width="100%"></iframe>

[Quito, Ecuador](https://vimeo.com/210737965) from [MATSim page on Vimeo](https://vimeo.com/matsim).
 
More information about the scenario and the work can be found in the following publications:

- R. Armas, H. Aguirre and K. Tanaka, “Multi-Objective Optimization of Level of Service in Urban Transportation”, _The Genetic and Evolutionary Computation Conference (GECCO)_, Berlin, 2017, to appear.
- R. Armas, H. Aguirre, F. Daolio and K. Tanaka, "An effective EA for short term evolution with small population for traffic signal optimization", _2016 IEEE Symposium Series on Computational Intelligence (SSCI)_, Athens, 2016, pp. 1-8. doi: 10.1109/SSCI.2016.7850099
- R. Armas, H. Aguirre, F. Daolio and K. Tanaka, "Traffic signal optimization and coordination using neighborhood mutation", _2016 IEEE Congress on Evolutionary Computation (CEC)_, Vancouver, BC, 2016, pp. 395-402. doi: 10.1109/CEC.2016.7743821
- R. Armas, and H. Aguirre, 2016. Quito Metropolitan District. In: Horni, A, Nagel, K and Axhausen, K W. (eds.) The Multi-Agent Transport Simulation MATSim, pp. 473-476. London: Ubiquity Press. DOI: http://dx.doi.org/10.5334/baw.80 License: CC-BY 4.0
- R. Armas, H. Aguirre, S. Zapotecas-Martínez and K. Tanaka (2016) Traffic Signal Optimization: Minimizing Travel Time and Fuel Consumption. In: Bonnevay S., Legrand P., Monmarché N., Lutton E., Schoenauer M. (eds) Artificial Evolution. EA 2015. Lecture Notes in Computer Science, vol 9554. Springer, Cham
- R. Armas, H. Aguirre and K. Tanaka (2014) Effects of Mutation and Crossover Operators in the Optimization of Traffic Signal Parameters. In: Dick G. et al. (eds) Simulated Evolution and Learning. SEAL 2014. Lecture Notes in Computer Science, vol 8886. Springer, Cham
