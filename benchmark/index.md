---
layout: default
title: MATSim Benchmark
---

# MATSim Benchmark

<div class="panel panel-info">
  <div class="panel-heading">
    <h3 class="panel-title">New MATSim Benchmark v2</h3>
  </div>
  <div class="panel-body" >
      <p>We've updated our benchmark to better represent today's use cases of MATSim in September 2022.
      </p>
  </div>
</div>

The performance of MATSim depends on a lot of different factors:

- CPU-speed (although by far not always the limiting factor!)
- Memory-Bus / -Controller (we’re moving huge amounts of memory, the faster the better)
- File system (local Hard drive vs. RAID vs. NFS vs …)

To get a better understanding, under which circumstances MATSim performs best, we 
created a simple benchmark (performance test) that runs 20 iterations of a sample 
scenario with different settings. If you run the benchmark on your 
machine, we would be happy if you could send us your results.

## Download and Installation

Download the zip-file containing the benchmark: [matsim-benchmark-2.0.0.zip](/files/benchmark/matsim-benchmark-2.0.0.zip)  (180 MB).

Unzip the downloaded file.

## Running the benchmark

On the command line, run the following: 

    java -Xmx6g -jar matsim-benchmark-2.0.0.jar

This will generate a directory `output` with some files in it from the run.  
The test will usually run **between 30 and 60 minutes**, depending on your system.  
The benchmark can run with **Java 11 and Java 17** (and likely other versions, but they were not tested).  
If you want to re-run the benchmark, rename or delete the `./output/` directory and run the test again.

## Submitting benchmark results

Please send an email to benchmark AT matsim DOT org containing:

- the file `output/stopwatch.txt`
- the file `output/logfile.log`
- a description of your benchmark environment, including:
  - vendor of machine (e.g. HP, Dell, Apple, etc.)
  - processor-type (vendor (Intel, AMD, etc.), model-number, clock-speed, cache-size, number of processors and cores, …)
  - memory (bus-speed, memory-controller, etc.)
  - storage system (rpm, cache size, …, type: e.g. local hard drive, RAID, …)
  - operation system
- any other information you think might be of interest to us


We plan to provide an aggregated analysis of benchmark results once we received a certain
amount of results.

<!-- 
We collected some results and did a short analysis on them. 
Have a look at the results in the next section. 
If you want your results included as well or have some interesting findings 
yourself, please submit us your benchmark results.
 -->