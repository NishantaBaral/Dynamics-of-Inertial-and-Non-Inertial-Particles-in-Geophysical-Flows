import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


F = np.loadtxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_min_tracerT=7.5.txt')
vmax = np.nanmax(np.abs(F))

fig, ax = plt.subplots(1,1,figsize=(5,5))
# rescale ticks
x = [0,250,497]
y = [0,125,247]
xlabels = ['0','1','2']
ylabels = ['0','0.5','1']

plt.xticks(x,xlabels)
plt.yticks(y,ylabels)
plt.xlabel("x")
plt.ylabel("y")

im = plt.imshow(F, cmap='RdBu', origin='lower', vmin=-vmax, vmax=vmax)

ax = plt.gca()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.05)

plt.colorbar(im, cax=cax)
plt.savefig('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_DG_min_tracerT=7.5.png',bbox_inches='tight')
plt.show()
