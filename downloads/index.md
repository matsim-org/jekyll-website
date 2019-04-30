---
layout: default
title: Download/Install
---

# Contents

[Use MATSim as a programmer out of an IDE.](#programmers)

[Use the MATSim GUI.](#gui)

[Use MATSim as a maven plugin.](#maven)

[About releases.](#releases)

[Benchmark.](#benchmark)

# &nbsp; {#programmers}
<!-- (stupid fix so anchor is not underneath page header. :-(  kai) -->
# Use MATSim as a programmer out of an IDE

<!-- ### Quickstart -->

This approach targets programmers who are comfortable with Java and an IDE (e.g. Eclipse or IntelliJ). This will automatically download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots.

You will _not_ be able to modify the existing MATSim source code -- which, in most cases, should not be necessary. It is preferred that you contact the developers in such situations and we will try to help or implement missing extension points.

1. (optional but recommended) Fork [matsim-example-project](https://github.com/matsim-org/matsim-example-project).
1. Clone matsim-example-project into local directory.
1. Import as maven project into IDE.
   1. IntelliJ: Import project --> browse to dir --> maven --> Next, Next, Next
   1. Eclipse: Import ... --> ... as maven project --> browse to dir --> accept, accept, accept

   Maven will sort out the dependencies.  No need to download the MATSim main repository.  Sources are available.
1. Run `MATSimGUI` .  
   1. An example config file is in `scenarios/equil`.
   1. Press `Run` to run MATSim.
1. Run `RunMATSim` directly from the IDE.
1. (optional but recommended) Connect your forked repo to [travis](https://travis-ci.org).
<!-- 1. Consult [matsim-code-examples](https://github.com/matsim-org/matsim-code-examples). -->

Code examples are in  [matsim-code-examples](https://github.com/matsim-org/matsim-code-examples) on github.

<!-- ### MATSim-example-project on GitHub -->

<!-- The recommended approach to getting started with MATSim is to clone the example project on GitHub. This approach targets programmers who are comfortable with Java and an IDE (e.g. Eclipse or IntelliJ). This will automatically download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots. -->

<!-- You will _not_ be able to modify the existing MATSim source code -- which, in most cases, should not be necessary. It is preferred that you contact the developers in such situations and we will try to help or implement missing extension points. -->

<!-- - [<i class="fa fa-github"></i> Clone the example project on GitHub](https://github.com/matsim-org/matsim-example-project) -->

<!-- ### MATSim-code-examples on GitHub -->

<!-- There is also a MATSim code examples project, which contains code examples of how to work with MATSim.  You can clone this project to have it locally on your computer, or browse the code in github directly.  This project is meant to be used in parallel with (1). -->

<!-- - [<i class="fa fa-github"></i> See the code examples on GitHub](https://github.com/matsim-org/matsim-code-examples) -->

# &nbsp; {#gui}
# Use the MATSim GUI

The "Standalone" version is targeted to users who want to use MATSim by editing the input files, including config.xml directly. A basic GUI is provided.

<div class="row">
<div class="col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> Latest Stable Release

Version 0.10.1 "Summer 2018", released August 2018

- [<i class="fa fa-download"></i> Download ZIP](https://github.com/matsim-org/matsim/releases/download/matsim-0.10.1/matsim-0.10.1.zip	)  ca. 63 MB
<!-- - [<i class="fa fa-cubes"></i> Extensions / Contribs](https://github.com/matsim-org/matsim/releases/tag/matsim-0.10.1) -->
<!-- (we do not support that any longer. marcel/kai/joschka, aug'18) -->
- [Older versions](https://github.com/matsim-org/matsim/tags)
- [Even older versions (on sourceforge)](https://sourceforge.net/projects/matsim/files/MATSim/)

</div>
<div class="col-md-6" markdown="1">

####   <i class="fa fa-bug"></i> Development Version

<!-- Maybe we keep this up and running as long as it works.  But if the build server ever starts failing us on this, I think we should just also remove this section here.  kai, oct'17 -->

These versions are typically less stable and don't come with up-to-date documenation, but may contain new features.

- [<i class="fa fa-download"></i> Download](/files/builds/) a Nightly Build.
- [<i class="fa fa-book"></i> How to use Nightly Builds](/downloads/nightly)

</div>
</div>

# &nbsp; {#maven}
# Use MATSim as a maven plugin

The "Maven" version is targeted to programmers who know about Maven, and want to include MATSim into an already existing Maven project.  Similar to the "MATSim example project" above, the Maven approach will maven-download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots (depending on your pom.xml).

It will _not_ allow you to modify the existing MATSim code -- which, in most cases, also should not be necessary: it is preferred that you contact the developers in such situations and we will try to help or implement missing extension points.

<div class="row">
<div class="col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> (Pre-)Release


    <repositories>
      <repository>
        <id>matsim</id>
        <name>MATSim release repository</name>
        <url>http://dl.bintray.com/matsim/matsim</url>



      </repository>
    </repositories>
    <dependencies>
      <dependency>
        <groupId>org.matsim</groupId>
        <artifactId>matsim</artifactId>
        <version>11.0</version>
      </dependency>
    </dependencies>

The [example project on GitHub](https://github.com/matsim-org/matsim-example-project) contains a valid `pom.xml`.

[Extensions](/extensions) can be added in the same way; see the `pom.xml` in the [code examples on GitHub](https://github.com/matsim-org/matsim-code-examples)

</div>
<div class="col-md-6" markdown="1">

#### <i class="fa fa-bug"></i> Automatic snapshot of development version


    <repositories>
      <repository>
        <id>ojo-snapshots</id>
        <name>MATSim snapshot repository</name>
        <url>http://oss.jfrog.org/libs-snapshot</url>
        <snapshots>
          <enabled>true</enabled>
        </snapshots>
      </repository>
    </repositories>
    <dependencies>
      <dependency>
        <groupId>org.matsim</groupId>
        <artifactId>matsim</artifactId>
        <version>12.0-SNAPSHOT</version>
      </dependency>
    </dependencies>

These versions are typically less stable and don't come with up-to-date documenation, but may contain new features.

</div>
</div>

# &nbsp; {#releases}
# About releases

We normally release together with our summer term class taught at TU Berlin:
1. A pre-release in march/april.
1. Possible bugfix versions while the class is running.
1. In june/july, the last bugfix version becomes the stable release.

In consequence, the "latest (pre-)release" may be more modern than the "latest stable release".



# &nbsp; {#benchmark}
# <i class="fa fa-tachometer"></i> &nbsp; Benchmark

[Download Benchmark](/files/benchmark/benchmark.zip) ZIP, ca. 35MB

More information about the [MATSim Benchmark](/benchmark).


<!-- Not advertising to clone the source code any more.  kai, oct'17 -->

<!-- ### <i class="fa fa-file-code-o"></i> &nbsp; Source Code -->

<!-- The source code to MATSim is [available on <i class="fa fa-github"></i>GitHub](https://github.com/matsim-org/matsim). -->

<!-- This is targeted to developers who change the MATSim core (a relatively small circle of persons), or persons who maintain one or more contribs. &nbsp;For a variety of reasons, we also have "playgrounds" in a second GitHub Repository, although they should be less necessary in the future than they were in the past.</p> -->

<!-- </div> -->



<!-- The example project is mentioned above, no need to repeat.  kai, oct'17 -->

<!-- <div class="col-md-4" markdown="1"> -->
<!-- ### <i class="fa fa-code-fork"></i> &nbsp; Example Code Project -->

<!-- To get you started writing your own code with MATSim, we provide an [example project on GitHub](https://github.com/matsim-org/matsim-example-project) you can fork, which includes a complete pom.xml to use MATSim as a Maven dependency for your own code.</p> -->

<!-- </div> -->
