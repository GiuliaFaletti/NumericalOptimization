import numpy as np
import LoadData as ld
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import quad
from RealIntegratedLuminosity import L_int_summary_18


plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica",
  "font.size": 12
})



#loading fit parameters and data
f=open('Data/a_18_2Par.txt',"r")
lines=f.readlines()
ax=[]
for x in lines:
    ax.append(float(x.split(' ')[0]))  

f.close()

#loading fit parameters and data
f=open('Data/b_18_2Par.txt',"r")
lines=f.readlines()
bx=[]
for x in lines:
    bx.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/ts_18_2Par.txt',"r")
lines=f.readlines()
ts_18=[]
for x in lines:
    ts_18.append(float(x.split(' ')[0]))  

f.close()

ts=ts_18[:6]
ts=np.array(ts)

#defining the first three fills that have occurred
a_known=ax[:3]
b_known=bx[:3]
a_known=np.array(a_known)
b_known=np.array(b_known)

#evaluating the average model parameters
mean_a_know=np.average(a_known)
mean_b_known=np.average(b_known)
std_a_known=np.std(a_known)
std_b_known=np.std(b_known)

#defining future fills model
a_future=np.random.normal(loc=mean_a_know, scale=std_a_known, size=3)
b_future=np.random.normal(loc=mean_b_known, scale=std_b_known, size=3)


a=np.append(a_known, a_future)
b=np.append(b_known, b_future)

#Initial guesses    
#x0=np.ones(6)*(15*3600)
x0=ts

#constraint determination
tot=sum(x0)

#Objective Function
def fun(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        lam=lambda x1: a[i]*np.exp(-(b[i]*x1))
        result[i]=-quad(lam, 0, t1[i])[0]
        
    result = np.sum(result)
    return result

#constraint
def cons(t1):
    res = np.sum(t1) - (tot)
    return res

#jacobian of the objective function
def jacb(t1):
    der=-a*np.exp(-(b*t1))
    #result=np.sum(der)
    return der

#bounds
list=[[1800,86400]]
for li in range(1, len(a)):
    list=list+[[1800, 86400]]
    
bnd=list

#optimization
res = minimize(fun, x0, options={'disp': True, 'maxiter':10000}, constraints={'type':'eq', 'fun': cons, 'jac': lambda x: np.ones(len(x0))}, jac=jacb, method='SLSQP', bounds=bnd) 

#Defining Integrated and total optimized Luminodity
def fun1(t1):
    result=np.empty(len(x0))
    for i in range(len(x0)):
        lam=lambda x1: a[i]*np.exp(-(b[i]*x1))
        result[i]=quad(lam, 0, t1[i])[0]
    return result

L_int_opt=fun1(res.x)
L_tot_opt=np.sum(L_int_opt)

#comparison between real and optimized times
fig, ax1= plt.subplots()
ax1.hist(x0/3600,  facecolor='steelblue', density=True, alpha=0.4, label="Real Fill Times" )
ax1.hist(res.x/3600, density=True, label="Optimized Fill Times")
ax1.set_xlabel('Times [h]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.legend(loc='best')
plt.savefig('TestingAverageModel/2018_2Par2.pdf')
plt.show()

#comparison between real and optimized integrated luminosity
fig, ax1= plt.subplots()
#ax1.hist(L_int_2018_2Par/1e9,  facecolor='steelblue', density=True, alpha=0.4, label="Real Integrated Luminosities" )
ax1.hist(L_int_opt/1e9, density=True, label="Optimized Integrated Luminosities")
ax1.set_xlabel(r'Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
#ax1.plot([],[], "k.", label="Initial L_tot={:.2f} 1/fb".format(L_tot_2018_2Par/1e9))
ax1.plot([],[], "k.", label='Optimized $L_{tot}$='+'{:.2f}'.format(L_tot_opt/1e9)+r'[$\mathrm{fb}^{-1}$]')
plt.legend(loc='best')
plt.savefig('TestingAverageModel/2018_2Par_lumi2.pdf')
plt.show()


#printing result
print("_______________Optimization Results___________________")
print(res)
print("Real Data=", x0)
print("Optimized Data=", res.x)        
 
#verifying differences between initial guesses and results
w=np.empty(len(x0))
for i in range(len(x0)):
    w[i]=res.x[i]-x0[i]

print("Differences between optimized and real data=", w) 
