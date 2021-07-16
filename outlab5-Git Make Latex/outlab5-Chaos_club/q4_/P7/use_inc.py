from inc import ang_to_vec as a2v
import numpy as np
from inc import vec_to_ang as v2a
import sys

def main():
    if int(sys.argv[3]) == 0:
        v = np.loadtxt(sys.argv[1], delimiter=",")
        a = v2a(v)
        np.savetxt(sys.argv[2], a, delimiter=",")
    elif int(sys.argv[3]) == 1:
        a = np.loadtxt(sys.argv[1], delimiter=",")
        v = a2v(a)
        np.savetxt(sys.argv[2], v, delimiter=",")

if __name__="__main__":
    main()
