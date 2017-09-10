---
layout: default
title: Building a (personal / nightly) release
---

# Building a (personal / nightly) release

**Note: We are currently deprecating the concept of playgrounds. If you are a new MATSim user, please use MATSim as a regular Java library, and package your package as you would package any other package.**	


The following information gives instructions how to package a playground with its dependencies, often used to upload it to another machine to execute a compute job. Playgrounds are subfolders in a shared repository, where people host their custom projects.
 
## Creating a release of a playground

Prerequisite: Make sure you have the file `assembly-release.xml` in your playground at `src/main/assembly`. 
If you are missing this file, you can copy it from `playgrounds/_template/src/main/assembly`.

    # install matsim, contribs and playgrounds to local maven repository
    # (from matsim repository root directory)
    mvn clean
    mvn install -DskipTests=true


    # from your playground
    mvn clean
    mvn -Prelease -DskipTests=true

This will create a file `myPlayground-0.x.0-SNAPSHOT-r#####.zip` in your 
contrib's or playground's target directory containing the release. Unzip it to use it.
 

## Verification for Contrib and Playgrounds

calling `java -cp myplayground.jar org.matsim.run.ReleaseInfo` should show some 
useful build information (revision number and timestamp).


## Running your code from the release

If you unzip the created release-zip-file, you'll find a jar-file of your 
contrib/playground, and a "libs" directory. To run your code, simple call
`java -cp myplayground.jar playground.myPlayground.my.MainClass arg1 arg2 arg3`
(naturally, replacing the filename, classname and actual arguments with correct values).
 
## Notes

The Manifest for the release-jars may be special and must be configured in the 
plugin-configuration in the pom, thus the release profile (`-Prelease`) is used 
for the generation of the final zip. This is also the reason why it is important 
to clean before building the release, as Maven might not recompile the jar when 
just the profile changes, leading to missing entries in the Manifest of 
the packaged jar-file.

To see the content of the generated zip file, use the following command to unzip it:

    unzip target/matsim-0.x.0-SNAPSHOT-release.zip -d target/release

Adding revision information and timestamp is possible with the buildnumber-plugin, 
but it needs quite some customization. Using the buildnumber-properties in 
filtered files seems only to work if the buildnumber-plugin is NOT configured 
in a profile, but in the main part of the pom.
