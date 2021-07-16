./q3.sh testcases/input1 > tmpout1
diff -bBZ tmpout1 testcases/output1 > result1
if [ -s result1 ]
then 
     echo "Test case-1 failed"
else
     echo "Test case-1 passed"
fi


./q3.sh testcases/input2 > tmpout2
diff -bBZ tmpout2 testcases/output2 > result2

if [ -s result2 ]
then 
     echo "Test case-2 failed"
else
     echo "Test case-2 passed"
fi

rm tmpout1 tmpout2 result1 result2