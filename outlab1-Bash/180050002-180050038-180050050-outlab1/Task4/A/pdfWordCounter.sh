#!/bin/bash

#read -p "Enter the link: " website
#read -p "Enter the word: " word1

#let main=wget $website
 wget -O main $1
#echo $main
#echo $word1
 #grep -o -i $word1 pdftotext main | wc -w
pdftotext main -|grep -i -o -w $2 |wc -w
#main= wget $website
rm main
#grep -o -i $word1 pdftotext wget $website | wc -w
#grep -o --ignore-case $word1| pdftotext $main | wc -w







