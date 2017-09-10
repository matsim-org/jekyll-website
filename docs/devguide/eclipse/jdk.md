---
layout: default
title: Run Eclipse with a JDK
---

# Run Eclipse with a JDK

Maven requires Eclipse using a JDK, i.e. Java Development Kit, instead of a Java 
Runtime Environment (JRE). The main difference is that a JDK also contains a 
Java Compiler and other tools to develop Java Code, while the JRE is only able 
to run compiled Java applications.

To check with what Java version (JRE or JDK) Eclipse is running, do the following:

- Open the menu item `Help > About Eclipse`. (On the Mac, it's in the Eclipse-menu, not the Help-menu)
- Click on `Installation Details`.
- Switch to the tab `Configuration`
- Search for a line that starts with `-vm`. The line following it shows which Java binary is used.

Depending on the name and location of the used Java binary one can figure out if a JRE or a JDK is used:

- If the path contains "jre" (e.g. as in `C:\Program Files\Java\jre6\bin\client\jvm.dll`) it is a JRE
- If the path contains "jdk" (e.g. as in `C:\Program Files\Java\jdk1.6.0_31\bin\javaw.exe`) it is a JDK.

If no JDK is used for Eclipse, change it:

- Quit Eclipse if it is running
- Go to the Eclipse installation directory and open the file `eclipse.ini` in a text editor.
- Search for the line `-vmargs`
- Before the line `-vmargs`, add two lines:
  
  On the first line, write `-vm`
  
  On the second line, write the path to your JDK installation (usually something 
  like: `C:\Program Files\Java\jdk1.6.0_31\bin\javaw.exe` on Windows)

