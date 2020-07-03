from math import *
import numpy as np
import matplotlib.pyplot as plt

# The 1976 standard atmosphere report was used as a reference for these calculations:
#https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19770009539.pdf

ADIABATIC_INDEX = 1.4;
T0 = 288.15 # surface temperature in K
S = 110.4 # Sutherland constant
u0 = 1.7894e-5 # surface viscosity
g0 = 9.80665 # accel due to gravity at SL
r0 = 6.356766e3 # radius of earth in km
P0 = 1.013250e5 # SL pressure in Pa
R = 8.31432 # gas constant
M0 = 28.97 # molar mass of air
H = np.array([0,11,20,32,47,51,71,86])  # precomputed table of altitude layers
L = np.array([-6.5,0,1,2.8,0,-2.8,-2])  # precomputed layer lapse rates
P = np.array([101325,22632.1,5474.89,868.02,110.91,66.94,3.96,0])# precomputed layer pressures
TM = np.array([288.15,216.65,216.65,228.65,270.65,270.65,214.65,182.65]) # precomputed layer temperatures

# returns the speed of sound in m/s based on the temperature in K
def speed_of_sound(T):
    return sqrt(T * ADIABATIC_INDEX * T0)
SpeedOfSound = np.vectorize(speed_of_sound)

# returns the viscosity based on kelvin temperature
def viscosity(T):
    return u0*((T/T0)**1.5)*(T0+S)/(T+S)
Viscosity = np.vectorize(viscosity)

# returns the local gravitational constant based on height above
# the earths surface Z (km)
def localGravity(Z):
    return g0*(r0/(r0+Z))**2
LocalGravity = np.vectorize(localGravity)

# returns the geopotential height layer based on altitude
def geopotentialHeightLayer(Z):
    if Z < 11:
        return 0
    elif Z < 20:
        return 1
    elif Z < 32:
        return 2
    elif Z < 47:
        return 3
    elif Z < 51:
        return 4
    elif Z < 71:
        return 5
    else:
        return 6
GeopotentialHeightLayer = np.vectorize(geopotentialHeightLayer)

# outputs the ambient temperature in K of height in km
def localTemperature(h):
    b = GeopotentialHeightLayer(h)
    T = TM[b] + L[b] * (h-H[b])
    return T
LocalTemperature = np.vectorize(localTemperature)

def localPressure(h):
    return
    #TODO: pressure equations
LocalPressure = np.vectorize(localPressure)

""" tests for visualizing graphs
x = np.linspace(0,86,1000)
y = localTemperature(x)
plt.plot(y,x)
plt.title("Temperature  @ altitude")
plt.xlabel("Temperature K")
plt.ylabel("Altitude km")
plt.savefig('altTempGraph.pdf')
plt.close()
"""


