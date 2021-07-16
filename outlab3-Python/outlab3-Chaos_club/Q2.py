import re
import os
import sys
# from collections import Counter
# path-to-diary=sys.agrv[1]
contact=sys.argv[2]
file_name=open(sys.argv[1],'r')
string_file=file_name.read()
file_name.close()
def removing_dot(stri):
	while stri[0]=='.':
		stri=stri[1:]
	else:
		return stri

# string_check="Today I met him emo&__43k.id@guys.com ,2876543234. the boy in the middle of this whole love story."
email_proto1=re.findall(r"\b[0-9a-zA-Z]+[0-9a-zA-Z\.\_]+[0-9a-zA-Z]+@[0-9a-zA-Z\.]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
# number_contacts=re.findall(r"\b[\.\,\'\;\:\"\(\!\`\-]*[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][\.\,\'\;\:\"\)\!\`\-]*\b",s)
number_contacts=re.findall(r"\b[1-9]\d{9}\b",string_file)
email_proto2=re.findall(r"\b[0-9a-zA-Z\.\_]+[\.\_]+[\.\_]+[0-9a-zA-Z]+@[0-9a-zA-Z\.\_]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_proto3=re.findall(r"\b[0-9a-zA-Z\.\_]+[0-9a-zA-Z]+@[0-9a-zA-Z\.]+[\.\_]+[\.\_]+[0-9a-zA-Z]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_proto4=re.findall(r"\b[0-9a-zA-Z\.\_]+[0-9a-zA-Z]+@\_+[0-9a-zA-Z\.\_]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_proto5=re.findall(r"\b[0-9a-zA-Z\.\_]+[0-9a-zA-Z]+[\.\_]+@[0-9a-zA-Z\.\_]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_proto6=re.findall(r"\b[0-9a-zA-Z\.\_]+[0-9a-zA-Z]+@\.+[0-9a-zA-Z\.\_]+\.[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_add1=re.findall(r"\b\.[\.]+[0-9a-zA-Z][0-9a-zA-Z\.\_]*[0-9a-zA-Z]*@[0-9a-zA-Z]+[0-9a-zA-Z\.]+[a-zA-Z\.]+[a-zA-Z]\b",string_file)
email_edit1=re.findall(r"\b[0-9a-zA-Z][0-9a-zA-Z]*@[0-9a-zA-Z][0-9a-zA-Z\.]*[a-zA-Z]*\b",string_file)
email_remo1=re.findall(r"\b\.[0-9a-zA-Z][0-9a-zA-Z]*@[0-9a-zA-Z][0-9a-zA-Z\.]*[a-zA-Z]*\b",string_file)
print(email_edit1)

email_add2=[]
for i in range(0,len(email_add1)):
	# email_add2=[removing_dot(x) for x in email_add1]
	val=removing_dot(email_add1[i])
	email_add2.append(val)
email_remo2=[]
for i in range(0,len(email_remo1)):
	# email_add2=[removing_dot(x) for x in email_add1]
	val=removing_dot(email_remo1[i])
	email_remo2.append(val)	
print(email_remo2)
email_edit1=[x for x in email_edit1 if x not in email_remo2]
# print(email_edit1)
print(email_edit1)
email_proto2=email_proto2+email_proto3+email_proto4+email_proto5+email_proto6+email_add2+email_edit1
# print(email_add2)
email_final=[x for x in email_proto1 if x not in email_proto2 ]
final_list=number_contacts+email_final+email_add2+email_edit1

def CountKey(my_list): 
 # Creating an empty dictionary  
	freq = {} 
	output_list=[]
	for items in my_list: 
		freq[items] = my_list.count(items)       
	for key, value in freq.items(): 
		output_list.append(key)
	return output_list
def CountValue(my_list): 
 # Creating an empty dictionary  
    freq = {} 
    output_list=[]
    for items in my_list: 
        freq[items] = my_list.count(items) 
    for key, value in freq.items(): 
         output_list.append(value)
    return output_list  

frequency_list=CountValue(final_list)
key_list=CountKey(final_list)

ref_po=-1
for i in range(0,len(key_list)):
	if contact==key_list[i]:
		ref_po=i
		break
if ref_po>=0:
	ref_value=frequency_list[ref_po]
else:
	ref_value=0
print("myfrequency: "+ str(ref_value))
count1=0
for i in range(0,len(key_list)):
	if ref_value<frequency_list[i]:
		print("Cheater alert! "+ str(key_list[i]) + " " + str(frequency_list[i]))
		count1=count1+1
	else:
		if i==len(key_list)-1:
			if count1==0:
				print("It's all good yo!")


















