import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import scipy.ndimage.filters as fil

def generate_sin_wave(period,range_,num):
    xlist=np.linspace(range_[0],range_[1],num,endpoint=True)
    ylist=np.sin(2*np.pi*xlist/period)
    return ylist
def noisify(array,var):
    noise=np.random.normal(0,math.sqrt(var),len(array))
    corrupt=array.copy()
    corrupt=corrupt+noise
    return corrupt
def mean_filter(array,k):
    arr=array.astype(np.float)
    p = np.zeros(k)
    arr = np.append(p,arr)
    arr = np.append(arr,p)
    cumsum = np.cumsum(np.insert(arr,0,0))
    filtered = (cumsum[(2*k+1):] - cumsum[:-(2*k+1)])/float(2*k+1)
    return filtered
