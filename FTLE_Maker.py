# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from mpl_toolkits.axes_grid1 import make_axes_locatable

# fig, ax = plt.subplots(1,1,figsize=(5,5))


# # rescale ticks
# x = [0,250,497]
# y = [0,125,247]

# xlabels = ['0','1','2']
# ylabels = ['0','0.5','1']

# plt.xticks(x,xlabels)
# plt.yticks(y,ylabels)
# plt.xlabel("x")
# plt.ylabel("y")

# F = np.loadtxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_trace_tracerT=15.txt') 
# im = plt.imshow(F,origin="lower")


# ax = plt.gca()
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)
   
# plt.colorbar(im, cax=cax)
# plt.tight_layout()
# #plt.savefig('/Users/nishantabaral/Desktop/Faxen correction/Final run/FTLE_DG_WithFaxen_St=0.5R=0P=1.png',dpi=1200,bbox_inches='tight')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


F = np.loadtxt('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/FTLE_min_tracerT=7.5.txt')
vmax = np.nanmax(np.abs(F))

fig, ax = plt.subplots(1,1,figsize=(5,5))
# rescale ticks
x = [0,2500,4990]
y = [0,1250,2470]
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