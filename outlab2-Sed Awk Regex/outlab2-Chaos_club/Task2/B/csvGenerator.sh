#!/bin/bash

sed -e 's/Student Name://g' $1 | sed 's/Roll Number://g' | sed 's/CPI://g' | sed 's/Department://g' | sed 's/Courses Undertaken://g' | awk 'NF' | awk 'BEGIN{FS="\n";RS="--------------------------------------------------------------------";OFS="|"}{if(NF!=0) {print $2,$3,$4,$5,$6}}' | sed '1 i\Student Name|Roll Number|CPI|Department|Courses Undertaken' > studentData.csv
