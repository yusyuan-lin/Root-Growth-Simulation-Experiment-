'''Version 1, 2020/ 11/ 04'''


from matplotlib.ticker import AutoLocator, AutoMinorLocator

#設定畫圖風格
def pltSty(ax, xName = 'x-axis', yName = 'y-axis', TitleSize = 15, LabelSize = 13):
    ax.set_xlabel(xName, fontsize = TitleSize, loc='right')
    ax.set_ylabel(yName, fontsize = TitleSize, loc='top')
    ax.xaxis.set_major_locator(AutoLocator())
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.tick_params(direction = 'in', length = 7, labelsize = LabelSize, top = True, right = True)
    ax.tick_params(direction = 'in', length = 4, which = 'minor', labelsize = LabelSize, top = True, right = True)

# 印出擬和結果
def fitRep(y, fit, Nconstraint = 0):
    dof = len(y) - (len(fit.model.params) - Nconstraint) # degree of fredom
    reduced_chi2 = fit.execute().chi_squared / dof
    res = '-------------------------- \n'
    res += '[Values of fit parameters] \n'
    for p in fit.model.params:
        value = fit.execute().value(p)
        value_str = '{:.8f}'.format(value) if value is not None else 'None'
        stdev = fit.execute().stdev(p)
        stdev_str = '{:.8f}'.format(stdev) if stdev is not None else 'None'
        res += '{:8}{:8}{} +/- {}\n'.format(p.name,'=',value_str, stdev_str, width=20)
    res += '-------------------------- \n'
    res += '[Goodness of Fit] \n'
    res += 'degree of freedom: {:d} \n'.format(dof)
    res += 'chi_squared: {:.8f} \n'.format(fit.execute().chi_squared) 
    res += 'reduced_chi_squared: {:.8f} \n'.format(reduced_chi2)
    res += '--------------------------'
    print (res)
