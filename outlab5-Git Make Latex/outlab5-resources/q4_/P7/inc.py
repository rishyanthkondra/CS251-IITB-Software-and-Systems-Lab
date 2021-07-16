import numpy as np


def vec_to_ang(vec):
    vec = (vec.T/np.linalg.norm(vec.T,axis=0)).T
    n = vec.shape[0]
    # ang = np.zeros((vec.shape[0],4))
    v1 = vec[:, :1]
    v2 = vec[:, 1:2]
    temp = np.arctan2(v2,v1)
    temp = np.rad2deg(temp)
    return temp.reshape(n,)


def ang_to_vec(ang):
    n = np.size(ang)
    ang = ang.reshape(n,1)
    ang_r = np.deg2rad(ang)
    temp1 = np.cos(ang_r)
    temp2 = np.sin(ang_r)
    return np.stack((temp1, temp2), axis=1).reshape(n, 2)


