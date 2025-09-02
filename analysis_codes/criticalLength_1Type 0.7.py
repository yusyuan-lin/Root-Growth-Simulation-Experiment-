import numpy as np
import matplotlib.pyplot as plt
from symfit import parameters, variables, Fit, Model, exp
from plotstyle import pltSty, fitRep

E = 1/8.635129e-10
#E=1/1.005283e-09
#L = np.array([0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05])

phi = np.linspace(0.8,0.86,4)
h = 0.01
delta = 0.25
l = 0.41
g = 9.8
mu = 0.48
t = 0.5*(10**(-3))
phij = 0.89
sigma = np.linspace(0.25,0.25,100)
m1 = 1.65*(10**(-3))

d1 = 0.0035

N1 = (l*delta*phi)/(np.pi*(d1**2))

rho = (N1*m1)/((np.pi*(N1*(d1**2)))*0.01)

# critical length
Phi = np.linspace(0.798,0.882,100)
n1 = (l*delta*Phi)/(2*np.pi*(d1**2))

Rho = (n1*m1)/((np.pi*(n1*(d1**2)))*0.01)
crit_L = t*((4*E*(phij-Phi)/(3*mu*Phi*Rho*g*t*phij))**0.25)
#crit_L = t*((4*E/(3*mu*Phi*Rho*g*t))**0.25)


# exp result
bx = np.array([80,80,80,82,82,84,84,86,82,80,82,84,84,86,86,86,78,78])+2
by = np.array([3.5,3,8,8,3.5,3,2.5,2.5,3,4,4,3.5,4,3,3.5,4,4,3.5])

jx = np.array([80,84,82,80,82,78,78,78])+2
jy = np.array([2.5,2,2.5,2,2,2,2.5,3])

cx = np.array([86])+2
cy = np.array([2])

ax = plt.subplot()

#plt.plot(100*Phi, 100*crit_L, color='blue',linewidth=2.0)
ax.errorbar(100*Phi, 100*crit_L,yerr=sigma ,label='critical', color='#2828FF')#, marker='o',ls='none')
plt.fill_between(100*Phi, 100*crit_L,color='#FF8040',label='jiggling')
plt.fill_between(100*Phi, 100*crit_L,8.2,color='#53FF53',label='bending')

# plot exp result
plt.scatter(bx,by, color='green')
plt.scatter(jx,jy, color='#FF0000')
plt.scatter(cx,cy, color='blue')

plt.ylim(1.8,4.2)
plt.xlim(79.8,88.2)

pltSty(ax, xName='phi(%)', yName = 'L(cm)')
plt.title('1-Type L-phi r=0.35 ')
plt.legend()

#plt.savefig('Characteristic curve')
plt.show()
