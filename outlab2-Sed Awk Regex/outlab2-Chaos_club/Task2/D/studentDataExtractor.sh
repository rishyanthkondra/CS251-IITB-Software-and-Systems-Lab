#!/bin/bash

i=0
a=0
b=0
c=0
d=0
e=0
g=0
f=0
cp $1 var.txt
echo "\n" >> var.txt 
while IFS= read -r line || [ "$line" ]
do
      j=$((i%6))
      if [[ j -eq 1 ]]
      then
	  a=$line
      elif [[ j -eq 2 ]]
      then
	  b=$line
	  g=$(echo $line | cut -d ":" -f2)
      elif [[ j -eq 3 ]]
      then
	  c=$line
      elif [[ j -eq 4 ]]
      then
	  d=$line
      elif [[ j -eq 5 ]]
      then
	  e=$line
      elif [[ j -eq 0 ]] && [[ ! i -eq 0 ]]
      then
	echo  $a >> $g.txt
	echo  $b >> $g.txt
	echo  $c >> $g.txt
	echo  $d >> $g.txt
	echo  $e >> $g.txt
      fi
     (( i++ ))
      
done < var.txt
      
rm var.txt
