BEGIN{FS=",";RS="\r\n";a=-1}
{
if(NR == 1){ 
 for(i=1;i<=20*(NF-1);i++) {printf "-";}
 print "";
 for(i=1;i<=NF;i++) {
 if($i=="Name")a=i;
 else printf("%20s",$i);}
 print ""; 
 for(i=1;i<=20*(NF-1);i++) {printf "-";}
 print "";}
else{
 for(i=1;i<=NF;i++){
 if(i!=a) printf("%20s",$i);}
 print "";
}}
