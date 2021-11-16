import numpy as np
import matplotlib.pyplot as plt
import LoadData as ld
import LuminosityOptimization as lo
from scipy.optimize import minimize
from scipy.integrate import quad
from DataModel import *

#define the fill times, the turnaround times and the model parameters
ts_tot_18=np.array(ts_18)
ta=np.array(data_ta18_sec)
a_tot_18=np.array(a_18)
b_tot_18=np.array(b_18)
c_tot_18=np.array(c_18)
d_tot_18=np.array(d_18)

#Total and integrated luminosity initial values
L_int_tot_2018=np.array(L_int_2018)
L_tot_tot_2018=np.sum(L_int_tot_2018)

#define total luminosity for evaluating the distribution
L_tot_test=[]

for k in range(len(ts_tot_18)):
    
    #redefining the fill times, the turnaround times and the model parameters
    a_18=np.delete(a_tot_18, k)
    b_18=np.delete(b_tot_18, k)
    c_18=np.delete(c_tot_18, k)
    d_18=np.delete(d_tot_18, k)
    ts_18=np.delete(ts_tot_18, k)
    
    #Total and integrated luminosity
    L_int_2018=np.delete(L_int_tot_2018, k)
    L_tot_2018=np.sum(L_int_2018)
    
    #Objective Function
    def fun(t1):
        result=np.empty(len(x0))
        for i in range(len(x0)):
            lam=lambda x1: a_18[i]*np.exp(-(b_18[i]*x1))+c_18[i]*np.exp(-d_18[i]*x1)
            result[i]=-quad(lam, 0, t1[i])[0]
            
        result = np.sum(result)
        return result

    #constraint
    def cons(t1):
        res = np.sum(t1) - (tot)
        return res

    #jacobian of the objective function
    a=a_18
    b=b_18
    c=c_18
    d=d_18
    def jacb(t1):
        der=-a*np.exp(-(b*t1))-c*np.exp(-d*t1)
        #result=np.sum(der)
        return der
            
        
    #Initial guesses    
    x0=ts_18

    #constraint determination
    tot=sum(x0)+ts_tot_18[k]+ta[k]

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
    for li in range(1, len(a_18)):
        list=list+[[x0[li]/2, x0[li]*2]]
        
    bnd=list

    #optimization
    res = minimize(fun, x0, options={'disp': True, 'maxiter':10000}, constraints={'type':'eq', 'fun': cons, 'jac': lambda x: np.ones(len(x0))}, jac=jacb, method='SLSQP', bounds=bnd) #


    #printing result
    #print("_______________Steps of the optimization___________________")
    print(np.sum(res.x), np.sum(x0))
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
            lam=lambda x1: a_18[i]*np.exp(-(b_18[i]*x1))+c_18[i]*np.exp(-d_18[i]*x1)
            result[i]=quad(lam, 0, t1[i])[0]
        return result

    L_int_opt=fun1(res.x)
    L_tot_opt=np.sum(L_int_opt)

    #comparison between real and optimized total
    print("Initial Total Luminosity=", L_tot_2018, "ub^-1")
    print("Optimized Total Luminosity=", L_tot_opt, "ub^-1")

    #comparison between real and optimized times
    fig, ax1= plt.subplots()
    ax1.hist(x0/3600, facecolor='steelblue', density=True, alpha=0.4, label="Real Fill Times" )
    ax1.hist(res.x/3600, color='red', histtype='step', density=True, label="Optimized Fill Times")
    ax1.set_xlabel('Times [h]')
    ax1.set_ylabel('Normalized Frequencies')
    ax1.set_title('2018')
    plt.legend(loc='best')
    plt.savefig('Test_18_4Par/2018_4Par_{}.pdf'.format(k))


    #comparison between real and optimized integrated luminosity
    fig, ax1= plt.subplots()
    ax1.hist(L_int_2018/1e9,  facecolor='steelblue', density=True, alpha=0.4, label="Real Integrated Luminosities" )
    ax1.hist(L_int_opt/1e9, color='red', histtype='step', density=True, label="Optimized Integrated Luminosities")
    ax1.set_xlabel('Integrated Luminosity [fb^-1]')
    ax1.set_ylabel('Normalized Frequencies')
    ax1.set_title('2018')
    ax1.plot([],[], "k.", label="Initial L_tot={:.2f} fb^-1".format(L_tot_2018/1e9))
    ax1.plot([],[], "k.", label="Optimized L_tot={:.2f} fb^-1".format(L_tot_opt/1e9))
    plt.legend(loc='upper left')
    plt.savefig('Test_18_4Par/2018_4Par_lumi_{}.pdf'.format(k))

    def fun2(t1):
        result=np.empty(len(x0))
        for i in range(len(x0)):
            result[i]=a_18[i]*np.exp(-(b_18[i]*t1[i]))+c_18[i]*np.exp(-d_18[i]*t1[i])
        return result

    #Istantaneous ending luminosities for optimized times
    fig, ax1= plt.subplots()
    L_ist=fun2(res.x)
    ax1.hist(L_ist,  facecolor='steelblue', density=True)
    ax1.set_xlabel('Istantaneous Luminosities [Hz/ub]')
    ax1.set_ylabel('Normalized Frequencies')
    ax1.set_title('2018')
    plt.savefig('Test_18_4Par/2018_4Par_istLumi_{}.pdf'.format(k))
    
    L_tot_test.append(L_tot_opt)


L_tot_test=np.array(L_tot_test)
#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
ax1.hist(L_tot_test/1e9, facecolor='steelblue', density=True, alpha=0.4)
ax1.axvline(np.average(L_tot_test/1e9), color='r', linestyle='dashed', linewidth=1, label="Mean Value={:.2f} fb^-1".format(np.average(L_tot_test/1e9)))
ax1.axvline(np.average(L_tot_tot_2018/1e9), color='b', linestyle='dashed', linewidth=1, label="Real L_tot={:.2f} fb^-1".format(L_tot_tot_2018/1e9))
ax1.plot([],[], "k.", label="Sigma={:.2f} fb^-1".format(np.std(L_tot_test/1e9)))
ax1.set_xlabel('Total Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('Distribution of Total Luminosities 2018')
plt.legend(loc='best')
plt.savefig('Test_18_4Par/2018_4Par_Test.pdf')