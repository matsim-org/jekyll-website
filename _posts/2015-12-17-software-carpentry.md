---
title: "Teaching real-world software skills to planners and modelers (or, how to stop using Excel for everything)"
author: Billy Charlton
image: /images/2015/swc-class-small.png
image-wide:
comments: true
layout: post
tags: [tools]

images:
   image1:
      image: /images/2015/swc-class.jpg
      caption: "Learning scripting the easy way: our first hands-on workshop."
   image2:
      image: /images/2015/software-carpentry-large.png
      caption: "Real-world &quot;lab skills&quot; for scientific computing"
      source: "[Software Carpentry](http://software-carpentry.org)"
   image3:
      image: /images/2015/how-learning-works.png
      caption: "How to get learners to actually learn stuff."
      source: "[Amazon](http://www.amazon.com/How-Learning-Works-Research-Based-Principles/dp/0470484101)"



---

By far, the most difficult challenge I face at PSRC is finding the time and resources to sharpen our team's technical skills, especially related to software and programming. Modeling requires more and more software development chops these days, yet few of the staff here have Computer Science degrees.

This disconnect has real consequences: familiar tools like Excel and GIS encourage point-and-click workflows that aren't very reproducible, and results are difficult to review for accuracy. So, how can we catch up and learn more modern approaches to building great software for data analysis?

It turns out we're not the only people thinking about this.

### Software Carpentry

[Software Carpentry](http://software-carpentry.org/) (SWC) is a non-profit volunteer organization whose mission is to teach modern lab skills (i.e., software) to scientific computing researchers. They focus on training university graduate students in the sciences, but their materials and methods are extremely relevant to the technical staff at organizations such as ours.

{% include image-right.html image=page.images.image2 %}

SWC sponsors [workshops](http://software-carpentry.org/workshops/index.html) for learners around the globe and also has a [formal training program](http://software-carpentry.org/pages/join.html) for aspiring instructors like myself. The workshops focus on just a few key skills:

* Learning the [command prompt](http://swcarpentry.github.io/shell-novice/) like a ninja (called the Unix "Bash Shell");
* Using [Git for version control](http://swcarpentry.github.io/git-novice/);
* [Introductory programming](http://swcarpentry.github.io/python-novice-inflammation/) in Python or R, conveniently the two most common languages for data scientists like us;
* Data and database management using [SQL](http://swcarpentry.github.io/sql-novice-survey/);
* Workflow automation using [Make](http://swcarpentry.github.io/make-novice/).

Their approach is proven: students often report being 10%, 20% or [even 10X](http://software-carpentry.org/pages/testimonials.html) more productive after going through the SWC workshops. As a result, the trainings are far more popular than they can possibly handle: I've been on the waiting list for instructor training for well over a year now.

### Going Rogue

This fall, I decided PSRC couldn't wait any longer. Software Carpentry puts all of their workshop materials online in a open format that encourages reuse, remixing, and collaboration. I "went rogue" and tried to learn as much as I could about their approach, in order to roll out a home-spun workshop here at PSRC on my own.

{% include image-right.html image=page.images.image3 %}

* Their workshop materials are based on actual educational theory and research. The book [How Learning Works](http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470484101.html) summarizes that research and I read it cover to cover. (I thought I was just going to skim it, but I couldn't believe how much useful, relevant information was packed in there! A valuable resource for anyone who occasionally teaches but doesn't have educational training.)

* I spent a lot of time in the past month [watching recorded videos](https://www.youtube.com/results?search_query=software+carpentry) of other SWC trainers teaching shell, Git, and Python. Having all that on Youtube is incredibly helpful. Great stuff to watch on the big TV while I'm chopping onions and carrots in the kitchen.

* All of SWC's lessons [are on GitHub](http://software-carpentry.org/lessons.html), as well as some high-level slideshows. Think about that: all these materials are high-quality and available for anyone with an interest. There are even user-contributed lessons on topics like [From a Spreadsheet to a Database](http://swcarpentry.github.io/capstone-novice-spreadsheet-biblio) — particularly relevant to my group of learners.

* Just this fall, the instructor training lesson itself went up on Github. I already had a good idea where things were headed but this lesson emphasized some important teaching guidelines which I think helped ensure a successful workshop.

### Initial Workshop

This all converged for our first scripting class this week. We targeted a very small set of students (just six), so that I could test out the materials (and myself) before exposing a wider audience. Each of the students was already well-versed in at least one of the other topics; the plan is for them to be my co-teachers for Git, Python, and SQL in the coming weeks. I wanted them to sit through a training class first, so they'd get a feel for the SWC way of doing things. I'll give them real "trainer training" after the holidays.

{% include image-right.html image=page.images.image1 %}

Since this was a team of coworkers working from one office downtown, we used "Remote Desktop" in the classroom so that each student would remote control their primary desktop workstation from a loaner laptop. Why? Because this way, everyone could install the required software on their primary desktop ahead of time. They accessed their familiar desktop machine via a laptop during the workshop, and then had all that software waiting for them when they returned to their desks at the end of the day. This only worked because it was an all-staff in-house production; you probably couldn't do this for a general audience, but it was like magic for us here.

The Software Carpentry method is big on feedback: every student puts a green or pink sticky note on the back of their laptop to signify whether they're keeping up, getting behind, or need help. The stickies are used for written good/bad feedback at the end of the session, too. The stickies showed me right away that the chapter on scripting "loops" was confusing, while the lesson on pipes and filters went really well.

Hands-on quiz-like questions at the end of each lesson allowed students to test their new skills. Enthusiasm at the end of the day was really high: one pink ("needs work") note said *"I want to learn more: are there homework or applications for our team specifically or other resources???"* — a pretty good sign. =)

### What's to Come

Given the success of the shell scripting lesson, we've decided to move forward internally with the rest of the Software Carpentry curriculum in early 2016. Everyone on the Data team here at PSRC will go through every class; those of us who already have some of the skills will be "helpers" for those who are at earlier stages of learning. And I'm not teaching all the courses -- there are plenty of people here at PSRC who know these topics well enough that I can sit back and watch them teach each other.

I'm going to wait for feedback from the wider Data Team rollout before committing to further work, but my hope is that things are successful enough that we'll want to advertise some similar workshops for interested staff at our member/peer agencies in the region.

### Thanks where thanks are due

I can't even begin to thank those who had a hand in developing and improving the Software Carpentry approach and materials. The quality and breadth are both really stunning. Even without the formal training, with just a bit of legwork I was able to craft a successful internal workshop.

Let us know if you have questions about any of this! Your feedback is welcome as we consider expanding this to a wider audience in 2016.

### Links and Resources you can use right now

* [Software Carpentry Website](http://software-carpentry.org). Free and open workshop materials, and information on how to attend a workshop or become an instructor.
* [How Learning Works](http://www.amazon.com/How-Learning-Works-Research-Based-Principles/dp/0470484101). The latest educational research on what motivates students to learn and how to get them to actually learn what you're teaching.

