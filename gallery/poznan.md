---
title: "Poznan, Poland"
thumbnail: /gallery/poland_thumb.jpg
layout: scenario

---
Poznan, with its population of over 550,000, is the 5th largest city in Poland. Together with the neighbouring districts, it makes up an agglomeration of nearly 1 million people.

<iframe allowfullscreen="" frameborder="0" height="425" mozallowfullscreen="" src="https://player.vimeo.com/video/54141254?badge=0" webkitallowfullscreen="" width="100%"></iframe>

The development of the MATSim scenario for the Poznan region began in 2012, with the primary goal of creating a 24-hour multi-agent simulation of the city and the surrounding districts. The road network was generated based on OpenStreetMap data and consists of over 13,600 nodes and over 32,000 links. The travel demand was derived from a static (1-hour morning peak) model created in PTV VISUM by the Poznan city planning department. The current version of the simulation covers the whole morning peak, 5 A.M. to 12 Noon.

In parallel with the work on the Poznan model, there is ongoing research on dynamic taxi fleet routing. The process of dispatching taxis is carried out on-line. New requests may be submitted at any time and often no assumptions can be made about future demand. Moreover, since only historic approximations of travel times are known, trips may last longer or shorter than expected due to the day-to-day changes in traffic flow and the limited precision of the estimates themselves.

The optimization algorithm dynamically reacts to changes in the current state concerning both supply and demand. Currently, in the first version of the simulation, there are 1,000 taxis (represented as light red rectangles in the video) moving around and serving 5000 taxi trips. Taxi trips are 2% of all 250,000 PrT trips during the morning peak.
