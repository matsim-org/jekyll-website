---
layout: default
title: Download/Install
---

# Install MATSim

Some options to get hold of MATSim are described here. These are in the recommended order for most users.
 
## (1) MATSim-example-project on GitHub

The recommended approach to getting started with MATSim is to clone the example project on GitHub. This approach targets programmers who are comfortable with Java and an IDE (e.g. Eclipse or IntelliJ). This will automatically download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots. 

You will _not_ be able to modify the existing MATSim source code -- which, in most cases, should not be necessary. It is preferred that you contact the developers in such situations and we will try to help or implement missing extension points.

- [<i class="fa fa-github"></i> Clone the example project on GitHub](https://github.com/matsim-org/matsim-example-project)
 
## (2) MATSim-code-examples on GitHub

There is also a MATSim code examples project, which contains code examples of how to work with MATSim.  You can clone this project to have it locally on your computer, or browse the code in github directly.  This project is meant to be used in parallel with (1).

- [<i class="fa fa-github"></i> See the code examples on GitHub](https://github.com/matsim-org/matsim-code-examples)
 
## (3) Standalone

The "Standalone" version is targeted to users who want to use MATSim by editing the input files, including config.xml directly. A basic GUI is provided.

<div class="row">
<div class="col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> Latest Stable Release

Version 0.10.1 "Summer 2018", released August 2018

- [<i class="fa fa-download"></i> Download ZIP](https://github.com/matsim-org/matsim/releases/download/matsim-0.10.1/matsim-0.10.1.zip)  ca. 20 MB
- [<i class="fa fa-cubes"></i> Extensions / Contribs](https://github.com/matsim-org/matsim/releases/tag/matsim-0.10.1)
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

## (4) Maven

The "Maven" version is targeted to programmers who know about Maven, and want to include MATSim into an already existing Maven project.  Similar to the "MATSim example project" above, the Maven approach will maven-download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots (depending on your pom.xml). 

It will _not_ allow you to modify the existing MATSim code -- which, in most cases, also should not be necessary: it is preferred that you contact the developers in such situations and we will try to help or implement missing extension points.

<div class="row">
<div class="col-xs-12 col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> Latest (Pre-)Release


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
        <version>0.10.1</version>
      </dependency>
    </dependencies>

The [example project on GitHub](https://github.com/matsim-org/matsim-example-project) contains a valid `pom.xml`.

[Extensions](/extensions) can be added in the same way; see the `pom.xml` in the [code examples on GitHub](https://github.com/matsim-org/matsim-code-examples)

</div>
<div class="col-xs-12 col-md-6" markdown="1">

#### <i class="fa fa-bug"></i> Development Version


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
        <version>0.11.0-SNAPSHOT</version>
      </dependency>
    </dependencies>

These versions are typically less stable and don't come with up-to-date documenation, but may contain new features.

</div>
</div>


## About releases

We normally release together with our summer term class taught at TU Berlin:
1. A pre-release in march/april.
1. Possible bugfix versions while the class is running.
1. In june/july, the last bugfix version becomes the stable release.

In consequence, the "latest (pre-)release" may be more modern than the "latest stable release".





## <i class="fa fa-tachometer"></i> &nbsp; Benchmark

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

