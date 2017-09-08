---
layout: default
title: Coding Conventions
---

# Coding Conventions


For a project the size of MATSim, we need a minimal set of guidelines to insure the stability
of MATSim and enable its further development. We try to keep this list as short as possible.

- **We try to follow the [Java Code Conventions](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html)**
  
  This includes the [Naming Conventions](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-135099.html#367)
  (Classes start with capital letters, variables with lowercase letters, ...), the 
  [usage of braces in `if` statements](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-142311.html#449)
  and other stuff. A notable exception are line lengths (we have no problem with lines up to 132 characters).
  
  Also, source code should only contain ASCII characters in code. Non-ascii in comments are ok; 
  non-ascii in Strings should be avoided but sometimes cannot (e.g. file readers).
  
  More detailed [Naming Conventions for MATSim](/docs/devguide/naming-conventions) are also available.
  
- **Indentation**

  MATSim Source code is indented with tabs, not spaces.

- **Code is consistent and compiles!**

  Code committed to the repository has to compile - always. If you want to try out some 
  stuff, do it somewhere else or do not commit it. Classes in `org.matsim.*` do not 
  reference other classes outside of the `org.matsim.*`-package except for classes 
  provided by third-party libraries. Especially, `org.matsim.*`-classes must not 
  reference `tutorial` and `contrib`-classes.

- **All our code files have the MATSim-specific GPL-Header**

  In Eclipse, you could add the header to the code template, so every new Java file 
  has this header set by default. To do this, go to the global Preferences in 
  Eclipse (Menu: Window &gt; Preferences), navigate to Java &gt; Code Style &gt; 
  Code Templates. Choose "Code &gt; New Java files" and click on "Edit...". 
  Paste there the following text:
  
      /* *********************************************************************** *
       * project: org.matsim.*
       * *********************************************************************** *
       *                                                                         *
       * copyright       : (C) ${year} by the members listed in the COPYING,        *
       *                   LICENSE and WARRANTY file.                            *
       * email           : info at matsim dot org                                *
       *                                                                         *
       * *********************************************************************** *
       *                                                                         *
       *   This program is free software; you can redistribute it and/or modify  *
       *   it under the terms of the GNU General Public License as published by  *
       *   the Free Software Foundation; either version 2 of the License, or     *
       *   (at your option) any later version.                                   *
       *   See also COPYING, LICENSE and WARRANTY file                           *
       *                                                                         *
       * *********************************************************************** */
      
      ${filecomment}
      ${package_declaration}
      
      ${typecomment}
      ${type_declaration}
      

- **We use meaningful commit-messages**

  Commit messages help to rule out quickly some revision of a file when looking for 
  specific changes that, for example, may have introduced a bug in the code. 
  Useless or empty commit messages make it more cumbersome, as the file itself 
  must be looked at in each revision. Additionally, we write commit-messages 
  (as well as comments in the code) in English, as development takes place 
  in many different areas, and not only in german-speaking Countries.

- **Do not commit personal test-data**

  Use another repository if you want to version your personal test-data. 
  We often work with data we are not allowed to share, and our code repository 
  is open to anyone. It is a bad idea to store test-data in this repository, 
  because sooner or later somebody will commit confidental data to the repository 
  which cannot be removed! Some simple test-data is available in the 
  directory `examples`, which is maintained by the core developers – please
  contact them if you want to add your own examples to this directory.
