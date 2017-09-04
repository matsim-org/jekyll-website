---
title: "The quandary of accessibility metrics"
author: Suzanne Childress
image: /images/2015/nasa-chicago.jpg
image-wide:
comments: true
layout: post
tags: [tools]

images:
   image1:
      image: /images/2015/accessibility-base-av-banner.jpg
      caption: "Aggregate Logsums in the PSRC region"
      source: "SoundCast travel demand model, 2010"
   image2:
      image: /images/2015/aggregate-logsums.png
      caption: "Example calculation of an aggregate logsum from a document I wrote"


---


We measure many things when evaluating projects, but one impact we care a lot about is **accessibility** - or the amount of economic, social, or other opportunities available to people through travel. In our [benefit-cost tool](http://www.psrc.org/data/models/benefit-cost-analysis/), we must turn accessibility into a dollar value, but this is a challenge, since accessibility is actually quite hard to quantify in way that is both a) easy-to-understand and b) statistically comprehensive and based on human behavior.

I haven't found a measure yet that is both easy-to-understand and accurate at depicting all the facets of accessibility. In this blog, I'll explain a few metrics that we've used in our work, and their benefits and shortcomings.

### Accessibility Metric 1: number of jobs one can reach within 30 minutes ###
One way to quantify accessibility is to show the number of jobs that can be reached within 30 minutes from a given location, with a specific travel mode. This measure is somewhat intuitive to planners, which makes the metric strong on the understandability level, but I can't think of how to turn the number of jobs available in a certain amount of time by a specific mode into a dollar amount. Can you? Is there an easy way to estimate the economic impact of access to jobs? Urban economic theory generally suggests that people are willing to pay more to live in a city, partially because of the access to opportunities like jobs, but would we ever be able to quantify that research and apply it directly to this metric? This measure also suffers from threshold effects - why thirty minutes? - why not thirty-five or fifteen? Finally, this metric would vary strongly by mode, and it would be difficult to compare across different modes. 

Although accessibility to jobs has issues as a rigorous metric, it sure does make a pretty map. Here is an awesome one that shows the number of jobs available from a given location by walking and transit in Seattle.


<embed width="500" height="500" src="https://a.tiles.mapbox.com/v4/ctswebrequest.jlheialj/page.html?access_token=pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw#11/47.5879/-122.2998" frameborder="0" allowfullscreen />

_(credit: [University of Minnesota Accessibility Observatory])(http://access.umn.edu/research/america/transit/2014/maps/)_

### Accessibility Metric 2: Travel times converted to cost using value of time###
Another way we try to measure accessibility is by measuring **travel times**.  We can use travel model results to sum up the time people spent traveling with and without a project or policy implementation. We then apply [a value of time](https://en.wikipedia.org/wiki/Value_of_time) to convert total time into a dollar amount, which is compared against other costs like collisions and air pollution. 

There are several problems with turning time into cost by multiplying by a value of time and using this as an accessibility measure.  First of all, sometimes people actually enjoy traveling, so it shouldn't necessarily be a cost. [People are actually happiest when they commute by walking](http://www.citylab.com/commute/2014/08/which-mode-of-travel-provides-the-happiest-commute/378673/), even though it is the slowest mode. Also, [the ideal commute time is not zero](http://link.springer.com/article/10.1023/A:1010366321778) ; workers reason that an ideal commute would provide enough time for a mental transition time between home and work. In other words, travel time is not always a dis-benefit, though we often assume it to be out of convenience. Also people's value of time greatly depends on contexts that are hard to model, such as trying to make a doctor's appointment in congested traffic (high value of time) as compared to walking to a park on a pretty street (low value of time).

The discrepancy between people's value of time in different situations has real implications to costs of travel in planning. For example, suppose a new light rail line to Bellevue attracts thousands of new riders. In general, transit travel time is **longer** than driving because it includes extra time like walking to a station and waiting for a vehicle to arrive. If you assumed that people only cared about travel time, and this time could be converted to cost, then you end up with the situation that the total cost of travel would be higher even as thousands of people are using the new light rail system. This doesn't make sense; a new option is provided people, and they choose to take it - this must mean that they **are** getting some benefit from the new option, which isn't represented in the travel time conversion metric. Using this measure, adding a transit line would create a higher travel cost, even though we know that the cost should be lower because people have asserted their valuation of the new mode by choosing it.

### Accessibility metric 3: Aggregate mode-destination logsums ###

A statistically strong measure of accessibility is an [aggregate logsum](http://www.jbowman.net/refereed/2006.Dong_et_al.Moving_to_AB_measures_of_acccessability.pdf), developed by several top travel modeling minds. An aggregate logsum is an accessibility measure that accounts for all places you can go, by all modes. They are estimated from observed behaviors of destination and mode choices and can be easily converted to a monetary scale. Here is what aggregate logsums look like in the Puget Sound region.

{% include image.html image=page.images.image1 %}

The problem with aggregate logsums is that they are hard to explain to the mathematically disinclined. An example equation for a logsum looks like this:

{% include image.html image=page.images.image2 %}

The general public will not abide such sigmas in the wild, and they likely revolt upon encountering a logarithm (even one that's natural). If people can't intutively understand a measure, it probably won't work for decision-making. Comments are very welcome in solving this accessibility measure quandary!





