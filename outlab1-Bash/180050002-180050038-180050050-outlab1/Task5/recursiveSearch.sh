#!/bin/bash

i=1

if [[ $# -eq 0 ]]
   then
       echo "Usage: ./recursiveSearch.sh <words-to-search>"
       exit 1

else
for word in $@
do
    if [[ i -eq 1 ]]
    then
	var="grep -inrwE $word Data"
	((i++))
else
    var="$var | grep -iw $word"
    fi
done
eval $var

fi

 


