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
G = 1 # Gravitational constant
R = 1 # Radius of Earth
Me = 1 # Mass of Earth
beta = 0 # angle of thrust
daCl = 0 # rate of change of drag coefficient wrt angle of attack
S = 1 # Surface area
t1 = 200 # Time of the first stage
M0 = 20000 # Original mass
M1 = 10000 # Mass at stage 1
ve = 30 # exhaust velocity
eps = 1 # timestep
dM = (M1 -M0)/t1 # Mass flow rate


T = np.abs(dM)*ve
rho = 20 # air density (to be updated as a function of r)


# Init desired variables
r = 0 # magnitude of instantaneous displacement from ground station (GS)
v = 0 # magnitude of instantaneous velocity 
a = 0 # magnitude of acceleration

psi = np.pi/2 # flight path heading (angle between v and local horizontal)
phi = 0 # ground track angle
alpha = 0 # angle of attack
y = 0 # altitude
t = 0 #time



#launch sequence

#stage 1
while t<=t1:
    # Init secondary variables
    g = G*Me/(R+y)**2
    M = M0 + dM*t
    
    t += eps
    
print(M)
