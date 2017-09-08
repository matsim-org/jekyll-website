---
layout: default
title: MATSim Benchmark
---

# MATSim Benchmark

The performance of MATSim depends on a lot of different factors:

- CPU-speed (although by far not always the limiting factor!)
- Memory-Bus / -Controller (we’re moving huge amounts of memory, the faster the better)
- File system (local Hard drive vs. RAID vs. NFS vs …)

To get a better understanding, under which circumstances MATSim performs best, we 
created a simple benchmark (performance test) that runs 20 iterations of a sample 
scenario with different settings. If you run the benchmark on your 
machine, we would be happy if you could send us your results.

## Download and Installation

Download the zip-file containing the benchmark: [benchmark.zip](/files/benchmark/benchmark.zip)  (35MB).

Unzip the downloaded file.

## Running the benchmark

On the command line, run the following: 

    java -Xmx500m -jar Benchmark.jar

This will generate a directory output with some files in it from the run. The test 
will usually run between 25 and 40 minutes. The benchmark requires Java 1.5 
or newer and 150MB free disk space. If you want to re-run the 
benchmark, rename or delete the ./output/ directory and run the test again.

## Submitting benchmark results

Please send an email to benchmark AT matsim DOT org containing:

- the file output/stopwatch.txt
- the file output/logfile.log
- a description of your benchmark environment, including:
  - vendor of machine (e.g. HP, Dell, Apple, etc.)
  - processor-type (vendor (Intel, AMD, etc.), model-number, clock-speed, cache-size, number of processors and cores, …)
  - memory (bus-speed, memory-controller, etc.)
  - storage system (rpm, cache size, …, type: e.g. local hard drive, RAID, …)
  - operation system
- any other information you think might be of interest to us

<!-- 
We collected some results and did a short analysis on them. 
Have a look at the results in the next section. 
If you want your results included as well or have some interesting findings 
yourself, please submit us your benchmark results.
 -->