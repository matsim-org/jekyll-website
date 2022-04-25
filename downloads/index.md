---
layout: default
title: Download/Install
---

# Contents

[Use MATSim as a programmer out of an IDE](#programmers)

[Use the MATSim GUI](#gui)

[Use MATSim as a maven plugin](#maven)

[Visualization](#visualization)

[About releases](#releases)

[Benchmark](#benchmark)

# &nbsp; {#programmers}

<!-- (stupid fix so anchor is not underneath page header. :-(  kai) -->

# Use MATSim as a programmer out of an IDE

<!-- ### Quickstart -->

This approach targets programmers who are comfortable with Java and an IDE (e.g. Eclipse or IntelliJ). This will automatically download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots.

Install:

1. (optional but recommended) Fork [matsim-example-project](https://github.com/matsim-org/matsim-example-project).
1. Clone matsim-example-project into local directory.
1. Import as maven project into IDE. Maven will sort out the dependencies. <mark>No need to download the MATSim main repository.</mark> Sources are available.
   1. IntelliJ: Import project --> browse to dir --> maven --> Next, Next, Next
   1. Eclipse: Import ... --> ... as maven project --> browse to dir --> accept, accept, accept
1. Run `MATSimGUI` from the IDE.
   1. An example config file is in `scenarios/equil`.
   1. Press `Run` to run MATSim.
1. (optional but recommended) Run `RunMATSim` from the IDE.
1. (optional but recommended) Set up, for your forked repo, a continuous integration (CI) workflow. On the github website of your repo: `Actions` --> `New Workflow` --> `More continuous integration workflows...` --> `Java with Maven` --> `Set up this workflow` --> `Start commit` --> `...`. This will result in a file `.github/workflows/maven.yml` which triggers the automatic build after each commit. Detailed configuration of the workflow via this file is possible at a later point in time.
   <!-- 1. (optional but recommended) Connect your forked repo to [travis](https://travis-ci.org). -->
   <!-- 1. Consult [matsim-code-examples](https://github.com/matsim-org/matsim-code-examples). -->

Notes:

- Code examples are in [matsim-code-examples](https://github.com/matsim-org/matsim-code-examples) on github. Also see there for examples of how to use extensions (package `extensions`).
- If you want/need to write your own extensions:

1. Again, look at [matsim-code-examples](https://github.com/matsim-org/matsim-code-examples) for examples.
1. Look at `ControlerDefaultsModule` (in your IDE, source is retrieved by maven) to see how MATSim is plugged together.

- You will not be able to modify the existing MATSim source code. This is an advantage, since it improves scientific reproducibility. If you feel the need to modify the existing MATSim source code, please use [https://matsim.org/faq](https://matsim.org/faq) and we will try to help or implement missing extension points.
- You can generate a "clickable jar file" of your own code with `mvn package`. This could, for example, be passed on to students or clients for specific studies.

<!-- ### MATSim-example-project on GitHub -->

<!-- The recommended approach to getting started with MATSim is to clone the example project on GitHub. This approach targets programmers who are comfortable with Java and an IDE (e.g. Eclipse or IntelliJ). This will automatically download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots. -->

<!-- You will _not_ be able to modify the existing MATSim source code -- which, in most cases, should not be necessary. It is preferred that you contact the developers in such situations and we will try to help or implement missing extension points. -->

<!-- - [<i class="fa fa-github"></i> Clone the example project on GitHub](https://github.com/matsim-org/matsim-example-project) -->

<!-- ### MATSim-code-examples on GitHub -->

<!-- There is also a MATSim code examples project, which contains code examples of how to work with MATSim.  You can clone this project to have it locally on your computer, or browse the code in github directly.  This project is meant to be used in parallel with (1). -->

<!-- - [<i class="fa fa-github"></i> See the code examples on GitHub](https://github.com/matsim-org/matsim-code-examples) -->

# &nbsp; {#gui}

# Use the MATSim GUI

This "standalone" version is targeted to users who want to use MATSim by editing the input files, including config.xml directly. A basic GUI is provided.

1. Download [matsim-example-project](https://github.com/matsim-org/matsim-example-project) and unzip it. There is an option ``download zipfile''; no need to use git.
1. A clickable jar file is no longer provided, since they make the git repo too large. Instead, follow the instructions under ``Building and Running it locally'' at [matsim-example-project](https://github.com/matsim-org/matsim-example-project).
1. As stated there, you will be able to double click on the generated MATSim jar file. What opens is what we call the MATSim GUI.
   1. An example config file is in `scenarios/equil`.
   1. Pres `Run` to run MATSim.

The logfile contains, between a lot of other information, also a dump of a the full
matsim configuration. If there are interesting parameters, you could try
to copy then into your own config file, modify them, and re-run.

In my (kn's) view, one can actually get quite far in this way, i.e. by just editing the config file. The main problem is how to obtain the network and in particular the so-called initial demand for your own scenario. If you can't get that from somewhere else, it is probably better to go through the tutorial.

<!-- ~~Then type (if you opened the directory on explorer you need to open the command line and type the following command in there)~~ -->

<!-- ~~java -Xmx2000m -cp matsim-0.7.0.jar org.matsim.run.Controler examples/tutorial/config/example5-config.xml~~ -->
<!-- ~~This should produce a new output directory.  Meaning of the parameters:~~ -->

<!-- ~~-Xmx2000m : Increases the Java heap space to 2000MB of memory. If you have less memory, try smaller values, but the Java default is too small.~~ -->
<!-- ~~-cp matsim-0.7.0.jar : The jar file (Java library) which contains MATSim. The release number of the jar file you downloaded might be different from the one in this example (0.7.0), so make sure you type in a release number that corresponds to the version you downloaded.~~ -->
<!-- ~~org.matsim.run.Controler : The class where the main method for running "iterations" resides. ~~ -->
<!-- ~~examples/tutorial/config/example5-config.xml : The xml file that contains all of the configuration of the run.  The file can be edited.~~ -->
<!-- ~~Note: if you run the above "org.matsim.run.Controler" line again, you first need to erase the contents of the output directory.~~ -->

<div class="row">
<div class="col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> Latest Stable Release

Version 14.0 "Spring 2022", released April 2022

- [<i class="fa fa-download"></i> Download ZIP](https://github.com/matsim-org/matsim-libs/releases/download/14.0/matsim-14.0-release.zip) ca. 60 MB
- [Older versions](https://github.com/matsim-org/matsim-libs/releases)
- [Even older versions (on sourceforge)](https://sourceforge.net/projects/matsim/files/MATSim/)

</div>
<div class="col-md-6" markdown="1">

#### <i class="fa fa-bug"></i> Development Version

This (= using a development version of MATSim via the GUI) is not recommended any longer. If you cannot work with a release, you should use the IDE and maven.

</div>
</div>

# &nbsp; {#maven}

# Use MATSim as a maven plugin

The "Maven" version is targeted to programmers who know about Maven, and want to include MATSim into an already existing Maven project. Similar to the "MATSim example project" above, the Maven approach will maven-download MATSim, allow you to browse the source code, and keep you up-to-date with releases or snapshots (depending on your pom.xml).

It will _not_ allow you to modify the existing MATSim code -- which, in most cases, also should not be necessary: it is preferred that you contact the developers in such situations and we will try to help or implement missing extension points.

<div class="row">
<div class="col-md-6" markdown="1">

#### <i class="fa fa-cube"></i> (Pre-)Release

    <repositories>
      <repository>
        <id>matsim</id>
        <name>MATSim Maven repository</name>
        <url>https://repo.matsim.org/repository/matsim/</url>
      </repository>
    </repositories>
    <dependencies>
      <dependency>
        <groupId>org.matsim</groupId>
        <artifactId>matsim</artifactId>
        <version>14.0</version>
      </dependency>
    </dependencies>

The [example project on GitHub](https://github.com/matsim-org/matsim-example-project) contains a valid `pom.xml`.

[Extensions](/extensions) can be added in the same way; see the `pom.xml` in the [code examples on GitHub](https://github.com/matsim-org/matsim-code-examples)

</div>
<div class="col-md-6" markdown="1">

#### <i class="fa fa-bug"></i> Automatic snapshot of development version

    <repositories>
      <repository>
        <id>matsim</id>
        <name>MATSim Maven repository</name>
        <url>https://repo.matsim.org/repository/matsim/</url>
      </repository>
    </repositories>
    <dependencies>
      <dependency>
        <groupId>org.matsim</groupId>
        <artifactId>matsim</artifactId>
        <version>15.0-SNAPSHOT</version>
      </dependency>
    </dependencies>

These versions are typically less stable and don't come with up-to-date documenation, but may contain new features.

</div>
</div>

# &nbsp; {#visualization}

# Visualization

When the simulation ran, many files were created in its output
directory. Note that the GUI has a button to reach the output
directory. One of the files is a so-called events file, typically
generated for every 10th iteration. The events file for the zeroth
iteration is located in `.../ITERS/it.0/...0.events.xml.gz`. This
contains a lot of information that can be visualized.

The easiest way to visualize MATSim output is to use VIA. A free
version, with a limit on the number of agents, is [available for
download](http://via.simunto.com). If you start VIA, you should see a
large, black area. This is where the traffic will be visualized. On
the left side of this area, you see a smaller area with 4 icons on the
top ("Controls"). Click the first icon (Data Sources). Now you can
either drag and drop files into this section (e.g. a `network.xml`, or
`events.xml.gz`), or click the "+" at the bottom to select a file to
be added. Use either option to add first `network.xml` to the list of
available data and then `events.xml.gz`. Now the visualizer knows
about our data, and we can tell it how to visualize it.

Next, click on the second icon ("Layers") in the Controls section.
Initially, you will see only the background layer listed. Click on
the '+' to select the data you want to have displayed. It should already
suggest to visualize the network with the loaded `network.xml`, so just
click `Add`. After a short moment, the network should be shown in the
visualization area. Click the '+' again, but this time choose Vehicles as
layer type. The `events.xml.gz` file will be already pre-selected.
Click on `Add`. As any layer depending on the events, a
`Load Data` button will appear at the bottom of the layer tag.
Click it to extract the vehicles' positions from the events.

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
