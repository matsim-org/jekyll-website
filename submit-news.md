---
layout: default
title: Submit MATSim News
---

## Submit MATSim-related news

---

{% capture today %}{{'now' | date: '%Y-%m-%d'}}{% endcapture %}

<div><a target="_blank"
  href="https://github.com/matsim-org/jekyll-website/new/master/?filename=/_posts/{{today}}-news-item.md&value=---%0alayout: post%0aauthor: Your Name%0atitle: %22News Item Title%22%0asummary: %22A sentence or two that will show up on the front page%22%0a---%0a%0aHere is my news item.%0a%0a- Use regular markdown for the full news item content%0a- The header at the top of the file MUST contain your name, item title, and a summary%0a">

<p class="submit-link">CREATE ITEM &raquo;<br/>ON GITHUB &raquo;</p></a></div>

We welcome MATSim-related news items, job postings, and event announcements for our front page. To submit news, create a pull request on Github.com with the content of your news item in Markdown format. Here's how to do that:


#### Instructions for posting news via GitHub

0. You'll need a free account on Github to post items
1. Click the **`Create item on Github`** button above, to draft a new item in the `_posts` directory of our site.
2. Edit the **file name**, **author**, **title**, and **summary** lines. The summary will be shown on the front page as a "teaser" blurb.  
    The file name becomes part of the URL, so please don't call it just "news-item", but give it a specific name.
3. Add your remaining content in [standard Markdown format](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
4. Preview your post using the `Preview` pane, and when done...
5. You're ready to create your pull request!
   - Click **`Propose New File`** button, which will take you to the confirmation page:
   - Click **`Create Pull Request`**
6. You're done!

We'll either add your content or get back to you soon!

---

#### If this is too complicated

If this is just too much, [send us an email](mailto:sekretariat@vsp.tu-berlin.de) and we'll post your item for you.
