##
#@file
# File Documentation
#
# @brief This code is to manupulate lists in python
# @details The programs here uses basic python to find determinant of a matrix,to
# read a file,for binary search on a sorted list,
from sys import argv
from copy import deepcopy
## Given a file as an argument, returns a list which stores all the information in the file as a list of integers.
def make(filename):
	file = open (filename)
	l=[]
	for line in file:
		a=int(line)
		l.append(a)
	return l
## This function takes a list of integers and returns a sorted list in increasing order.
#The sorting is done based on bubble sort.
#We run  variable 'i' from 0 to n-1 and for each i ,we also run 'j' from
# 0 to n-i-1 and find maximum of elements from 0 to n-i-1 and bring that element to
# position 'n-i-1'.Such that zeroeth maximum comes to position n-1,next maximum gets to 'n-2'
# and so on.As a result the array or list is now increasingly sorted.
#\param l -> list to be sorted
#\return sorted list in increasing order 
def fun1(l):	
	size=len(l)
	for i in range(0,size-1):
		for j in range(0,size-i-1):
			if l[j] > l[j+1]:
				temp=l[j]
				l[j]=l[j+1]
				l[j+1]=temp
			
	return l
##We are performing Binary search on a sorted list.
#Checks if an integer x is present in a given list of integers 
#and returns the number of probes made to check if presentbut if not present then returns -1
#We consider to pointers e and s wrt the end and start f the list l respectively.
#Now mainting the condition that the  pointere is to the right of s,we find the middle
#element of the two pointers of the list and compare the middle element of the sublist to
#the element 'x';if it is greater than x then s becomes the m+1 or if it is less than x then e becomes 
#m-1 until s<=e or when middle element equals x.Then if the x is present in the list number of while 
#loops made is returned.or else -1 is returned. 
#\param l,x
#\return number of iterations made to find the element in the list if present else -1 
def fun2(l,x):
	n=int(x)
	probes=0
	s=0
	e=len(l)-1
	flag=0
	
	while(s<=e):
		probes=probes+1
		m=(s+e)//2
		print ("Probe "+str(probes)+":",m,l[m])
		if(l[m]==n):
			flag=1 ## if 'x' is in the list then flag is made 1 and loop is broken.
			break
		elif(l[m]>n):
			e=m-1##if sublist of l of starting from position s and 
		elif(l[m]<n):
			s=m+1
	if(flag==1):
		return probes
	else:	
		return -1
##This function calculates the determinant of the matrix given.
#\param L-> An n*n matrix
#\return d -> the determinant of a matrix L
def fun3(L):
 	#We take d,n as variables and finally return d as determinant of the matrix.
	d=0
	n=len(L)
	if(n==1):
		return L[0][0]
	for i in range(0,n):
		A=deepcopy(L)
		for j in range(0,len(A)):
			A[j].pop(i)
		A.pop(0)
		d=d+L[0][i]*((-1)**i)*fun3(A)
		print(d)
	return d
L = make("data")
#Storing all the information in data file as a list in L.
print (L)
L = fun1(L)
#L changed after applying f1 on it.
print ("\nAfter Fun1:")
print (L)
print ("\nFun2 Starts:")
#Do fun2 on L and store it in ans
ans = fun2(L, 48)
print ("Result of Fun2:", ans)
print ("\n")
# Change the elements and observe the result  
#define new L as L = [[1, 2, 3], [100, 54, 23], [9, 27, 11]]
L = [[1, 2, 3], [100, 54, 23], [9, 27, 11]]
print(L)
#Apply fun3 on L and store it as ans
ans = fun3(L)
#Print ans
print ("Result of Fun3:", ans)