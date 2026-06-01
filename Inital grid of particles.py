import numpy as np

output = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/Inital grid of particles.txt','w')
X,Y = np.meshgrid(np.linspace(0,2,5000),np.linspace(0,1,2500))
positions = np.column_stack([X.ravel(),Y.ravel()])
np.savetxt(output,positions)
output.close()



