import numpy as np
import LoadData as ld
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import quad
from RealIntegratedLuminosity import L_int_summary_18

#loading fit parameters and data
f=open('Data/a_18_2Par.txt',"r")
lines=f.readlines()
a_18x=[]
for x in lines:
    a_18x.append(float(x.split(' ')[0]))  

f.close()

#loading fit parameters and data
f=open('Data/b_18_2Par.txt',"r")
lines=f.readlines()
b_18x=[]
for x in lines:
    b_18x.append(float(x.split(' ')[0]))  

f.close()

a_18x=np.array(a_18x)
b_18x=np.array(b_18x)

mean_a=np.average(a_18x)
mean_b=np.average(b_18x)
std_a=np.std(a_18x)
std_b=np.std(b_18x)

a=np.random.normal(loc=mean_a, scale=std_a, size=len(a_18x))
b=np.random.normal(loc=mean_b, scale=std_b, size=len(b_18x))
print(mean_a, std_a)
print(np.average(a))
print(np.std(a))

a_18=a
b_18=b

#loading data
data_16, data_17, data_18, array16, array17, array18 = ld.Data()
data_tot, dataTot, arrayTot = ld.TotalDataSet(data_16, data_17, data_18)
data_ta16, data_tf16, data_ta17, data_tf17, data_ta18, data_tf18 = ld.loadFill()     
FillNumber16, FillNumber17, FillNumber18 = ld.FillNumber()
data_16_sec, data_ta16_sec, data_tf16_sec, data_17_sec, data_ta17_sec,\
   data_tf17_sec, data_18_sec, data_ta18_sec, data_tf18_sec=ld.Data_sec(array16,\
      data_ta16, data_tf16, array17, data_ta17, data_tf17, array18, data_ta18, data_tf18)

f=open('Data/ts_18_2Par.txt',"r")
lines=f.readlines()
ts_18=[]
for x in lines:
    ts_18.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2018_2Par.txt',"r")
lines=f.readlines()
L_int_2018=[]
for x in lines:
    L_int_2018.append(float(x.split(' ')[0]))  

f.close()



#model parameters and initial guesses
ts_18=np.array(ts_18)

#Total and integrated luminosity initial values
L_int_2018_2Par=np.array(L_int_2018)
L_tot_2018_2Par=np.sum(L_int_2018_2Par)


#Objective Function
def fun(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        lam=lambda x1: a_18[i]*np.exp(-(b_18[i]*x1))
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
def jacb(t1):
    der=-a*np.exp(-(b*t1))
    #result=np.sum(der)
    return der
        
    
#Initial guesses    
x0=ts_18

#constraint determination
tot=sum(x0)

#bounds
list=[[1800,86400]]
for li in range(1, len(a_18)):
    list=list+[[1800, 86400]]
    
bnd=list

#optimization
res = minimize(fun, x0, options={'disp': True, 'maxiter':10000}, constraints={'type':'eq', 'fun': cons, 'jac': lambda x: np.ones(len(x0))}, jac=jacb, method='SLSQP', bounds=bnd) 

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
        lam=lambda x1: a_18[i]*np.exp(-(b_18[i]*x1))
        result[i]=quad(lam, 0, t1[i])[0]
    return result

L_int_opt=fun1(res.x)
L_tot_opt=np.sum(L_int_opt)

#comparison between real and optimized total
print("Initial Total Luminosity=", L_tot_2018_2Par, "ub^-1")
print("Optimized Total Luminosity=", L_tot_opt, "ub^-1")


#comparison between real and optimized times
fig, ax1= plt.subplots()
ax1.hist(x0/3600,  facecolor='steelblue', density=True, alpha=0.4, label="Real Fill Times" )
ax1.hist(res.x/3600,  color='red', histtype='step', density=True, label="Optimized Fill Times")
ax1.set_xlabel('Times [h]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.legend(loc='best')
plt.savefig('TestingAverageModel/2018_2Par.pdf')
plt.show()

#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
ax1.hist(L_int_2018_2Par/1e9,  facecolor='steelblue', density=True, alpha=0.4, label="Real Integrated Luminosities" )
ax1.hist(L_int_opt/1e9,  color='red', histtype='step', density=True, label="Optimized Integrated Luminosities")
ax1.set_xlabel('Integrated Luminosity [1/fb]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
ax1.plot([],[], "k.", label="Initial L_tot={:.2f} 1/fb".format(L_tot_2018_2Par/1e9))
ax1.plot([],[], "k.", label="Optimized L_tot={:.2f} 1/fb".format(L_tot_opt/1e9))
plt.legend(loc='best')
plt.savefig('TestingAverageModel/2018_2Par_lumi.pdf')
plt.show()


def fun2(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        result[i]=a_18[i]*np.exp(-(b_18[i]*t1[i]))
    return result

#Istantaneous ending luminosities for optimized times
fig, ax1= plt.subplots()
L_ist=fun2(res.x)
ax1.hist(L_ist, facecolor='steelblue', density=True)
ax1.set_xlabel('Istantaneous Luminosities [Hz/ub]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.savefig('TestingAverageModel/2018_2Par_istLumi.pdf')
plt.show()

#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
ax1.hist(L_int_2018_2Par/1e9,  facecolor='steelblue', density=True, alpha=0.5, label="Real Integrated Luminosities" )
ax1.hist(L_int_summary_18/1e9, histtype='step', density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel('Integrated Luminosity [1/fb]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.legend(loc='upper left')
plt.savefig('TestingAverageModel/2018_2Par_Real_Measured_Lumi.pdf')
plt.show()