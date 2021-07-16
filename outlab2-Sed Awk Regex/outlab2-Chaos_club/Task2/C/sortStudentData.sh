#!/bin/bash
   
sort -Vrt '|' -k3 $1 > sortedStudentData.csv
cut -d "|" -f 1 sortedStudentData.csv | sed -n '2,6 p'  > top5Students.txt
