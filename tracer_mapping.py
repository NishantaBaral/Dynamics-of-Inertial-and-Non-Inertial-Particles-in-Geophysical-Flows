import numpy as np

# constants used for advecting the passive tracers
dt = 0.01
T = 15

# constants on formula for DG flow
p = np.pi
A = 0.1
epsilon = 0.25
w = 0.6*p
# function that computes velocity of flow at any point, any time
def velocity(x,y,t):
    f = epsilon*np.sin(w*t)*x*x + (1-2*epsilon*np.sin(w*t))*x
    vx = -A*p*np.sin(p*f)*np.cos(p*y)
    vy = A*p*np.cos(p*f)*np.sin(p*y)*(2*epsilon*np.sin(w*t)*x + (1-2*epsilon*np.sin(w*t)))
    return vx,vy     


def update(r,t):
    x = r[:,0]
    y = r[:,1]
    
    vx,vy = velocity(x,y,t)
    
    return np.column_stack((vx,vy))


#this file stores the final position of the tracers. For example, if we stared at t = 0 and are 
#advecting the particles up to t = 7.5, this will store the position of tracers at t=7.5

output = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/tracerT=15.txt','ab')

def read_mapping():
    Input = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/Inital grid of particles.txt','r')
    X,Y = np.loadtxt(Input,unpack = True)
    Input.close()
    return np.column_stack((X,Y))
        
  
r = read_mapping()
print(len(r))

    
# for t in np.arange(0,T,dt).round(2):
    
#     k1 = dt*update(r,t)
#     k2 = dt*update(r+0.5*k1,t+0.5*dt)
#     k3 = dt*update(r+0.5*k2,t+0.5*dt)
#     k4 = dt*update(r+k3,t+dt)
#     k = r + (k1+2*k2+2*k3+k4)/6

#     x = k[:,0].copy()
#     y = k[:,1].copy()
    
#     x[x>2] = 2
#     x[x<0] = 0
#     y[y>1] = 1
#     y[y<0] = 0
    
#     r[:,0] = x
#     r[:,1] = y

#     # append data to the file	
    
#     print(t)
    
          
# np.savetxt(output,k)
# output.close()
save_times = [7.49, 14.99]   # save at these times
# Track which save times have been completed
saved = {st: False for st in save_times}
base_path = '/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/'


for t in np.arange(0, T, dt).round(2):
    k1 = dt * update(r, t)
    k2 = dt * update(r + 0.5*k1, t + 0.5*dt)
    k3 = dt * update(r + 0.5*k2, t + 0.5*dt)
    k4 = dt * update(r + k3, t + dt)
    k = r + (k1 + 2*k2 + 2*k3 + k4) / 6

    x = k[:, 0].copy()
    y = k[:, 1].copy()
    x[x > 2] = 2
    x[x < 0] = 0
    y[y > 1] = 1
    y[y < 0] = 0
    r[:, 0] = x
    r[:, 1] = y

    # Compute time after this step has been applied
    t_after = round(t + dt, 2)

    # Check if any save time has been reached
    for st in save_times:
        if not saved[st] and abs(t_after - st) < 1e-6:
            fname = base_path + f'tracerT={st}.npy'
            np.save(fname, r)
            print(f"Saved t={st} to {fname}")
            saved[st] = True

    if t % 1 < dt:   # progress every ~1 time unit
        print(f"t = {t_after}")
    
    
    
        
        