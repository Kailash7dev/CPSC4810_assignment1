#!/usr/bin/env bash 
(echo "dest,count" && awk -F',' 'NR>1{arr[$17]++}END{for (a in arr) print a,",", arr[a]}' 2007.csv  | sort -k3 -rn | head -3 ) > top3dest.csv
echo 'kailash'
