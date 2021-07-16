#!/bin/bash
source ./resources/defineColors.sh

awk -F ',' ' BEGIN{OFS="  ";} {print $1,$2,$3,$4;}' $2 > Itstemp1
#cat Itstemp1
awk  '
BEGIN{
FS="  "
f["BLACK"]="'$BLACK_FONT'"
f["RED"]="'$RED_FONT'"
f["GREEN"]="'$GREEN_FONT'"
f["YELLOW"]="'$YELLOW_FONT'"
f["BLUE"]="'$BLUE_FONT'"
f["MAGENTA"]="'$MAGENTA_FONT'"
f["CYAN"]="'$CYAN_FONT'"
f["WHITE"]="'$WHITE_FONT'"
b["BLACK"]="'$BLACK_BACKGROUND'"
b["RED"]="'$RED_BACKGROUND'"
b["GREEN"]="'$GREEN_BACKGROUND'"
b["YELLOW"]="'$YELLOW_BACKGROUND'"
b["BLUE"]="'$BLUE_BACKGROUND'"
b["MAGENTA"]="'$MAGENTA_BACKGROUND'"
b["CYAN"]="'$CYAN_BACKGROUND'"
b["WHITE"]="'$WHITE_BACKGROUND'"
res="'$RESET_ALL'"
a=-1}
{if(FNR==NR) #{print $0,NF;
{if(FNR!=1) {p[$1]=f[$3];q[$1]=b[$4];}}
else if(FNR<NR)
{if(FNR<4) print $0;
else {
for(i in p) if($0 ~ i){
printf "%s%s%s%s\n",q[i],p[i],$0,res;
}}}}' Itstemp1 $1
rm Itstemp1
