# Write your code here!
import numpy as np
import scipy as sp
import scipy.cluster.vq as scp_clus
import argparse
import imageio
parser=argparse.ArgumentParser(prefix_chars='--')
parser.add_argument("--input")
parser.add_argument("--k",type=int)
parser.add_argument("--output")
args=parser.parse_args()
inp=args.input
k=args.k
out=args.output
ori_img=imageio.imread(inp)
ori_arr=np.array(ori_img).astype('float')
nr=np.size(ori_arr[:,:,0],0)
nc=np.size(ori_arr[:,:,0],1)
n=nr*nc
chang1=ori_arr[:,:,0].reshape(1,n).flatten('F')
chang2=ori_arr[:,:,1].reshape(1,n).flatten('F')
chang3=ori_arr[:,:,2].reshape(1,n).flatten('F')
new_array=np.zeros((n,3))
new_array[:,0]=chang1
new_array[:,1]=chang2
new_array[:,2]=chang3
Kcluster=scp_clus.kmeans2(new_array,k,minit='++')
Centroid_array=Kcluster[0]
label=Kcluster[1]
new_image=np.zeros((n,3))
for i in range(0,n):
    new_image[i]=Centroid_array[label[i]]
column_1=new_image[:,0]
column_2=new_image[:,1]
column_3=new_image[:,2]
Red=column_1.reshape(nr,nc)
Green=column_2.reshape(nr,nc)
Blue=column_3.reshape(nr,nc)
final_arr=np.zeros((nr,nc,3))
final_arr[:,:,0]=Red
final_arr[:,:,1]=Green
final_arr[:,:,2]=Blue
final_arr=final_arr.astype(np.uint8)
imageio.imwrite(out,final_arr)
