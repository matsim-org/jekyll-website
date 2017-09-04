---
layout: default
title: Authors of the MATSim.org blog
---

### _MATSIM.ORG AUTHORS: WHO'S WRITING THIS STUFF?_

This blog is brought to you by the technical writers of the MATSim.org team.

<table class="author_table">
{% for person in site.data.authors %}
	<tr>
                      <td class="author_table">
		<img class="author_table" src="{{person.image}}" alt="{{person.name}}" width="80">
		<strong>{{person.name}}</strong>. {{person.blurb}}
                      </td>
              </tr>
{% endfor %}
</table>

