import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy.linalg as LA
import time as time

# constants
L = 5000
H = 2500
# horizontal grid difference
delta_1 = 2/(L-1)
# verticle grid difference
delta_2 = 1/(H-1)
T = 15

start_time = time.time()

# spatial Jacobian that is used to compute FTLE
def Jacobian(X,Y):
    J = np.empty([2,2],float)
    FTLE_max = np.empty([H-2,L-2],float)
    FTLE_min = np.empty([H-2,L-2],float)
    
    for i in range(0,H-2):
        for j in range(0,L-2):
            J[0][0] = (X[(1+i)*L+2+j]-X[(1+i)*L+j])/(2*delta_1)
            J[0][1] = (X[(2+i)*L+1+j]-X[i*L+1+j])/(2*delta_1)
            J[1][0] = (Y[(1+i)*L+2+j]-Y[(1+i)*L+j])/(2*delta_2)
            J[1][1] = (Y[(2+i)*L+1+j]-Y[i*L+1+j])/(2*delta_2)
			
	    # Green-Cauchy tensor
            D = np.dot(np.transpose(J),J)
	    # its largest eigenvalue
            lamda = LA.eigvals(D)
            FTLE_max[i][j] = np.log(np.sqrt(max(lamda)))
            FTLE_min[i][j] = np.log(np.sqrt(min(lamda)))
    return FTLE_max, FTLE_min


#Input = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/tracerT=7.49.npy','r')
#X,Y = np.loadtxt(Input,unpack = True)
#Input.close()

data = np.load("/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/tracerT=7.49.npy")
X, Y = data[:, 0], data[:, 1]


FTLE_max, FTLE_min = Jacobian(X,Y)

FTLE_max =  1/T*FTLE_max
FTLE_min =  1/T*FTLE_min
FTLE_tracer = FTLE_max + FTLE_min

print(np.shape(FTLE_max))

np.savetxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_max_tracerT=7.5.txt', FTLE_max)
np.savetxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_min_tracerT=7.5.txt', FTLE_min)
np.savetxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_trace_tracerT=7.5.txt', FTLE_tracer)

