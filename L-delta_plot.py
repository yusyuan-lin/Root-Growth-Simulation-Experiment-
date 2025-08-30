import numpy as np
import matplotlib.pyplot as plt
from symfit import parameters, variables, Fit, Model, exp
from plotstyle import pltSty, fitRep

x =( np.loadtxt(r"84%8cm(2).txt", usecols=(0)))  
y =-(np.loadtxt(r"84%8cm(2).txt", usecols=(1) ))+34.42 # L

delta = abs(x-13.79)
#plt.scatter(frame_x, frame_y, color='b', label='pulley',s=12)
#plt.scatter(fiber_x, fiber_y, color='r', label='fiber',s=12)

ax = plt.subplot()

ax.scatter(y, delta, color='r',s=10)


pltSty(ax, xName='L(cm)', yName = 'delta(cm)')

plt.title('high packing fraction')
#plt.xlim(-1,1)
#plt.legend()

#plt.savefig('Characteristic curve')
plt.show()
