import numpy as np

# Create an array 'a0' from this list: [1, 1, 2, 3, 5, 8, 13, 21, 34]
# a0 = # insert your expression here
a0 = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34])

# print a0
print("a0 at beginning:\n{}".format(a0))

# reshape a0 to create a 3X3 matrix a1
# a1 = # insert your expression here
a1 = np.reshape(a0,(3,3))

# print a1
print("a1 at the beginning:\n{}".format(a1))

# now, change the central element of a1 to 0
# write 1 line of code below this line
a1[1][1]=0

# print a1
print("a1 after change:\n{}".format(a1))

# print a0
print("a0 after changing a1:\n{}".format(a0))
print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")

# make a copy of a1 and flatten it (call it a1cpy)
a1cpy = a1.flatten()# insert your expression here
# multiply each element of a1cpy by 0.7:
a1cpy = a1cpy * 0.7# insert your expression here

# print a1cpy:
print("a1cpy\n{}".format(a1cpy))

# print a1:
print("a1 after changing its copy:\n{}".format(a1))

# create an array 'arng0' of shape (4,5) containing numbers from 0 to 19, arranged along rows
#arng0 =  # insert your expression here
arng0 = np.arange(20).reshape(4,5)
# print arng0
print("arng0\n{}".format(arng0))

# create another array 'arng1' of shape ((4,3)) containing numbers from 4 to 15 arranged along columns:
arng1 = np.arange(4,16).reshape(3,4).transpose()# insert your expression here

# print arng1
print("arng1\n{}".format(arng1))

# multiply transpose of arng0 with arng1 to get mult0:
mult0 = np.dot(arng0.transpose(),arng1) # insert your expression here

# print mult0:
print("mult0\n{}".format(mult0))
# take max of mult0 along its rows and store it in v0:
v0 = mult0.max(1)# insert your expression here
#v0 = v0.reshape(v0.shape[0],1)
# print v0's shape:
print("shape of v0: \n{}".format(v0.shape))

# reshape v0 to make it a column vector:
v0 = v0.reshape(-1,1)
print(v0)
# insert your expression here
# subtract v0 from each column of mult0 and store it in base0:
base0 = mult0 - v0 # insert your expression here

# print base0
print("base0\n{}".format(base0))

# interchange second and third column of base0 and store it in base1:
### write your code in this block ####
base1 = base0.copy()
base1[:,[1, 2]] = base1[:,[2, 1]]
######################################

# print base1
print("base1\n{}".format(base1))
