touch ItsTemp1 ItsTemp2
head -n 3 $1 > ItsTemp1
awk -v "Str=$2" -v "a=-1" -F '  ' '
{
if(NR==2){
for(i=1;i<=NF;i++){
if($i == "Code") a=i;}}
#{print i,$i,a;}}
else if(NR>=4){
if($a ~ Str){print $0 }#| "sort -u"}
}}' $1 > ItsTemp2
sort -k 5,4 ItsTemp2 -o ItsTemp2
cat ItsTemp2 >> ItsTemp1
cat ItsTemp1
rm ItsTemp1
rm ItsTemp2
