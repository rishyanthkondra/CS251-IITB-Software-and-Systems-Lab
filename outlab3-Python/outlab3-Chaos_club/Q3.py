import math
class Dimension:
	x=0
	y=0
	z=0
	d=[]

	def __init__(self,a1):
		parted=a1.partition(' - ')
		part1=parted[0]
		part1_splt=part1.split(',')
		date1=parted[2]
		date_splt=date1.split('/')

		self.x=int(part1_splt[0])
		self.y=int(part1_splt[1])
		self.z=int(part1_splt[2])
		self.d=[date_splt[2],date_splt[1],date_splt[0]]
	
	def forw_possible(self,other):
		if other.d[0]>self.d[0]:
			return True
		elif other.d[0]==self.d[0]:
			if other.d[1]>self.d[1]:
				return True
			elif other.d[1]==self.d[1]:
				if other.d[2]>self.d[2]:
					return True
				else:
					return False
			else:
				return False
		else:
			return False


	def __sub__(self,other):
		if self.forw_possible(other):
			varx=self.x-other.x
			vary=self.y-other.y
			varz=self.z-other.z
			return math.sqrt((varx**2)+(vary**2)+(varz**2))
		else:
			return -1
#	def __str__(self):
	
	def __str__(self):
		#print("Coordinates:"+str())
		return "Coordinates: "+ str("({0},{1},{2})".format(self.x,self.y,self.z)) + " Time: "+ str("({0},{1},{2})".format(self.d[0],self.d[1],self.d[2]))


curr_point=Dimension(str(input()))
n=int(input())
Possible_future=[]
for i in range(0,n):
	input_point=Dimension(str(input()))
	Possible_future.append(input_point)

eucl_dist=[]
for i in range(0,n):
	print(Possible_future[i])
	vari=curr_point-Possible_future[i]
	eucl_dist.append(vari)
#print(eucl_dist)
min_posi=0
value1=-1
# for i in range(0,n):
# 	if i==0
# 		if eucl_dist[i]!=-1 and eucl_dist[i]<eucl_dist[min_posi]:
# 			min_posi=i
# 			print (min_posi)
# 		else:
# 			print(min_posi)
# 	else:
# 		if eucl_dist[i]!=-1 and eucl_dist[i]<eucl_dist[min_posi]:
# 			min_posi=i
# 			print (min_posi)
# 		else:
# 			print(min_posi)

# if eucl_dist[min_posi]==-1:
# 	print("Can't move to any point")
# else:
# 	print("Closest point is:")
# 	print(Possible_future[min_posi])
for i in range(0,n):
	if value1==-1:
		if eucl_dist[i]>0:
			value1=eucl_dist[i]
			min_posi=i
		# 	print(min_posi)
		# else:
		# 	print(min_posi)
		# if eucl_dist[i]!=-1 and eucl_dist[i]<eucl_dist[min_posi]:
		# 	min_posi=i
		# 	print (min_posi)
		# else:
		# 	print(min_posi)
	else:
		if eucl_dist[i]!=-1 and eucl_dist[i]<value1:
			min_posi=i
			value1=eucl_dist[i]
			#print (min_posi)
		
			#print(min_posi)

if value1==-1:
	print("Can't move to any point")
else:
	print("Closest point is:")
	print(Possible_future[min_posi])
	








#xexample(2,3,89 - )		