#! /bin/bash

text=$2
valueas=$(printf "%d\n" \'$1) 

key=$(($valueas - 65))

if [ $key == 0 ] ;  then
  echo $text | tr '[A-Z]' '[A-Z]'
elif [ $key == 1 ] ;then
 echo $text | tr '[A-Z]' '[B-ZA]'
elif [ $key == 2 ] ; then
 echo $text | tr '[A-Z]' '[C-ZA-B]'
elif [ $key == 3 ] ; then
 echo $text | tr '[A-Z]' '[D-ZA-C]'
elif [ $key == 4 ] ; then
 echo $text | tr '[A-Z]' '[E-ZA-D]'
elif [ $key == 5 ] ; then
 echo $text | tr '[A-Z]' '[F-ZA-E]'
elif [ $key == 6 ] ; then
 echo $text | tr '[A-Z]' '[G-ZA-F]'
elif [ $key == 7 ] ; then
 echo $text | tr '[A-Z]' '[H-ZA-G]'
elif [ $key == 8 ] ; then
 echo $text | tr '[A-Z]' '[I-ZA-H]'
elif [ $key == 9 ] ; then
 echo $text | tr '[A-Z]' '[J-ZA-I]' 
elif [ $key == 10 ] ; then
 echo $text | tr '[A-Z]' '[K-ZA-J]'
elif [ $key == 11 ] ; then
 echo $text | tr '[A-Z]' '[L-ZA-K]'
elif [ $key == 12 ] ; then
 echo $text | tr '[A-Z]' '[M-ZA-L]'
elif [ $key == 13 ] ; then
 echo $text | tr '[A-Z]' '[N-ZA-M]'
elif [ $key == 14 ] ; then
 echo $text | tr '[A-Z]' '[O-ZA-N]'
elif [ $key == 15 ] ; then
 echo $text | tr '[A-Z]' '[P-ZA-O]'
elif [ $key == 16 ] ; then
 echo $text | tr '[A-Z]' '[Q-ZA-P]'
elif [ $key == 17 ] ; then
 echo $text | tr '[A-Z]' '[R-ZA-Q]'
elif [ $key == 18 ] ; then
 echo $text | tr '[A-Z]' '[S-ZA-R]'
elif [ $key == 19 ] ; then
 echo $text | tr '[A-Z]' '[T-ZA-S]'
elif [ $key == 20 ] ; then
 echo $text | tr '[A-Z]' '[U-ZA-T]'
elif [ $key == 21 ] ; then
 echo $text | tr '[A-Z]' '[V-ZA-U]'
elif [ $key == 22 ] ; then
 echo $text | tr '[A-Z]' '[W-ZA-V]'
elif [ $key == 23 ] ; then
 echo $text | tr '[A-Z]' '[X-ZA-W]'
elif [ $key == 24 ] ; then
 echo $text | tr '[A-Z]' '[Y-ZA-X]'
elif [ $key == 25 ] ; then  
 echo $text | tr '[A-Z]' '[ZA-Y]'
fi
