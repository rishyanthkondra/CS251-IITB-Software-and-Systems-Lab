#!/bin/bash

n=$1
val=1
re='^[0-9]+$'

if ! [[ $n =~ $re ]]
    then
	echo "Invalid argument!"
	val=2

 elif [[ n -eq 2 ]] || [[ n -eq 3 ]]
    then
     val=1


elif [[ $((n % 2)) -eq 0 ]] || [[ $((n % 3)) -eq 0 ]]
    then
    val=0

else
    i=5
    w=2
 while [[ $((i * i)) -lt n ]] || [[ $((i*i)) -eq n ]]
    do
        if [[ $((n % i)) -eq 0 ]]
	then
            val=0
	    break
        fi
        i=$((i + w))
        w=$((6 - w))
    done
fi

if [[ val -eq 1 ]]
   then
   echo Prime Year!

elif [[ val -eq 0 ]]
     then
       echo Not a prime year

 fi
