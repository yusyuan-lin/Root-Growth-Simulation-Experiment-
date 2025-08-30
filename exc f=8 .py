import math
import numpy as np
from lmfit import Model
import matplotlib.pyplot as plt
from plotstyle import pltSty, fitRep #

def function (x,a,b):
    return a*np.exp(x/b)

t = np.loadtxt(r"phi80,l=6_7.txt", skiprows=1, usecols=(0))
d = -np.loadtxt(r"phi80,l=6_7.txt", skiprows=1, usecols=(1))+35.21



Del = t - 12
    
model=Model(function)
params=model.make_params(a=1,b=1)

result=model.fit(Del,params,x=d)
for i in result.params:
    print(i,'=',result.params[i].value,'+-',result.params[i].stderr)
print('chi-square=',result.chisqr)
print('reduced-chis square=',result.redchi)

ax = plt.subplot()  #
ax.scatter(d,Del,color='red',s=3,label='data')
ax.plot(d,result.best_fit,color='black',label='fit')
plt.title('fit exp for phi=0.80, L=6cm')
pltSty(ax, xName='L(cm)', yName = 'delta(cm)') #
plt.legend()
plt.show()
