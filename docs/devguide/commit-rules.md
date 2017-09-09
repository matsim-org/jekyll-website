---
layout: default
title: Commit Rules
---

# Commit Rules


- **Code to be committed must compile.**
- **Use UTF-8 as file encoding.**

  Otherwise it may not compile on all machines.

- **By default, only commit to your personal contrib**. 

  Do not commit to `org.matsim.*` unless you are the maintainer of a package/module in `org.matsim.*`.
  
- **Create Pull-Requests for changes in `org.matsim.*`.** 
	
	Do not directly commit to `org.matsim.*`, but create a pull request with the changes
	you want to apply.

- **Write useful commit messages.**
- **Write your commit messages in English.**
- **Do not commit personal data (=non-code) files to the repository.**

  Exception is data for test cases, which must be committed to `test/input/*`. 
  See the [detailed discussion](/docs/devguide/data-in-source-repository) of this topic.
