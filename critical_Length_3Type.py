import numpy as np
import matplotlib.pyplot as plt
from symfit import parameters, variables, Fit, Model, exp
from plotstyle import pltSty, fitRep


#E = 1.0553*(10**6)
E = 1/8.333038e-10

I = 1.25*(10**(-10))
L = np.array([0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055,0.06])

phi = np.linspace(0.72,0.8,5)
h = 0.01
delta = 0.25
l = 0.41
g = 9.8
mu = 0.48
t = 0.5*(10**(-3))
phij = 0.81
sigma = np.linspace(0.6235,0.6235,20)
m1 = 1.65*(10**(-3))
m2 = 1.87*(10**(-3))
m3 = 1.33*(10**(-3))
d1 = 0.0035
d2 = 0.004
d3 = 0.003
N1 = (l*delta*phi)/(3*np.pi*(d1**2))
N2 = (l*delta*phi)/(3*np.pi*(d2**2))
N3 = (l*delta*phi)/(3*np.pi*(d3**2))

rho = (N1*m1+N2*m2+N3*m3)/((np.pi*(N1*(d1**2)+N2*(d2**2)+N3*(d3**2)))*0.01)
sigma = np.linspace(0.25,0.25,100)


# critical length
Phi = np.linspace(0.69,0.81,100)
n1 = (l*delta*Phi)/(3*np.pi*(d1**2))
n2 = (l*delta*Phi)/(3*np.pi*(d2**2))
n3 = (l*delta*Phi)/(3*np.pi*(d3**2))
Rho = (n1*m1+n2*m2+n3*m3)/((np.pi*(n1*(d1**2)+n2*(d2**2)+n3*(d3**2)))*0.01)
crit_L = t*((4*E*(phij-Phi)/(3*mu*Phi*Rho*g*t*phij))**0.25)

#crit_L = t*((4*E/(3*mu*Phi*Rho*g*t))**0.25)

# exp result
bx = np.array([70,70,72,72,74,74,76,78,80,70,72,72,74,74,76,76,76,76,78,78,78,78,78,80,80,80,80,80,80])
by = np.array([4.5,4,3.5,4,4,3.5,3,2.5,2,5,5,4.5,5,4.5,5,4.5,4,3.5,5,4.5,4,3.5,3,5,4.5,4,3.5,3,2.5])

jx = np.array([70,70,72,74,74,76,78,70,70,72,72,74,76])
jy = np.array([3.5,3,3,3,2.5,2.5,2,2.5,2,2.5,2,2,2])

cx = np.array([])
cy = np.array([])

ax = plt.subplot()

ax.errorbar(100*Phi, 100*crit_L,yerr=sigma, color='#2828FF')#, ls='none', marker='o')
plt.plot(100*Phi, 100*crit_L, color='blue',linewidth=2.0,label='critical')

ax.fill_between(100*Phi, 100*crit_L,color='#FF8040',label='jiggling')
ax.fill_between(100*Phi, 100*crit_L,5.2,color='#53FF53',label='bending')

ax.scatter(bx,by, color='green')
ax.scatter(jx,jy, color='#FF0000')
ax.scatter(cx,cy, color='blue')

plt.ylim(1.8,5.2)
plt.xlim(69,81)
pltSty(ax, xName='phi(%)', yName = 'L(cm)')

plt.title('3-Type L-phi ')
plt.legend()

#plt.savefig('Characteristic curve')
plt.show()
