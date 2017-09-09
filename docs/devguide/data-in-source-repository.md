---
layout: default
title: Data in the Source Repository
---

# Data in the Source Reporsitory

Some questions occurred about committing data to the MATSim project. 
To clarify what kind of data is allowed to commit and where to put it, here a short guideline:

1. Only commit source files in `src` and its subdirectories. Do not commit any data files under `src`!

2. If you need to use data during the development and you want to keep that data on a save 
place, please use internal storages of you institution (e.g. internal SVN/Git repositories, 
internal shared folders, etc.)

3. When you write JUnit test cases under `test/src`, you are allowed to add required data 
  to `test/input` or `test/scenario`. Then please follow the following constraints:
  
    - Use—if possible—already existing scenario data sets in `test/scenario`.

    - Add only *small* data sets (some KBytes to max. 2 MBytes) to `test/input` or `test/scenario`.
    Note that bigger files may be compressed with gzip since MATSim supports reading and 
    writing gzipped files with `org.matsim.utils.io.IOUtils.getBufferedReader()` and
    `IOUtils.getBufferedWriter()` respectively.

    - Use artificial or falsified data in test cases and put them under `test/input` or `test/scenario`.

