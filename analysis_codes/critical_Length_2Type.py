import numpy as np
import matplotlib.pyplot as plt
from symfit import parameters, variables, Fit, Model, exp
from plotstyle import pltSty, fitRep



E = 1/8.333038e-10

I = 1.25*(10**(-10))
L = np.array([0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05])

phi = np.linspace(0.7,0.8,6)
h = 0.01
delta = 0.25
l = 0.41
g = 9.8
mu = 0.48
t = 0.5*(10**(-3))
phij = 0.84

m1 = 1.65*(10**(-3))
m2 = 1.87*(10**(-3))
d1 = 0.0035
d2 = 0.004
N1 = (l*delta*phi)/(2*np.pi*(d1**2))
N2 = (l*delta*phi)/(2*np.pi*(d2**2))
rho = (N1*m1+N2*m2)/((np.pi*(N1*(d1**2)+N2*(d2**2)))*0.01)

sigma = np.linspace(0.25,0.25,100)

# critical length
Phi = np.linspace(0.69,0.81,100)
n1 = (l*delta*Phi)/(2*np.pi*(d1**2))
n2 = (l*delta*Phi)/(2*np.pi*(d2**2))
Rho = (n1*m1+n2*m2)/((np.pi*(n1*(d1**2)+n2*(d2**2)))*0.01)
crit_L = t*((4*E*(phij-Phi)/(3*mu*Phi*Rho*g*t*phij))**0.25)

#crit_L = t*((4*E/(3*mu*Phi*Rho*g*t))**0.25)

# exp result
bx = np.array([70,70,72,72,72,74,74,74,76,76,76,78,78,78,78,80,80,80,80,80,80,74,70,78,88,88,88,88,88,76,70,78])
by = np.array([4.5,5,4,4.5,5,4,4.5,5,4,4.5,5,3.5,4,4.5,5,3,3.5,4,4.5,5,2.75,3.75,4.25,3.5,2,2.5,3,3.5,4,3.5,4,3.25])

jx = np.array([70,70,70,70,72,72,72,72,74,74,74,76,76,76,78,78,80,78,80,76,74,72,70])
jy = np.array([2,2.5,3,3.5,2,2.5,3,3.5,2,2.5,3,2,2.5,3,2,2.5,2,3,2.5,3.25,3.5,3.75,3.75])

cx = np.array([])
cy = np.array([])

ax = plt.subplot()

ax.errorbar(100*Phi, 100*crit_L,yerr=sigma, color='#2828FF')#, marker='o', ls='none')
plt.plot(100*Phi, 100*crit_L, color='blue',linewidth=2.0,label='critical')


ax.fill_between(100*Phi, 100*crit_L,color='#FF8040',label='jiggling')
ax.fill_between(100*Phi, 100*crit_L,5.5,color='#53FF53',label='bending')

plt.scatter(bx,by, color='green')
plt.scatter(jx,jy, color='#FF0000')
plt.scatter(cx,cy, color='blue')
pltSty(ax, xName='phi(%)', yName = 'L(cm)')
plt.ylim(1.8,5.2)
plt.xlim(69,81)

plt.title('2-Type L-phi ')
plt.legend()

#plt.savefig('Characteristic curve')
plt.show()
