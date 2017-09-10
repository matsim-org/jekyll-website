---
layout: default
title: Working behind a Proxy
---

# Working behind a Proxy

Things are getting a bit cumbersome if you are behind a proxy server. Apparently, 
Java ignores your system wide proxy settings (checked on Linux Mint 16, 
Windows Server 2008, Mac OS 10.9), that is, you need to configure each piece 
of software that is involved in your build process separately. Usually, 
this includes Eclipse and Maven.

## Eclipse

Go to `Preferences > General > Network Connections` and enter your proxy settings. 
Set `Active Provider` to `Manual`. The `Native` option did never work for 
me (JI apr'14). Users report that one should leave the SOCKS field empty. You may need to restart Eclipse.

## Maven

Edit your maven settings file (or create if not existing) `~/.m2/settings.xml` to look like that:

    <?xml version="1.0" encoding="UTF-8"?>
    <settings xmlns="http://maven.apache.org/SETTINGS/1.1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd">
   
      <proxies>
        <proxy>
          <active>true</active>
          <protocol>http</protocol>
          <host>localhost</host>
          <port>3128</port>
          <nonProxyHosts>127.0.0.1</nonProxyHosts>
        </proxy>
      </proxies>
    
    </settings>
 
If neccessary, add `<username>` and `<password>` fields (see 
also [here](https://maven.apache.org/guides/mini/guide-proxies.html)). Double 
check that Eclipse is using the correct settings file (`Preferences > Maven > User Settings`).

## NTLM Authentification

Things are getting even worse, if you are behind a proxy that uses NTLM 
authentification (usually Windows based networks). As far as my experience 
goes (JI apr'14) none of the above java tools can talk to a NTLM based proxy. 
The only work around is to run a local NTLM-capable proxy on your machine that 
handles the authentification. There is [cntlm](http://cntlm.sourceforge.net/) which 
works flawlessly for me (JI apr'14), or [Java NTLM Proxy](http://java-ntlm-proxy.sourceforge.net/) 
and [NTLMaps](http://sourceforge.net/projects/ntlmaps/) (both I have not tested).
