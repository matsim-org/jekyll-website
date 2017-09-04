---
title: "Playground test failures"
author: Kai Nagel
image-wide: /images/matsim-logo.png
image: /images/matsim-logo.png
layout: post
tags: [tools]

images:
   image1:
      image: /images/2016/licenses-by-age.png
      caption: "Percent of People With Driver's Licenses by Age Group"
      source: "PSRC Household Travel Surveys 2006 and 2014"
---

Dear MATSim community,

You have probably noticed that we have recently separated "matsim"+"contribs" on the one hand from "playgrounds" on the other hand.
This also means that the playgrounds are now tested separately both on travis and on jenkins.
Several people have, in the past, nudged people to repair playground test failures.  

I now want to announce that I essentially will no longer be one of these people.  I have just switched off my monitoring apps for these tests.  This means that if the system notifies me of a failure which I may have caused, I will still look at it, but if other people make the playgrounds fail, I will not act any more.

Maybe some other group in the community wants to self-organize to take this on.  An alternative, clearly, is that people who mostly want to monitor their own code, could pull out into a separate repository.  The matsim-example-project points the way for this.  The arguments in both directions in my view are:

- Playgrounds are a service from us to the community: they are included in refactorings.  Separate, individual repositories are in general not.
- A downside of the playgrounds, however, is that if one of the playgrounds has a compile error, none of the playgrounds is tested.

In the longer run, our goal would be to get rid of playgrounds completely.  However, we are still refactoring our API, and as long as we are still doing this, we will keep them.

So maybe a group of people who want to keep their playgrounds functional wants to form and jointly make sure that the playground tests do not fail.  You could, for example, start self-organizing via "comment" posts under this blog entry.

Best wishes

Kai
