---
layout: default
title: Naming Conventions
---

# Naming Conventions


- We follow the [Naming Conventions](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-135099.html#367)
  from Oracle's [Java Code Conventions](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html).
  Short version: Use CamelCase in general, with:
  - Classes and Interfaces starting with uppercase letters
  - Methods, packages and variables/members starting with lowercase letters
  - Constants use all-uppercase letters together with underscores ("_").

- Abbreviations should be avoided:
  - ~~`getTravTime()`~~  >>  `getTravelTime()`
  - ~~`getDist()`~~  >>  `getDistance()`
- `Id` is an abbreviation for Identifier, the 'd' is thus usually a lowercase letter.
- Factory methods are named `create*()`, e.g. `createLink()`. `newLink()` or other names should be avoided.
- Abstract classes should start with `Abstract`, e.g. `AbstractPersonAlgorithm`.
- Interfaces are **not** specially marked in their name, e.g. there is no pre- or suffix `I` like `SomeInterfaceI`.
- Default Implementations of interfaces end on `Impl`, if no more specific class-name is suitable, e.g. `PlanImpl implements Plan`.