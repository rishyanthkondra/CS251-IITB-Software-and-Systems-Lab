#!/bin/bash
sum=0
K=$1
times=0
for value in $( seq 1 $K)
do
    export times
    . ./findTheAnswer.sh
sum=$((sum+times))

done

av=$((sum/K))
echo $av
rm howFarFromTruth.txt
