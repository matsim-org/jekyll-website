---
layout: default
title: MATSim Extensions
---

# MATSim Extensions

## _Important Note_

_The following text is no longer up to date and needs to be revised.  We now say that "extensions" is everything that extends MATSim, but there are two categories of extensions:_
* _"contribs", which are inside the MATSim main repository_
* _"other extensions", which are maintained outside the MATSim main repository.  This category again splits into two subcategories_
  * _extensions hosted in the matsim-org repository but not in the MATSim main repository_
  * _other extensions.  VIA is the most prominent example here._

_So please read the following text with care; quite often it says "extension" but means "contrib"._

## Introduction

As a lot of functionality in MATSim is created by PhD students, there is often a 
problem maintaining this functionality after the respective students finished their 
work and leave university.  In order to better communicate which features 
are "standard MATSim" which will (and have to) be maintained by the MATSim 
core developers, and which features are just "single-developer functionality", 
MATSim introduces the concept of "**MATSim core**" and "**MATSim extensions**".

The core will be maintained by the core developers, and should contain central
functionality which is likely to stay in MATSim forever. Extensions can 
provide new, but stable, functionality developed to solve specific problems 
which can be of interest to others in the MATSim community.

Extensions will—as long as they compile and pass all tests—also be packaged 
for releases and be thus optional parts of MATSim releases. This requires that 
extensions follow certain guidelines, also in order to keep code maintenance 
and user support in reasonable bounds.

## Requirements
- You feel responsible for your extension
- Document the functionality of your extension
- Document the usage of your extension. This documentation should cover topics
like (a) How to use it, (b) How to configure it, (c) if it has any special system requirements, (d) optionally have a small tutorial with sample data to demonstrate the functionality.
- If your code offers one or more main classes, make sure to provide useful error message to the user in the case the user submits no or wrong arguments
- If your code offers functionality to other code (e.g. special algorithms and data structures), such classes/interfaces should be well-documented using Javadoc comments.
- You will maintain the code in the case that some updates in MATSim-Core break some functionality in your extension
- You are wiling to assist interested users in the case something is not working as described by your documentation.

## Creating your own extension

- Create the code in your playground or private repository
- Make sure you meet the code requirements outline above
- Talk to a member of the MATSim committee to request a new contrib-project for your code.
- If the committee agrees to your request, they will create a contrib-project for you, where you can move your code to.
- Write documentation about your extension to comply with the above-mentioned documentation requirements.
- Once all the code and documentation requirements are met, your extension will be included in future releases and nightly builds will be created for it.

## Documenting extensions in the contrib section

Extensions in the contrib section are stand-alone documentations.  The entry 
points are under [matsim.org/javadoc](/javadoc). Always please do the following:

- Provide an example "script in java" with a name RunXxx somewhere inside that extension 
package, and add documentation to enable others to use it.
Also see [How to provide coding examples](https://matsim.atlassian.net/wiki/questions/29229089/how-to-provide-coding-examples?src=browse)?

Additional options depend on personal style.  Some options are

- Populate src/main/javadoc/overview.html with html text.  Look at at the minibus 
contrib for an example.  The content will show up at the entry point of the documentation.

- Javadoc can link into the listing by something 
like `<a href="{@docRoot}/src-html/org/matsim/contrib/emissions/example/RunEmissionToolOnlineExample.html">here</a>` 
into the java source listing.
