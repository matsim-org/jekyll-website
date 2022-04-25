---
layout: default
title: Conferences and Meetings
---

# <i class="fa fa-calendar">&nbsp;</i>MATSim Conferences and Meetings

Here you will find links to upcoming and past conferences and meetings related to MATSim research and application.

{% comment %} with some liquid wizardry, one can probably detect those posts that are older than the current date and move them to "past events" automatically {% endcomment %}

<div class="col-md-12 posts">

    <!-- The news items in _data/news.yml are auto-generated from the CI build script once an hour. -->

    {% for post in site.conferences reversed %}
    <article class="post">

      <div class="entry">
        <h4>
          <a class="news-headline" href="{{ post.url }}">{{ post.title }}</a>
        </h4>
        <p class="blog-byline">
            {% if post.event_date.start %}
                {% if post.event_date.end %}
                    {{ post.event_date.start | date: "%e %B, %Y" }}
                    to
                    {{ post.event_date.end | date: "%e %B, %Y" }}
                {% else %}
                    on {{ post.event_date.start | date: "%e %B, %Y" }}
                {% endif %}
            {% endif %}

            {% if post.location.name %}
                in
                {% if post.location.url %}
                    <a href="{{post.location.url}}">
                {% endif %}
                    {{post.location.name}}
                {% if post.location.url %}
                        </a>
                {% endif %}
            {% endif %}


            {% assign contact_name=post.contact.name | default: post.contact.email %}
            {% if contact_name %}
                <br>Contact:
                {% if post.contact.email %}
                    <a href="mailto:{{ post.contact.email }}">{{contact_name}}</a>
                {% else %}
                    {{contact_name}}
                {% endif %}
            {% endif %}
        </p>

        {{ post.summary }}
        <br/>
        <br/>

        <a href="{{ post.url }}" class="read-more">&raquo;&nbsp;Read&nbsp;More&hellip;</a>
      </div>

      <div class="faint_border"></div>

    </article>
    {% endfor %}

</div>

<br/>

### Past Conferences

Here you can find information and documentation from the annual MATSim user meeting and MATSim tutorials. The user meeting and a preceding overview tutorial take place annually, often alternating between Zurich and Berlin. Special tutorials are held upon request.

- [2021 User Meeting - Virtual](/conferences/user_meeting_2021)
- [2020 User Meeting - Warsaw, Poland \| Cancelled](/conferences/user_meeting_2020)
- [2019 User Meeting - Leuven, Belgium](https://matsim.atlassian.net/wiki/spaces/MATPUB/pages/365133825/MATSim+User+Meeting+2019)
- [2018 User Meeting - Atlanta, USA](https://matsim.atlassian.net/wiki/spaces/MATPUB/pages/116916260/MATSim+User+Meeting+2018+ITM+Atlanta+June+23) - [(Slides available)](https://matsim.atlassian.net/wiki/spaces/MATPUB/pages/299335682/Presentations+from+MATSim+User+meeting+2018)
- [2017 User Meeting - Haifa, Israel](https://matsim.atlassian.net/wiki/spaces/MATPUB/pages/117899265/MATSim+User+Meeting+special+session+hEART+2017) (some [presentation slides](https://matsim.atlassian.net/wiki/spaces/MATPUB/pages/112202007/Presentations+at+the+MATSim+User+Meeting+2017) also available)
- [2015 User Meeting - Singapore](http://archive.matsim.org/singapore2015)
- [2015 Tutorial - Singapore](http://archive.matsim.org/tutorial/singapore2015)
- [2014 Tutorial - Berlin](http://archive.matsim.org/tutorial/berlin2014)
- [2013 User Meeting - Zurich](http://archive.matsim.org/zurich2013)
- [2013 Tutorial - Berlin](http://archive.matsim.org/tutorial/berlin2013)
- [2012 User Meeting and Tutorial - Berlin](http://archive.matsim.org/usermeeting12)
- [2012 MATSim Tutorial in July 2012 - Madison, WI](http://archive.matsim.org/tutorial/madison2012)
- [2011 Special Tutorial - Shanghai](http://archive.matsim.org/node/636)
- [2011 Special Tutorial - Seoul](http://archive.matsim.org/node/625)
- [2011 Special Tutorial - Singapore](http://archive.matsim.org/node/646)
- [2011 Annual User Meeting and Tutorial - Berlin](http://archive.matsim.org/usermeeting11)
- [2010 Annual User Meeting and Tutorial - Zurich](http://archive.matsim.org/usermeeting10)
- [2010 Tutorial and User Meeting Announcement](http://archive.matsim.org/usermeeting10/announcement)
- [2009 Annual User Meeting and Tutorial - Berlin](http://archive.matsim.org/usermeeting09)
- [2009 User Meeting Announcement](http://archive.matsim.org/usermeeting09/announcement)

---

### Old Website

Some links on third-party sites may refer to content that no longer exists on this website. You might have a look at the [archived, old website](http://archive.matsim.org/) and see if the content is still available there.

- Look here for the [archived conference page](http://archive.matsim.org/usermeetings).
