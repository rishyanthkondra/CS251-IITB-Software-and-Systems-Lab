#!/bin/bash

cut -d ',' -f1,2,3 $1 > $2
cut -d ',' -f1,4,5 $1 >> $2
cut -d ',' -f1,6,7 $1 >> $2
sort -t ',' -k1 $2 -o $2   
sort -t ',' -k3 $2 -o $2
