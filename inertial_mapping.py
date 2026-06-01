import numpy as np
import time as time

# constants
Delta = 0.001
dt = 0.01
delta = dt

#Discretization of grid
L = 500
H = 250

# Stokes' constant
St = 0.1
St_inverse = 1/St
# Density ratio
R = 0


# constants on formula for DG flow
p = np.pi
A = 0.1
epsilon = 0.25
w = 0.6*p

start_time = time.time()

# function that computes velocity of flow at any point, any time
def velocity(x,y,t):
    f = epsilon*np.sin(w*t)*x*x + (1-2*epsilon*np.sin(w*t))*x
    vx = -A*p*np.sin(p*f)*np.cos(p*y)
    vy = A*p*np.cos(p*f)*np.sin(p*y)*(2*epsilon*np.sin(w*t)*x + (1-2*epsilon*np.sin(w*t)))
    return np.column_stack((vx,vy))     

    
# flow acceleration; material derivative (DU/DT = du/dt + u* del(u))
def u_acc(x,y,t):
    u_accel = (velocity(x,y,t + Delta) - velocity(x,y,t - Delta))/(2*Delta)
    v = velocity(x,y,t)
    
    dudx = (velocity(x+Delta,y,t) - velocity(x-Delta,y,t))/(2*Delta)
    dudy = (velocity(x,y+Delta,t) - velocity(x,y-Delta,t))/(2*Delta)
    

    u_accel = u_accel + dudx*np.column_stack((v[:,0],v[:,0])) + dudy*np.column_stack((v[:,1],v[:,1]))
    
    return u_accel

# particle acceleration function
def accel(x,y,v,t):
    u = velocity(x,y,t)
 
    #Stoke's drag term
    a = St_inverse*(u - v)
    
    #Added mass term
    au = 1.5*R*u_acc(x,y,t)     
    temp = a + au  
    return temp

# state transition function used in RK4 routine 
def update(state,t):
    r = state[:,2:4]
    v = accel(state[:,0],state[:,1],r,t) 
    return np.hstack((r,v))

    
def rk4(state,t):
    r = state[:,0:4]
    k1 = dt*update(r,t)
    k2 = dt*update(r+0.5*k1,t+0.5*dt)
    k3 = dt*update(r+0.5*k2,t+0.5*dt)
    k4 = dt*update(r+k3,t+dt)
    r += (k1+2*k2+2*k3+k4)/6
    
    x = state[:,0].copy()
    y = state[:,1].copy()
    
    x[x>2] = 2
    x[x<0] = 0
    y[y>1] = 1
    y[y<0] = 0
    
    r[:,0] = x
    r[:,1] = y
        
    return state


output = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/St=0.1R=0.txt','ab')

def read_mapping():
    Input = open('/Users/nishantabaral/Desktop/Geophysical Flows/Double Gyre Flow/Trace Analysis/Inital grid of particles.txt','r')
    X,Y = np.loadtxt(Input,unpack = True)
    Input.close()
    return np.column_stack((X,Y))


state = np.zeros((L*H,4))

r = read_mapping()
print(len(r))

state[:,0] = r[:,0]
state[:,1] = r[:,1]
state[:,2:4] = velocity(state[:,0],state[:,1],0)

# perform RK4 to get position of particle 15s later
for t in np.arange(0,15,dt).round(2):
    print(t)
    state = rk4(state,t)
    previous_state = state[:,0:2]

np.savetxt(output,state[:,0:2])
output.close()


print(time.time()-start_time)


