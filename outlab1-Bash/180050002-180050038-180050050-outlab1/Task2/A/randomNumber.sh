#!/bin/bash

n=$1
num=0
x=$((n-2))
y=$((n-1))

if [[ n -eq 0 ]]
then
echo invalid input


else
for value in $( seq 0 $x )
do
ran=$(od -A n -t d -N 1 /dev/urandom)
use=$(($ran%10))
pow=$((10**$value))
next=$(($use*$pow))
num=$(($num+$next))
done

ran=$(od -A n -t d -N 1 /dev/urandom)
use=$(($ran%10))

while [ $use -eq 0 ]
do
ran=$(od -A n -t d -N 1 /dev/urandom)
use=$(($ran%10))
done

pow=$((10**$y))
next=$(($use*$pow))
num=$(($num+$next))

echo $num
fi
