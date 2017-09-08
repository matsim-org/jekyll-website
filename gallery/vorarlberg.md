---
title: "Vorarlberg, Austria"
thumbnail: /gallery/vorarlberg_thumb.png
layout: scenario
  
---

The Austrian Institute of Technology's (AIT) business unit [Dynamic Transportation Systems (Mobility Department)](http://dts.ait.ac.at/) has developed a new MATSim model for Vorarlberg, the westernmost state of Austria with a size of 2,600 km² and about 380,000 inhabitants in 2015. The model area covers the whole state of Vorarlberg and takes into account the trips of all inhabitants. Freight transport and holiday traffic are excluded in the current model. The work has been developed within the project [SmartCityRheintal](http://www.smartcityrheintal.at/), a research project funded by the [Climate and Energy Fund Austria](http://www.smartcities.at/stadt-projekte/smart-cities/smartcityrheintal/).

The network graph has been derived from OpenStreetMap and enhanced using specialized methods to (1) make it routable and (2) provide each link with its specific parameters like capacity and free-flow speed. The population was generated based on the traffic survey “Mobilität in Vorarlberg 2013”, the land use plan, and the places of interest ("POI") database of Vorarlberg, as well as sociodemographic data. To supply the agents’ plans with a transport mode, an external mode choice model using a maximum likelihood approach was developed.

The MATSim simulation of the existing situation was run twice, first with 10% and finally with 100% of the population. Based on this model, three scenarios were simulated with a 10% sample: (1) improvements in the public transport schedule, (2) traffic impacts of urban development projects, and (3) location and distribution of charging stations for e-mobility.

<iframe allowfullscreen="" frameborder="0" height="468" mozallowfullscreen="" src="https://player.vimeo.com/video/166501600" webkitallowfullscreen="" width="100%"></iframe>

The simulation video above includes 100% of the population of Vorarlberg and shows the motorized individual traffic of the basic model - without holiday traffic and commuters travelling to Vorarlberg from other regions. Each colored dot represents a single, simulated vehicle where the color green represents high velocity / free speed and red represents low velocity.

_Scenario description and video provided by Gernot Lenz, AIT, Mobility DTS_

**Files**

- [SmartCityRheintal Endbericht Verkehrsmodell (german only)](http://matsim.org/sites/default/files/scenarios/SmartCityRheintal_Endbericht_Verkehrsmodell.pdf)