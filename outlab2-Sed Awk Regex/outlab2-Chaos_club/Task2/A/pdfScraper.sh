#!/bin/bash

i=1

wget -qcO - $1 > studentData.pdf

pdftotext studentData.pdf var

rm studentData.pdf

while read -r line
do
    if [[ $line =~ "-" ]]
    then
	if [[ i -eq 1 ]]
	then
	    echo $line >> test.txt
	    (( i++ ))
       else    
	echo "" >> test.txt
	echo $line >> test.txt
	fi
    elif [[ $line == "" ]]
    then
	continue
    elif [[ $line =~ "Name:" ]]
    then
	echo $line >> test.txt
    elif [[ $line =~ "Number:" ]]
    then
	echo $line >> test.txt
    elif [[ $line =~ "CPI:" ]]
    then
	echo $line >> test.txt
    elif [[ $line =~ "Department:" ]]
    then
	echo $line >> test.txt
    elif [[ $line =~ "Undertaken:" ]]
    then
	echo -n $line" ">> test.txt
    else
	echo -n $line" ">> test.txt
    fi
    
done < var

rm var
echo "" >> test.txt
iconv -c -f utf-8 -t ascii test.txt | tr -cd "[:print:]\n" | sed 's/ *$//' > studentData.txt

rm test.txt
