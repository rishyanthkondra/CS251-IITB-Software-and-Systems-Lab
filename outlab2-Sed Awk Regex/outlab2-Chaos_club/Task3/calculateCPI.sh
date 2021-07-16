touch ItsTemp1 ItsTemp2
awk '
BEGIN{a=-1;b=7;OFS=",";FS=",";}
{if(NR==1){
for(i=1;i<=NF;i++){
if($i == "letterGrade") b=i;}
for(i=1;i<=NF;i++){
if($i == "Credits") a=i;}
#print a,b;
}
else{
print $a,$b;
}}' $1 > ItsTemp1
#cat ItsTemp1
awk -F ',' 'FNR==NR&&FNR>1 { ar[$1]=$2;next } { for (j in ar) gsub(j,ar[j]) }1' $2 ItsTemp1 > ItsTemp2
awk -F ',' '{n+=$1;sum+=$1*$2;}
END {
if (n>0){
sum = sum / n};
printf("%.4f",sum);
print ""}' ItsTemp2
rm ItsTemp1 ItsTemp2
