touch ItsTemp1 ItsTemp2 ItsTemp3
head -n 1 $1 > ItsTemp1
grep $3 $1 | grep $4 >> ItsTemp1
#cat ItsTemp1
awk '
BEGIN{a=-1;b=7;OFS=",";FS=",";}
{if(NR==1){
for(i=1;i<=NF;i++){
if($i == "letterGrade") b=i;
if($i == "Credits") a=i;
}
#printf b;
}
else{
print $a,$b;
}}' ItsTemp1 > ItsTemp2
#cat ItsTemp1
awk -F ',' 'FNR==NR&&FNR>1 { ar[$1]=$2;next } { for (j in ar) gsub(j,ar[j]) }1' $2 ItsTemp2 > ItsTemp3
awk -F ',' '{n+=$1;sum+=$1*$2;}
END {
if (n >0){
sum = sum / n;
printf("%.4f",sum);}
else printf "0.0";
print ""}' ItsTemp3
rm ItsTemp1 ItsTemp2 ItsTemp3
