#!/usr/bin/env bash

export JAVA_OPTS="-Xms100m -Xmx2000m -Dcom.sun.management.jmxremote"
../apache-flume-1.9.0-bin/bin/flume-ng agent \
   -f /home/acerrato/m3_indiv/flume_indiv/ejercicio1/conf/flume_bicimad_stations.conf \
   --name Agent1 \
   -Dflume.root.logger=INFO,console


#####################################################
## Para enviar datos:
##  
##  $> nc localhost 1357
##  blbblalalablba
##  OK
##  dlsakjdlakjdsalk
##  OK
#####################################################

