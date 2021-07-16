# Your code goes here.

awk 'BEGIN{OFS="\t";}
{if(NR==1){$5="Points";print $1,$2,$3,$4,$5;} 
 else{$5=4*$3+2*$4;print $1,$2,$3,$4,$5;}}' $1
