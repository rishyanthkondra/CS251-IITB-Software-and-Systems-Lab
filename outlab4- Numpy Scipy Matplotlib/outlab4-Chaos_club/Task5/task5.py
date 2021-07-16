import pandas as pd
import argparse
import matplotlib.pyplot as plt
parser=argparse.ArgumentParser(prefix_chars='--')
parser.add_argument("--data",help="the path of data file")
args=parser.parse_args()
df=pd.read_csv(args.data)
df1=df.groupby('instance')
hori_list=df['horizon'].unique()
hori_list.sort()
g_small=df1.get_group('small_scale')
g_medium=df1.get_group('medium_scale')
g_large=df1.get_group('large_scale')
algorithm_array=['ucb','kl-ucb','round-robin','thompson-sampling','epsilon-greedy']
g_small_algori=g_small.groupby('algorithm')
g_medium_algori=g_medium.groupby('algorithm')
g_large_algori=g_large.groupby('algorithm')
g_small_algo=[0,0,0,0,0,0,0]
g_medium_algo=[0,0,0,0,0,0,0]
g_large_algo=[0,0,0,0,0,0,0]
for i in range(0,len(algorithm_array)):
    g_small_algo[i]=g_small_algori.get_group(algorithm_array[i])
    g_medium_algo[i]=g_medium_algori.get_group(algorithm_array[i])
    g_large_algo[i]=g_large_algori.get_group(algorithm_array[i])
gr_sm_eps_0_002=g_small_algo[4].groupby('epsilon').get_group(0.002)
gr_med_eps_0_002=g_medium_algo[4].groupby('epsilon').get_group(0.002)
gr_lar_eps_0_002=g_large_algo[4].groupby('epsilon').get_group(0.002)
gr_sm_eps_0_02=g_small_algo[4].groupby('epsilon').get_group(0.02)
gr_med_eps_0_02=g_medium_algo[4].groupby('epsilon').get_group(0.02)
gr_lar_eps_0_02=g_large_algo[4].groupby('epsilon').get_group(0.02)
gr_sm_eps_0_2=g_small_algo[4].groupby('epsilon').get_group(0.2)
gr_med_eps_0_2=g_medium_algo[4].groupby('epsilon').get_group(0.2)
gr_lar_eps_0_2=g_large_algo[4].groupby('epsilon').get_group(0.2)
g_small_algo[4]=gr_sm_eps_0_002
g_small_algo[5]=gr_sm_eps_0_02
g_small_algo[6]=gr_sm_eps_0_2
g_medium_algo[4]=gr_med_eps_0_002
g_medium_algo[5]=gr_med_eps_0_02
g_medium_algo[6]=gr_med_eps_0_2
g_large_algo[4]=gr_lar_eps_0_002
g_large_algo[5]=gr_lar_eps_0_02
g_large_algo[6]=gr_lar_eps_0_2
f1=[]
f2=[]
f3=[]
# g_large_algo is the list containing all rows with all particular algorithm in large_scale
for i in range(0,len(g_small_algo)):
    v1=g_small_algo[i].groupby(['instance','algorithm','horizon']).mean()['REG']
    v2=g_medium_algo[i].groupby(['instance','algorithm','horizon']).mean()['REG']
    v3=g_large_algo[i].groupby(['instance','algorithm','horizon']).mean()['REG']
    l1=[]
    l2=[]
    l3=[]
    for j in range(0,len(hori_list)):
        l1.append(v1[j])
        l2.append(v2[j])
        l3.append(v3[j])
    f1.append(l1)
    f2.append(l2)
    f3.append(l3)
list_final=[f1,f2,f3]
title_list=['Instance1-small_scale with both axes in logscale','Instance2-medium_scale with both axes in logscale','Instance3-large_scale with both axes in logscale']
for i in range(0,len(list_final)):
    fi_name='instance'+str(i+1)+'.png'
    plt.suptitle(title_list[i])
    plt.loglog(hori_list,list_final[i][0],label='ucb')
    plt.loglog(hori_list,list_final[i][1],label='kl-ucb')
    plt.loglog(hori_list,list_final[i][2],label='round-robin')
    plt.loglog(hori_list,list_final[i][3],label='thompson-sampling')
    plt.loglog(hori_list,list_final[i][4],label='epsilon-greedy with epsilon=0.002')
    plt.loglog(hori_list,list_final[i][5],label='epsilon-greedy with epsilon=0.02')
    plt.loglog(hori_list,list_final[i][6],label='epsilon-greedy with epsilon=0.2')
    plt.legend()
    plt.xlabel('Horizon')
    plt.ylabel('Regret')
    plt.savefig(fi_name)
    plt.close()
