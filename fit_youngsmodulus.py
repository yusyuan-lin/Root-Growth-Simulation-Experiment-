import numpy as np
import matplotlib.pyplot as plt
from symfit import parameters, variables, Fit, Model, sin, pi
from plotstyle import pltSty, fitRep


w = np.array([1,2,3,4,5,6,7,8])

sigma = np.array([0.07,0.098,0.07,0.0017,0.08,0.02,0.18,0.08])
h = np.array([2.86,3.12,3.53,3.4,2.8,4.08,3.11,2.84])

x, y = variables('x, y')
a, b= parameters('a,b')


model = {y : a*x+b}

fit = Fit(model, x=w, y=h)
fit_result = fit.execute()

print(fit_result)

yfit = fit.model(x=w, **fit.execute().params).y
ax = plt.subplot()





ax.plot(w, h)
ax.plot(w, yfit, label='fit',color='green')

ax.errorbar(w,h,yerr=sigma, ls='none', color='b', marker='o',label='data')
plt.ylim(1,6)

pltSty(ax, xName='times', yName = 'lamda(cm)')
plt.legend()
plt.show()
