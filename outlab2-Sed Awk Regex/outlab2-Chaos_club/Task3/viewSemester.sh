touch ItsTemp1 ItsTemp2
head -n 3 $1 > ItsTemp1
grep -w $2 $1 | grep -w $3 > ItsTemp2
sort -k 5,4 ItsTemp2 -o ItsTemp2
cat ItsTemp2 >> ItsTemp1
cat ItsTemp1
rm ItsTemp1
rm ItsTemp2
#to sort yet ,,DONE!!
