---
layout: default
title: Configuration Conventions
---

# Configuration Conventions


For non-programmers, MATSim is configured via the config file.  
(For extensions, we have not yet found a good solution.)  
If you make your code configurable, please observe the following hints.

## Avoid automagic

Examples for automagic are:

- If the code finds a file of a certain type, then do something special.
- If the code finds a config module of a certain type, then do something special.
- If some values are overwritten then some other values are cleared.

The problem with such automagic is that it is nearly impossible to write code 
that is robust against typoes.  As a result, one gets warnings such as

- "File of certain type not found, thus assuming ..."  (This may either be a deliberate user decision, or a typo on the filename.)
- "Config module of a certain type not found, thus assuming ..." (This may either be a deliberate user decision, or a type in the module name.)
- "Config module of a certain type found, thus assuming ..." (This may be a leftover module from some other experiments.)
- "When you are overwriting value X please remember that this also affects values Y and Z." (Which may be what the user wants, or not.)

If a user is not able to switch off warnings, she or he will eventually start to ignore them.  Which is not good. In that sense:

## Avoid warnings that cannot be switched off

If a user is not able to switch off warnings, she or he will eventually start to ignore them.  Two aspects:

- Automagic should be avoided (see above).
- If the user is doing something non-standard/not-recommended, this may lead to a warning.
  It would make sense to provide a switch to disable such warnings. (Makes the configuration file a lot longer, though.)
