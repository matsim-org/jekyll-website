---
layout: post
author: Kai Nagel
title: "Events comparison in regression tests"
summary: "A more flexible way to retrofit events comparison in regression tests."
---

There are many tests that at some point run
```
EventsFileComparator.compare( filename1, filename2 )
```
I have now, somewhat as an experiment, added coordinates into the person arrival events.  This will break the strict events comparison.

I have therefore made the events comparison somewhat more flexible; you can now write
```
new EventsFileComparator()
    .setIgnoringCoordinates(true)
    .runComparison(filename1, filename2)
```
This will then ignore the coordinates in the comparison, and thus make the test pass again (if nothing else is broken).  

Since we are planning to play around a bit more with this (in the context of visualization), I would recommend to use this switch rather than replacing the reference events files.
