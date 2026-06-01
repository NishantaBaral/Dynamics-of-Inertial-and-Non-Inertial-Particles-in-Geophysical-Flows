import numpy as np

output = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Inital grid of particles.txt','w')
X,Y = np.meshgrid(np.linspace(0,2,500),np.linspace(0,1,250))
positions = np.column_stack([X.ravel(),Y.ravel()])
np.savetxt(output,positions)
output.close()



