#! /bin/bash
wget $1 -rq robots=off -np -P $2
tree  $2 -J > urlReport.json
md5sum urlReport.json | cut -f 1 -d " "
number=$(grep -oh "{"  urlReport.json | wc -w)
echo $number
proces=$(ps -q $number -o comm=)
#echo $proces
if [ -z  "$proces" ]
then
    echo No such process
else
    echo $proces
 fi
