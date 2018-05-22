---
layout: default
title: MATSim Extensions
---

## MATSim Extensions

### Introduction

The default MATSim releases contain all the functionality typically used to model agent behavior and simulate traffic. But sometimes, this just is not enough. The MATSim Extensions provide additional functionality for specific tasks, and can be used along MATSim.  [MATSim Extensions](/extensions) gives an overview of the currently available extensions. Please note that these extensions are usually provided and maintained by single persons from the community, and thus long-term support may vary from the default MATSim release.

### Using Extensions via Maven

*This is the recommended way for using extensions.*

See [here](/downloads) under "Maven" about how to use MATSim via Maven.  Note, in particular, the "MATSim example project".  MATSim contribs (those extensions that are part of the contrib directory) can then just be used by adding them as additional dependencies in the pom.xml.


### Using Extensions "manually"

This is *not* the recommended way for using extensions (see "Using Extensions via Maven" above).

#### Downloading Extensions

All extensions come as a compressed zip-file. You can either download the last stable release of an extension to be used together with the stable release of MATSim, or you can download a so-called "nightly build"—an automatically created, but untested and probably unstable version of the extension.

You can download the stable releases of extensions from the [MATSim download page](/downloads).
Likely unstable nightly builds can be found from the same page.
Make sure to also download MATSim itself. The extensions cannot be used without MATSim.

#### Using Extensions on the Command Line

Once you've downloaded an extension and MATSim, unzip the extension and place the extension's directory inside the MATSim directory, next to the libs directory. The file/directory structure should look similar to the following example:

```
matsim/
+ MATSim.jar
+ libs/
| + <lots of .jar files>
+ extension1/
| + extension1.jar
+extension2/
| + extension2.jar
| + libs/       <-- not all extensions contain additional libs
| | + <one or more .jar files>
```

Then, start your simulation with the extension.jar-file on the classpath along the MATSim jar-file, e.g:

```
java -Xmx2000m -cp MATSim.jar:extension1/extension1.jar:extension2/extension2.jar org.matsim.contrib.RunXxxExample myConfig.xml
```

On Windows, use `;` instead of `:` to separate the different jar-files.

<!-- ### Using Manually Downloaded Extensions in Eclipse -->

<!-- Unzip the downloaded extension and place the extension's directory in your eclipse project. Then, add the extension's jar-file to the Java Build Path in Eclipse's Project Settings. -->

<!-- not recommending this any more; IDE users really should use maven.  kai, may'18 -->

<!-- ## Documentation about Specific Extensions -->

<!-- Extensions are developed and documented by their maintainers.  Not all extensions are listed below; see the list of available extensions for their description and documentation. -->

### Contributing Extensions

See [here](/docs/contributing/extensions) for instructions.
