#!/bin/bash

times=0
number=0

until [ $number -eq 42 ]
do

    number=$(./randomNumber.sh 2)
    
echo $number >> howFarFromTruth.txt

(( times++ ))
done

