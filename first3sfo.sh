#!/usr/bin/env bash
awk -F',' 'BEGIN {print "ArrDelay,Orgin";OFS=","} $17=="SFO" {print $15,$17}' 2007.csv | head -4 > first3sfo.csv
