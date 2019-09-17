---
layout: default
title: Quickstart
---


# Quickstart

(0) [Download](/downloads) the release and unzip it.


(1) Go the the directory where you find `matsim-*.jar`.


(2) Double click on the MATSim jar file.  What opens is what we call the MATSim GUI.

~~Then type (if you opened the directory on explorer you need to open the command line and type the following command in there)~~

~~java -Xmx2000m -cp matsim-0.7.0.jar org.matsim.run.Controler examples/tutorial/config/example5-config.xml~~
~~This should produce a new output directory.  Meaning of the parameters:~~

~~-Xmx2000m : Increases the Java heap space to 2000MB of memory. If you have less memory, try smaller values, but the Java default is too small.~~
~~-cp matsim-0.7.0.jar : The jar file (Java library) which contains MATSim. The release number of the jar file you downloaded might be different from the one in this example (0.7.0), so make sure you type in a release number that corresponds to the version you downloaded.~~
~~org.matsim.run.Controler : The class where the main method for running "iterations" resides. ~~
~~examples/tutorial/config/example5-config.xml : The xml file that contains all of the configuration of the run.  The file can be edited.~~
~~Note: if you run the above "org.matsim.run.Controler" line again, you first need to erase the contents of the output directory.~~


(3) Now it is time to have a look at the output. When the simulation ran, 
many files were created in its output directory. Note that the GUI has a 
button to reach the output directory. One of the files is a so-called events file, 
typically generated for every 10th iteration. The events file for the first 
iteration is located in `output/ITERS/it.0/run0.0.events.xml.gz`. This contains
a lot of information that can be visualized. 

Now, when you start the visualizer (called Via, a [free version is 
available for download](http://via.senozon.com), you should see a large, black area. This is 
where the traffic will be visualized. On the left side of this area, you 
see a smaller area with 4 icons on the top ("Controls"). Click the first
icon (Data Sources). Now you can either drag and drop files into 
this section (e.g. a `network.xml`, or `events.xml.gz`), or click the "+" 
at the bottom to select a file to be added. Use either option to add first 
`network.xml` to the list of available data and then `events.xml.gz`. 
Now the visualizer knows about our data, and we can tell it how to visualize it.

Next, click on the second icon ("Layers") in the Controls section. 
Initially, you will see only the background layer listed. Click on
the '+' to select the data you want to have displayed. It should already 
suggest to visualize the network with the loaded `network.xml`, so just
click "Add". After a short moment, the network should be shown in the 
visualization area. Click the '+' again, but this time choose Vehicles as 
layer type. The `events.xml.gz` file will be already pre-selected. 
Click on "Add". As any layer depending on the events, a  
"Load Data" button will appear at the bottom of the layer tag. 
Click it to extract the vehicles' positions from the events.

 
(4) The logfile, with the above example in `output/example5/logfile.log` 
contains, between a lot of other information, also a dump of a the full 
matsim configuration.  If there are interesting parameters, you could try 
to copy then into your own config file, modify them, and re-run.

In my (kn's) view, one can actually get quite far in this way, i.e. by just editing the config file.  The main problem is how to obtain the network and in particular the so-called initial demand for your own scenario.  If you can't get that from somewhere else, it is probably better to go through the tutorial.