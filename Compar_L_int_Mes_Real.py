from typing import ChainMap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LoadData as ld
import matplotlib.colors
from RealIntegratedLuminosity import L_int_summary_16, L_int_summary_17, L_int_summary_18
import matplotlib.cm as cm

#plt.rcParams['text.usetex'] = True
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica",
  "font.size": 12
})

#loading data
data_16, data_17, data_18, array16, array17, array18 = ld.Data()
data_tot, dataTot, arrayTot = ld.TotalDataSet(data_16, data_17, data_18)
data_ta16, data_tf16, data_ta17, data_tf17, data_ta18, data_tf18 = ld.loadFill()     
FillNumber16, FillNumber17, FillNumber18 = ld.FillNumber()
data_16_sec, data_ta16_sec, data_tf16_sec, data_17_sec, data_ta17_sec,\
   data_tf17_sec, data_18_sec, data_ta18_sec, data_tf18_sec=ld.Data_sec(array16,\
      data_ta16, data_tf16, array17, data_ta17, data_tf17, array18, data_ta18, data_tf18)

f=open('Data/L_int_2016_4Par.txt',"r")
lines=f.readlines()
L_int_2016_4Par=[]
for x in lines:
    L_int_2016_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2016_3Par.txt',"r")
lines=f.readlines()
L_int_2016_3Par=[]
for x in lines:
    L_int_2016_3Par.append(float(x.split(' ')[0]))  

f.close()


f=open('Data/L_int_2016_2Par.txt',"r")
lines=f.readlines()
L_int_2016_2Par=[]
for x in lines:
  L_int_2016_2Par.append(float(x.split(' ')[0]))  

f.close()


f=open('Data/L_int_2017_4Par.txt',"r")
lines=f.readlines()
L_int_2017_4Par=[]
for x in lines:
    L_int_2017_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2017_3Par.txt',"r")
lines=f.readlines()
L_int_2017_3Par=[]
for x in lines:
    L_int_2017_3Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2017_2Par.txt',"r")
lines=f.readlines()
L_int_2017_2Par=[]
for x in lines:
    L_int_2017_2Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2018_4Par.txt',"r")
lines=f.readlines()
L_int_2018_4Par=[]
for x in lines:
    L_int_2018_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2018_3Par.txt',"r")
lines=f.readlines()
L_int_2018_3Par=[]
for x in lines:
    L_int_2018_3Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/L_int_2018_2Par.txt',"r")
lines=f.readlines()
L_int_2018_2Par=[]
for x in lines:
    L_int_2018_2Par.append(float(x.split(' ')[0]))  

f.close()

L_int_2016_4Par=np.array(L_int_2016_4Par)
L_int_2016_3Par=np.array(L_int_2016_3Par)
L_int_2016_2Par=np.array(L_int_2016_2Par)
L_int_2017_4Par=np.array(L_int_2017_4Par)
L_int_2017_3Par=np.array(L_int_2017_3Par)
L_int_2017_2Par=np.array(L_int_2017_2Par)
L_int_2018_4Par=np.array(L_int_2018_4Par)
L_int_2018_3Par=np.array(L_int_2018_3Par)
L_int_2018_2Par=np.array(L_int_2018_2Par)




