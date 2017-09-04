---
layout: default
title: Authors of PSRC I/O
---

### _I/O AUTHORS: WHO'S WRITING THIS STUFF?_

This blog is brought to you by the technical writers of the Data Systems and Analysis team at the <a href="http://www.psrc.org">Puget Sound Regional Council</a>. We love talking about data.

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

