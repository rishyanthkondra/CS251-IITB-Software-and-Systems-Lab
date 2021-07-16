def isSquare(n):
    i=0
    while i*i<n :
       i = i+1
    if i*i==n :
        print(n,"is a square number")
    else :
        print(n,"is not a square number")

n = int(input())
num = [int(i) for i in input().split()]
j=0
while j<n :
    isSquare(num[j])
    j = j+1