fig, ax1= plt.subplots()
ax1.hist(L_int_2016_4Par/1e9, histtype='step', density=True, label=r"Real 4 par $L_\mathrm{int}$" )
ax1.hist(L_int_2016_3Par/1e9,  histtype='step', density=True, label=r"Real 3 par $L_\mathrm{int}$" )
ax1.hist(L_int_2016_2Par/1e9,  histtype='step', density=True, label=r"Real 2 par $L_\mathrm{int}$" )
ax1.hist(L_int_summary_16/1e9, facecolor="green", alpha=0.3, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel(r'Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2016')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2016_tot_comp_real_meas.pdf')
#plt.show()

fig, ax1= plt.subplots()
ax1.hist(L_int_2017_4Par/1e9, histtype='step', density=True, label=r"Real 4 par $L_\mathrm{int}$" )
ax1.hist(L_int_2017_3Par/1e9,  histtype='step', density=True, label=r"Real 3 par $L_\mathrm{int}$" )
ax1.hist(L_int_2017_2Par/1e9,  histtype='step', density=True, label=r"Real 2 par $L_\mathrm{int}$" )
ax1.hist(L_int_summary_17/1e9, facecolor="steelblue", alpha=0.5, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel(r'Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2017_tot_comp_real_meas.pdf')
#plt.show()

fig, ax1= plt.subplots()
ax1.hist(L_int_2018_4Par/1e9, histtype='step', density=True, label=r"Real 4 par $L_\mathrm{int}$" )
ax1.hist(L_int_2018_3Par/1e9,  histtype='step', density=True, label=r"Real 3 par $L_\mathrm{int}$")
ax1.hist(L_int_2018_2Par/1e9,  histtype='step', density=True, label=r"Real 2 par $L_\mathrm{int}$" )
ax1.hist(L_int_summary_18/1e9, facecolor="pink", alpha=0.8, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel(r'Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2018_tot_comp_real_meas.pdf')
#plt.show()

colors = cm.rainbow(np.linspace(0, 1, len(L_int_summary_16)))
cmap = plt.cm.rainbow 
norm = matplotlib.colors.Normalize(vmin=FillNumber16[0], vmax=FillNumber16[len(FillNumber16)-1])
fig, ax1= plt.subplots()
xb=[0.1,0.72]
yb=[0.1,0.72]
ax1.plot(xb,yb, color="gray", linestyle="dashed", linewidth=1, alpha=0.4)
for x1, y1, c in zip(L_int_summary_16, L_int_2016_4Par, colors):
    ax1.scatter(x1/1e9, y1/1e9, color=c, marker="+")
for x2, y2, c in zip(L_int_summary_16, L_int_2016_3Par, colors):
    ax1.scatter(x2/1e9, y2/1e9, color=c, marker="x")
for x3, y3, c in zip(L_int_summary_16, L_int_2016_2Par, colors):
    ax1.scatter(x3/1e9, y3/1e9, color=c, marker=".")   
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm, extend='both', label='Fill Number')
ax1.set_ylabel(r'Evaluated Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_xlabel(r'Measured Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.plot([],[], "k+", label="4 Parameters Model")  
ax1.plot([],[], "kx", label="3 Parameters Model")  
ax1.plot([],[], "k.", label="2 Parameters Model")  
ax1.set_title('2016')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2016_tot_comp_real_meas2.pdf')

colors = cm.rainbow(np.linspace(0, 1, len(L_int_summary_17)))
cmap = plt.cm.rainbow 
norm = matplotlib.colors.Normalize(vmin=FillNumber17[0], vmax=FillNumber17[len(FillNumber17)-1])
fig, ax1= plt.subplots()
xb=[0,0.78]
yb=[0,0.78]
ax1.plot(xb,yb, color="gray", linestyle="dashed", linewidth=1, alpha=0.4)
for x1, y1, c in zip(L_int_summary_17, L_int_2017_4Par, colors):
    ax1.scatter(x1/1e9, y1/1e9, color=c, marker="+")
for x2, y2, c in zip(L_int_summary_17, L_int_2017_3Par, colors):
    ax1.scatter(x2/1e9, y2/1e9, color=c, marker="x")
for x3, y3, c in zip(L_int_summary_17, L_int_2017_2Par, colors):
    ax1.scatter(x3/1e9, y3/1e9, color=c, marker=".") 
ax1.plot([],[], "k+", label="4 Parameters Model")  
ax1.plot([],[], "kx", label="3 Parameters Model")  
ax1.plot([],[], "k.", label="2 Parameters Model")  
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm, extend='both', label='Fill Number')
ax1.set_ylabel(r'Evaluated Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_xlabel(r'Measured Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_title('2017')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2017_tot_comp_real_meas2.pdf')

colors = cm.rainbow(np.linspace(0, 1, len(L_int_summary_18)))
cmap = plt.cm.rainbow 
norm = matplotlib.colors.Normalize(vmin=FillNumber18[0], vmax=FillNumber18[len(FillNumber18)-1])
fig, ax1= plt.subplots()
xb=[0.06,0.72]
yb=[0.06,0.72]
ax1.plot(xb,yb, color="gray", linestyle="dashed", linewidth=1, alpha=0.4)
for x1, y1, c in zip(L_int_summary_18, L_int_2018_4Par, colors):
    ax1.scatter(x1/1e9, y1/1e9, color=c, marker="+")
for x2, y2, c in zip(L_int_summary_18, L_int_2018_3Par, colors):
    ax1.scatter(x2/1e9, y2/1e9, color=c, marker="x")
for x3, y3, c in zip(L_int_summary_18, L_int_2018_2Par, colors):
    ax1.scatter(x3/1e9, y3/1e9, color=c, marker=".")  
ax1.plot([],[], "k+", label="4 Parameters Model")  
ax1.plot([],[], "kx", label="3 Parameters Model")  
ax1.plot([],[], "k.", label="2 Parameters Model")   
sm=plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm, extend='both', label='Fill Number')
ax1.set_ylabel(r'Evaluated Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_xlabel(r'Measured Integrated Luminosity [$\mathrm{fb}^{-1}$]')
ax1.set_title('2018')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2018_tot_comp_real_meas2.pdf')
plt.show()