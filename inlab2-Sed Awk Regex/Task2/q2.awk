# Your code goes here.


BEGIN { RS="!";FS=",";OFS="\t";
    print "Value\tSensorNumber";}
 { print $1,$2;}
