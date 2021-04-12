---
layout: post
author: Marcel Rieser
title: "MATSim 13.0 released, and new Maven Repository"
summary: "We've released MATSim 13.0 and switched to a new maven repository."
---

## MATSim 13.0

We're happy to announce the release of MATSim 13.0.

Among many small changes and improvements, here are a few highlights of this release:

- SwissRailRaptor is now the default transit router.
  If you have enabled SwissRailRaptor yourself in the code (e.g. with `controler.addOverridingModule(new SwissRailRaptorModule());`), you should
  now remove this line as not to enable it twice.
- There is a new, faster routing algorithm names `SpeedyALT` available for network (e.g. `car`) routing. It can be enabled in the config and used
  in place of `Dijkstra`, `AStarLandmarks` or any of the other existing routing algorithms.
- Adding Hermes, a faster alternative to QSim for some scenarios (Hermes does not support all features that QSim does).
- Vehicles can have attributes.
- Support for cordon toll was removed from road pricing.
  
In addition, several contribs saw major work going on (e.g. the whole MAAS group: DRT, DVRP, ...), so if you are not yet on a recent
weekly snapshot, make sure to upgrade to version 13.0 soon to benefit from all the work.
  
To use the new version from your code as a Maven dependency, please note that you 
need to update the repository, as outlined in the next section.

  
## New Maven Repository

For the last few years, we've hosted our jar-files in a Maven repository hosted by BinTray.
Recently, BinTray announced that it shuts down its service for open source projects.
We have thus migrated our MATSim releases to a new Maven repository.

Please update your `pom.xml` to use the following repository:

```xml
<repository>
    <!-- Repository for MATSim releases and snapshots (MATSim is not on Maven central) -->
    <id>matsim</id>
    <url>https://repo.matsim.org/repository/matsim</url>
</repository>
```

The two old repositories for releases (`dl.bintray.com/matsim/matsim`) and for snapshots
(`https://oss.jfrog.org/libs-snapshot`) can be removed from the pom.


