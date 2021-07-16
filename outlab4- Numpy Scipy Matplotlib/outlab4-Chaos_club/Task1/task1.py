import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.misc
def fn_plot1d(fn, x_min, x_max, filename):
    points=10**4
    xlist = np.linspace(x_min,x_max,points,endpoint=True)
    fun=np.vectorize(fn)
    ylist = fun(xlist)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    ax.plot(xlist,ylist)
    ax.set_title('graph of fn(x) in ['+str(x_min)+','+str(x_max)+']')
    fig.savefig(filename)
    plt.close(fig)
    pass

def nth_derivative_plotter(fn, n, x_min, x_max, filename):
    points=10**3
    xlist=np.linspace(x_min,x_max,points,endpoint=True)
    fund=np.vectorize(deriv)
    ylist=fund(fn,xlist,n)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    ax.plot(xlist,ylist)
    ax.set_title('graph of fn'+n*'\''+'(x) in ['+str(x_min)+','+str(x_max)+']')
    fig.savefig(filename)
    plt.close(fig)
    pass

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    points=10**3
    xlist=np.linspace(x_min,x_max,points,endpoint=True)
    ylist=np.linspace(y_min,y_max,points,endpoint=True)
    X,Y=np.meshgrid(xlist,ylist)
    fun2=np.vectorize(twodsinc)
    zlist=fun2(np.ravel(X),np.ravel(Y))
    Z=zlist.reshape(X.shape)
    fig=plt.figure()
    ax=fig.add_subplot(111, projection='3d')
    ax.plot_surface(X,Y,Z)
    #ax.set_title('graph of fn(x) in ['+str(x_min)+','+str(x_max)+'] and ['+str(y_min)+','+str(y_max)+']')
    plt.savefig(filename)
    plt.close(fig)
    pass

def deriv(fn,t,N):
    return scipy.misc.derivative(fn,t,dx=1/256,n=N,order=(2*N+1))
    pass

def b(x):
    return g(math.fabs(x))
    pass

def g(x):
    return h(2-x)/(h(2-x)+h(x-1))
    pass

def h(x):
    if x>0:
        return math.exp(-1/x**2)
    else:
        return 0
    pass

def twodsinc(x,y):
    t=math.sqrt(x**2+y**2)
    if t>0:
        return math.sin(t)/t
    else:
        return 1
    pass
fn_plot1d(b,-2,2,'fn1plot.png')
fn_plot2d(twodsinc,-1.5*math.pi,1.5*math.pi,-1.5*math.pi,1.5*math.pi,'fn2plot.png')
for i in range(11):
    if i>0:
        nth_derivative_plotter(b,i,-2,2,"bd_"+str(i)+".png")
