#!/bin/bash

cd $1
list=$(ls *.txt)
cd -

for file in $list
	    do

		var=$(sed -e 's/Student Name://g' $1$file | sed 's/Roll Number://g' | sed 's/CPI://g' | sed 's/Department://g' | sed 's/Courses Undertaken://g' | awk 'NF' | awk 'BEGIN{FS="\n";RS="?";OFS="|"}{if(NF!=0) {print $4}}')

	        var=$(echo $var | sed -e 's/ //g')
		mkdir $var
		cp $1$file $var

done 

rm -rf b=0
