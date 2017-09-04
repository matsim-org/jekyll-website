---
title: How to mine publicly available, crowd-sourced transportation data sources
author: Suzanne Childress
image: /images/2014/seattle_square_map.png
comments: yes
layout: post
tags: [tools]
---

Many commercial transportation data sources share information via "application programming interfaces", known as APIs. These APIs allow  access to the data using simple snippets of code. As planners, this gives us access to modern, timely data sources for a low (or sometimes zero) cost. Here are some APIs we are currently exploring at PSRC:


|service|description|
|---|---|
|[OneBusAway](http://developer.onebusaway.org/modules/onebusaway-application-modules/current/api/where/index.html)| Transit arrival, departure times, trip data|
|[Google Directions](https://developers.google.com/maps/documentation/directions/)|Origin-Destination directions|
|[Google Distance Matrix](https://developers.google.com/maps/documentation/distancematrix/)|Origin-Destination Distance and Travel Time|
|[Google Elevation](https://developers.google.com/maps/documentation/elevation/)|Elevation at X-Y coordinates |
|[Uber ride-sharing](https://developer.uber.com/)| Origin-Destination pair cost, service, time estimate|
|[Car2Go car-sharing](https://code.google.com/p/car2go/wiki/vehicles_v2_1)|locations of ready-for-use car to go vehicles|


Many of these data sources have open-source code available to help you access the information programmatically: check out the list at the [Open Source Planning](https://github.com/osPlanning/) site on GitHub if you want to dive in.

##### What can you do with the data?

We're already using this data at PSRC for travel model validation.  Travel models rely on matrices of zone-to-zone travel time, cost, and distance. Validation can be challenging since observed data like travel time and traffic flow are sparsely collected. We often rely on small samples of sometimes outdated data to make sure our models' baselines accurately reflect reality. Being able to reflect current conditions is critical, because a wrongly calibrated model for today's setting will almost certainly produce inaccurate future analyses.

We use the Google APIs to help validate our model's travel time and cost estimates. An example result from a Google API call would provide data as follows:

|Origin Zone|Destination Zone|Distance (miles)| Auto Travel Time (minutes)|
|---|---|---|---|
|2216|3566|104.3|118|
|2246|789|40.9|50.6|
|23|1804|6.6|14.8|
|2836|997|28.1|36.0|

We can compare these values against model results for validation. Other uses could include the creation of visualizations and animations.  The animation below shows car2go use in Seattle over a few days in April.

**car2go Vehicle Availability in Seattle Time-Lapse**

Another example is below. The animation was created using a query of car2go ready-to-use vehicles:

<embed width="560" height="315" src="//www.youtube.com/embed/Y_P47n0NOWE" frameborder="0" allowfullscreen />

_(credit: Jarek Piorkowski on YouTube)_

From the Uber and car2go data, you could create trip tables for these modes.  These trip tables could be grown over time, or factored up based on an assumption of increased use.

You can even build a simple mode choice model that includes Uber and car2go.  That is, if you had enough car2go or Uber data from your household survey.

##### What are the concerns with using this data?

The relationship between planning agencies and technology groups providing this data is relatively new, and hopefully evolving, so we want to remain good neighbors.

Most of these sources limit the number of calls to the API so you cannot continuously download data or get data for every origin-destination pair. Also, any time "big data" is being used, privacy concerns are involved. Most API data is intentionally secure and void of user-info, but even anonymized GPS traces hold potential of revealing personal behaviors. In the often grey world large-scale data collection, we encourage planners and programmers to take all possible steps to consider privacy in their collection methods and analyses.

Since APIs are not necessarily designed with data-collection (esp. by planners) in mind, we should remain vigilant that we are not breaking terms of use.  Most of the terms of use are geared towards commercial software developers, as opposed to non-profit or government planners.  This can make them somewhat hard to understand as planners.  We would like to use the data to validate models and help decision-makers understand travel patterns, instead of using the data to build an app to sell. Our purpose doesn't lie in periodic API calls for clients, but we're interested in large-scale harvesting of user data, to build aggregate knowledge on how cities and regions are traveling.

Let us know if you've found other big data sources on the web that have proven useful!