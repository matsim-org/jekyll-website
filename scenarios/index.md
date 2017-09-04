---
layout: default
title: Scenarios
---

<h4>Scenarios</h4>

<div>

<div class="col-md-12">

<div class="col-md-5">

  MATSim is used all over the world! Have a look how others use MATSim and in what regions they apply it. Learn what data they used and how they prepared their data and processed the output.

  <div class="infobox">
  Some scenario data is freely available. <a href="http://matsim.org/open-scenario-data">Have a look!</a>
  </div>
</div>

<div class="col-md-5">
  <img width="100%" src="/images/matsim-locations.png" />
</div>

</div>

</div>

{% assign years = "2022|2021|2020|2019|2018|2017|2016|2015|2014|2013|2012" | split: "|" %}
{% capture strnowyear %}{{'now' | date: '%Y'}}{% endcapture %}
{% assign nowyear = strnowyear | plus: 0 %}

{% for stryear in years %}
   {% assign year = stryear | plus: 0 %}
   {% if year <= nowyear %}
<br/>

<p class="sidebar_title"> {{year}}</p>

{% for post in site.posts %}
{% capture postyear %} {{post.date | date: '%Y'}}{% endcapture %}
{% if postyear contains stryear %}
**[ {{ post.title }} ]({{ post.url }})**
<br/>
_&nbsp;&nbsp;&nbsp;&raquo; by {{ post.author }} on {{ post.date | date_to_string }}_

{% endif %}
{% endfor %}

{% endif %}
{% endfor %}

<br/><br/>
Do you have a scenario and want to present it here as well? Feel free to [contact us](mailto:info@matsim.org) so we can add it as well!
