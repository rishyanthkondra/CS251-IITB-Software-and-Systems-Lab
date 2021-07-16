#! /bin/bash

text=$1 
i=0

#echo $i
#if [ i == 0 ] ; then
 output1=$(echo $text)  
final="A "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 1 ] ; then
  output1=$(echo $text | tr '[B-ZA]' '[A-Z]')
 final="B "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 2 ] ; then
 output1=$(echo $text | tr '[C-ZA-B]' '[A-Z]') 
 final="C "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 3 ] ; then 
 output1=$(echo $text | tr '[D-ZA-C]' '[A-Z]') 
final="D "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 4 ] ; then
 output1=$(echo $text | tr '[E-ZA-D]' '[A-Z]') 
final="E "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 5 ] ; then
 output1=$(echo $text | tr '[F-ZA-E]' '[A-Z]') 
final="F "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 6 ] ; then
 output1=$(echo $text | tr '[G-ZA-F]' '[A-Z]') 
final="G "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 7 ] ; then
 output1=$(echo $text | tr '[H-ZA-G]' '[A-Z]') 
final="H "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 8 ] ; then
 output1=$(echo $text | tr '[I-ZA-H]' '[A-Z]') 
final="I "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 9 ] ; then
 output1=$(echo $text | tr '[J-ZA-I]' '[A-Z]') 
final="J "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 10 ] ; then
 output1=$(echo $text | tr '[K-ZA-J]' '[A-Z]') 
final="K "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 11 ] ; then
 output1=$(echo $text | tr '[L-ZA-K]' '[A-Z]') 
final="L "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 12 ] ; then
 output1=$(echo $text | tr '[M-ZA-L]' '[A-Z]') 
final="M "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 13 ] ; then
 output1=$(echo $text | tr '[N-ZA-M]' '[A-Z]') 
final="N "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 14 ] ; then
 output1=$(echo $text | tr '[O-ZA-N]' '[A-Z]') 
final="O "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 15 ] ; then
 output1=$(echo $text | tr '[P-ZA-O]' '[A-Z]') 
final="P "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 16 ] ; then
 output1=$(echo $text | tr '[Q-ZA-P]' '[A-Z]') 
final="Q "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 17 ] ; then
 output1=$(echo $text | tr '[R-ZA-Q]' '[A-Z]') 
final="R "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 18 ] ; then
 output1=$(echo $text | tr '[S-ZA-R]' '[A-Z]') 
final="S "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 19 ] ; then
 output1=$(echo $text | tr '[T-ZA-S]' '[A-Z]') 
final="T "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 20 ] ; then
 output1=$(echo $text | tr '[U-ZA-T]' '[A-Z]') 
final="U "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 21 ] ; then
 output1=$(echo $text | tr '[V-ZA-U]' '[A-Z]') 
final="V "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 22 ] ; then
 output1=$(echo $text | tr '[W-ZA-V]' '[A-Z]') 
final="W "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 23 ] ; then
 output1=$(echo $text | tr '[X-ZA-W]' '[A-Z]') 
final="X "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 24 ] ; then
 output1=$(echo $text | tr '[Y-ZA-X]' '[A-Z]') 
final="Y "$output1
echo $final 
i=$(($i + 1))
#elif [ i == 25 ] ; then  
 output1=$(echo $text | tr '[ZA-Y]' '[A-Z]')
final="Z "$output1
echo $final 
#i=$(($i + 1))
 
