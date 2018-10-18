'''
####################################################################################
%% ROCKETMAN %%

Main GNC code. For ESI use only.
# to be implemented in parts
1. As civilised people, we only use SI units.

### Description ###
Part 1: 
To be a general simulation, accounting for as many influences as possible.

Part 2: 
To include basic optimisation toward a set point

Part 3: 
To include active correction

### Changelog ###
1.0 Init. Relaxed assumptions (stationary Earth). First approximation. 2D

####################################################################################
'''
import numpy as np

#Init static variables (to be edited)
G = 6.67*10**-11 # Gravitational constant
R = 6371000 # Radius of Earth
Me = 5.972*10**24 # Mass of Earth
beta = 0 # angle of thrust
daCl = 0 # rate of change of drag coefficient wrt angle of attack
S = 113 # Surface area
t1 = 200 # Time of the first stage
M0 = 407000 # Original mass
M1 = 15500 # Mass at stage 1
ve = 2500 # exhaust velocity
eps = 1 # timestep
dM = (M1 -M0)/t1 # Mass flow rate


T = np.abs(dM)*ve
rho = 20 # air density (to be updated as a function of r)
Delta = dM*t1/M0 # to be a function of dM


# Init desired variables
r = R # magnitude of instantaneous displacement from earth
v = 0 # magnitude of instantaneous velocity 
a = 0 # magnitude of acceleration

psi = np.pi/2 # flight path heading (angle between v and local horizontal)
phi = 0 # ground track angle
alpha = 0 # angle of attack
t = 0 #time

# Init some lists
r_list = []
psi_list = []

#launch sequence

#stage 1
while t<=t1:
    # Init secondary variables
    g = G*Me/(r)**2 # gravitational force
    M = M0 + dM*t # M(t)
    L = daCl*S*rho*v**2 #Lift 
    gaxi = t/t1 # Burn stage
    chi = v/ve 
    n0 = T/(M0*g)
    
    #evolve the system
    a = -g*np.sin(psi) + T*np.cos(alpha)/M
    if a > 0:
        v += a
    psi_dot = ( (T/M)*(1 + daCl*S*rho*(v**2)*np.sin(alpha)/(2*T)) -(g-v**2/(r))*np.cos(psi))/v if v > 0 else 0
    psi += psi_dot
    
    r += v*np.sin(psi)
    phi += (v*np.cos(psi)/r)
    
    r_list.append(r-R)
    psi_list.append(psi)
    
    alpha = (((R/r)**2 * (1-v**2/(r*g)) * (1-(gaxi*Delta))*np.cos(psi)/n0 + ((chi/Delta)*(1-gaxi*Delta)*psi_dot/t1))/ (1+daCl*S*rho*v**2/(2*T)))
    
    
    
    t += eps
    
    

