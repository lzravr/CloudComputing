#!/bin/bash

# MEM=`kubectl get hpa | awk '/api/{ print $3 }' | awk -F"/" '{print $1}'`
# echo $MEM
REP=`kubectl get hpa | awk '/api/{ print $6 }'`
# echo $REP
KOL=40

echo TIME,REPLICAS,MEMORY > load.csv

while [ $REP -lt 8 ]
do
    echo $KOL
    curl http://147.91.204.85:31646/index.php?kolicinaMemorije=$KOL

    sleep 45s

    # prosecna memorija
    # MEM=`kubectl get hpa | awk '/api/{ print $3 }' | awk -F"/" '{print $1}'`

    # suma zauzete memorije u svim podovima
    MEM=`kubectl top pods | awk '/api/{ print $3 }' | awk -F"M" '{sum += $1} END {print sum}'`
    REP=`kubectl get hpa | awk '/api/{ print $6 }'`
    KOL=`echo $KOL + 10 | bc`
    echo `date +%s`,$REP,$MEM >> load.csv
done

while [ $REP -ne 1 ]
do
    REP=`kubectl get hpa | awk '/api/{ print $6 }'`
    sleep 1m
done

MEM=`kubectl top pods | awk '/api/{ print $3 }' | awk -F"M" '{sum += $1} END {print sum}'`

echo `date +%s`,$REP,$MEM >> load.csv