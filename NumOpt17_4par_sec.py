import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize.nonlin import Jacobian
import LoadData as ld
import LuminosityOptimization as lo
import scipy.integrate as integrate
from lmfit import Model
import sympy as sp
from scipy.optimize import minimize, LinearConstraint
from scipy.integrate import quad
from DataModel import *
from RealIntegratedLuminosity import L_int_summary_17


#model parameters and initial guesses
ts_17=np.array(ts_17)
a_17=np.array(a_17)
b_17=np.array(b_17)
c_17=np.array(c_17)
d_17=np.array(d_17)
b1_17=np.array(b1_17)
d1_17=np.array(d1_17)
a1_17=np.array(a1_17)
c1_17=np.array(c1_17)

#Total and integrated luminosity initial values

L_int_2017_4Par=np.array(L_int_2017)
L_tot_2017_4Par=np.sum(L_int_2017_4Par)
#number of evaluation control
Nfeval=1


#Objective Function
def fun(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        lam=lambda x1: a_17[i]*np.exp(-(b_17[i]*x1))+c_17[i]*np.exp(-d_17[i]*x1)
        result[i]=-quad(lam, 0, t1[i])[0]
        
    result = np.sum(result)
    return result

#constraint
def cons(t1):
    res = np.sum(t1) - (tot)
    return res

#jacobian of the objective function
a=a_17
b=b_17
c=c_17
d=d_17
def jacb(t1):
    der=-a*np.exp(-(b*t1))-c*np.exp(-d*t1)
    #result=np.sum(der)
    return der
        
#callback function   
def callbackF(t1i):
    global Nfeval
    print('{}  {}  {}  {}  '.format(Nfeval, t1i[0], t1i[1], fun(t1i)))
    Nfeval=Nfeval+1
    
#Initial guesses    
x0=ts_17

#constraint determination
tot=sum(x0)

#printing prerogatives
print("###################################################################")
print("Initial function evaluation=", fun(x0))
print("initial guess=", x0)
print("Parameters values")
print("amp1=", a)
print("lambda1=", b)
print("amp2=", c)
print("lambda2=", d)

#bounds
list=[[x0[0]/2,x0[0]*2]]
for li in range(1, len(a_17)):
    list=list+[[x0[li]/2, x0[li]*2]]
    
bnd=list


#optimization
res = minimize(fun, x0, options={'disp': True, 'maxiter':10000}, constraints={'type':'eq', 'fun': cons, 'jac': lambda x: np.ones(len(x0))}, jac=jacb, method='SLSQP', bounds=bnd) #


#printing result
#print("_______________Steps of the optimization___________________")
print(res)
print("Real Data=", x0)
print("Optimized Data=", res.x)        
 
#verifying differences between initial guesses and results
w=np.empty(len(x0))
for i in range(len(x0)):
    w[i]=res.x[i]-x0[i]

print("Differences between optimized and real data=", w) 

#Defining Integrated and total optimized Luminodity
def fun1(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        lam=lambda x1: a_17[i]*np.exp(-(b_17[i]*x1))+c_17[i]*np.exp(-d_17[i]*x1)
        result[i]=quad(lam, 0, t1[i])[0]
    return result

L_int_opt=fun1(res.x)
L_tot_opt=np.sum(L_int_opt)

#comparison between real and optimized total
print("Initial Total Luminosity=", L_tot_2017_4Par, "ub^-1")
print("Optimized Total Luminosity=", L_tot_opt, "ub^-1")

#comparison between real and optimized times
fig, ax1= plt.subplots()
ax1.hist(x0/3600, facecolor='steelblue', density=True, alpha=0.4, label="Real Fill Times" )
ax1.hist(res.x/3600,  color='red', histtype='step', density=True, label="Optimized Fill Times")
ax1.set_xlabel('Times [h]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
plt.legend(loc='best')
plt.savefig('OptimizationResults/2017_4Par.pdf')
plt.show()

#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
ax1.hist(L_int_2017_4Par/1e9, facecolor='steelblue', density=True, alpha=0.4, label="Real Integrated Luminosities" )
ax1.hist(L_int_opt/1e9, color='red', histtype='step', density=True, label="Optimized Integrated Luminosities")
ax1.set_xlabel('Integrated Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
ax1.plot([],[], "k.", label="Initial L_tot={:.2f} fb^-1".format(L_tot_2017_4Par/1e9))
ax1.plot([],[], "k.", label="Optimized L_tot={:.2f} fb^-1".format(L_tot_opt/1e9))
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2017_4Par_lumi.pdf')
plt.show()

def fun2(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        result[i]=a_17[i]*np.exp(-(b_17[i]*t1[i]))+c_17[i]*np.exp(-d_17[i]*t1[i])
    return result

#Istantaneous ending luminosities for optimized times
fig, ax1= plt.subplots()
L_ist=fun2(res.x)
ax1.hist(L_ist,  facecolor='steelblue', density=True)
ax1.set_xlabel('Istantaneous Luminosities [Hz/ub]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
plt.savefig('OptimizationResults/2017_4Par_istLumi.pdf')
plt.show()


#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
ax1.hist(L_int_2017_4Par/1e9,  facecolor='steelblue', density=True, alpha=0.5, label="Real Integrated Luminosities" )
ax1.hist(L_int_summary_17/1e9, histtype='step', density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel('Integrated Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2017_4Par_Real_Measured_Lumi.pdf')
plt.show()