---
layout: default
title: Build a custom GUI runner
---

# Build a custom GUI runner

Since version 0.8.0, MATSim comes with a simple GUI that starts upon double-clicking 
the matsim.jar file. The GUI requests a config file, and then lets users run a 
simulation by starting `org.matsim.run.Controler` with the specified config file 
as argument. Contribs are able to re-use the GUI infrastructure to provide a 
version of the GUI that starts their own, specialized Controler.

## How to create a GUI that runs a special class

Prepare your main class that should be started to run your simulation:

    public class MySuperSimulation {
      public static void main(String[] args) {
        String configFilename = args[0];
        Controler controler = new Controler();
        // setup controler or do other custom stuff
        controler.run(configFilename);
      }
    }


Create a new class, acting as the main class when double-clicking the jar-file. This class essentially only runs one command to start the GUI and specifies which main class should be started by the GUI:

    import org.matsim.run.gui.Gui;
    public class MySuperSimulationGUI {
      public static void main(String[] args) {
        Gui.show("MATSim: My Super Simulation", MySuperSimulation.class);
      }
    }
 

Modify the `pom.xml` in your contrib to include the following settings. Make sure to specify the correct class name for your GUI class.

    <build>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-jar-plugin</artifactId>
          <configuration>
            <archive>
              <manifest>
                <mainClass>org.matsim.contribs.mySuperContrib.MySuperSimulationGUI</mainClass>
              </manifest>
            </archive>
          </configuration>
        </plugin>
      </plugins>
    </build>


And then, build a release. First, make sure that all required dependencies 
(including MATSim-core) are maven-installed, e.g. do `mvn install -DskipTests=true` 
for all required dependencies. Then change to the directory of your 
project, e.g. `cd /path/to/matsim/contribs/mySuperContrib/`. Perform a Maven 
clean (`mvn clean`) first, followed by `mvn -Prelease -DskipTests=true`. 
This will result in a zip file in the target-directory which includes the clickable jar-file.