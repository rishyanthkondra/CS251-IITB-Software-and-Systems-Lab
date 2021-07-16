# Your code goes here. 
# Temporarily it has a command which replace all occurences of a in a file to a. and all occurences of b to b. you need to overwrite the same
awk '{print tolower($0)}' $1 > temp1
awk 'BEGIN{OFS="\n";}{for(i=1;i<=NF;i++) print $i}' temp1 > temp2
rm temp1 
sed 's/^[[:punct:]]\+//g' temp2|sed 's/[[:punct:]]\+$//g'|sed -n '/^[[:punct:]]*$/d;p'> temp3
rm temp2
sed -e '/^$/d' temp3 > temp4
rm temp3
awk '!seen[$0]++' temp4 > temp5
rm temp4
awk '{print|"sort -u"}' temp5
rm temp5
