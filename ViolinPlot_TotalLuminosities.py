import numpy as np
import matplotlib.pyplot as plt
import LoadData as ld
import LuminosityOptimization as lo
from RealIntegratedLuminosity import *
from matplotlib.ticker import MaxNLocator

#plt.rcParams['text.usetex'] = True
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica"
})



L_tot_2016_measured=np.sum(L_int_summary_16/1e9)

f=open('Data/L_tot_2016_4Par.txt',"r")
lines=f.readlines()
L_tot_2016=[]
for x in lines:
    L_tot_2016.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2016_4Par_Measured_Real_1Fill.txt',"r")
lines=f.readlines()
L_tot_1Fill_16=[]
for x in lines:
    L_tot_1Fill_16.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2016_4Par_Measured_Real_2Fills.txt',"r")
lines=f.readlines()
L_tot_2Fill_16=[]
for x in lines:
    L_tot_2Fill_16.append(float(x.split(' ')[0])/1e9)  

f.close()

f=open('Data/L_tot_2016_4Par_Measured_Real_3Fills.txt',"r")
lines=f.readlines()
L_tot_3Fill_16=[]
for x in lines:
    L_tot_3Fill_16.append(float(x.split(' ')[0])/1e9)  

f.close()

def relative(y):
    return y/L_tot_2016_measured

pos = [int(len(FillNumber16)), int(len(FillNumber16))-1, int(len(FillNumber16))-2, int(len(FillNumber16))-3]
data = [L_tot_2016, L_tot_1Fill_16, L_tot_2Fill_16, L_tot_3Fill_16]

fig, axs=plt.subplots()
ax2 = axs.twinx()
    
axs.axhline(L_tot_2016, color='gray', alpha=0.4, linestyle='dashed', linewidth=1)
violinz=axs.violinplot(data, pos, points=20, widths=0.3, showmeans=True)
# Make all the violin statistics marks red:
for partname in ('cbars','cmins','cmaxes','cmeans'):
    vp = violinz[partname]
    vp.set_edgecolor('darkolivegreen')
    vp.set_linewidth(1)

# Make the violin body blue with a red border:
for vi in violinz['bodies']:
    vi.set_facecolor('green')
    vi.set_edgecolor('darkolivegreen')
    vi.set_linewidth(0.25)
    vi.set_alpha(0.3)
axs.xaxis.set_major_locator(MaxNLocator(integer=True))
axs.axhline(L_tot_2016_measured, color='r', linestyle='dashed', linewidth=1, label="Measured 2016 Total Luminosity")
axs.legend(loc='upper right')
y1, y2 = axs.get_ylim()
ax2.set_ylim(relative(y1), relative(y2))
axs.set_xlabel('Nr. of Fills', fontsize=12)
axs.set_ylabel(r'Total Luminosity [$\mathrm{fb}^{-1}$]', fontsize=12)
ax2.set_ylabel(r'$L_\mathrm{tot}$/Measured $L_\mathrm{tot}$', fontsize=12)
plt.savefig('ViolinPlot16.pdf')
plt.show()



#2017
L_tot_2017_measured=np.sum(L_int_summary_17/1e9)

f=open('Data/L_tot_2017_4Par.txt',"r")
lines=f.readlines()
L_tot_2017=[]
for x in lines:
    L_tot_2017.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2017_4Par_Measured_Real_1Fill.txt',"r")
lines=f.readlines()
L_tot_1Fill_17=[]
for x in lines:
    L_tot_1Fill_17.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2017_4Par_Measured_Real_2Fills.txt',"r")
lines=f.readlines()
L_tot_2Fill_17=[]
for x in lines:
    L_tot_2Fill_17.append(float(x.split(' ')[0])/1e9)  

f.close()

f=open('Data/L_tot_2017_4Par_Measured_Real_3Fills.txt',"r")
lines=f.readlines()
L_tot_3Fill_17=[]
for x in lines:
    L_tot_3Fill_17.append(float(x.split(' ')[0])/1e9)  

f.close()

def relative(y):
    return y/L_tot_2017_measured

pos = [int(len(FillNumber17)), int(len(FillNumber17))-1, int(len(FillNumber17))-2, int(len(FillNumber17))-3]
data = [L_tot_2017, L_tot_1Fill_17, L_tot_2Fill_17, L_tot_3Fill_17]

fig, axs=plt.subplots()
ax2 = axs.twinx()
    
axs.axhline(L_tot_2017, color='gray', alpha=0.4, linestyle='dashed', linewidth=1)
violinz=axs.violinplot(data, pos, points=20, widths=0.3, showmeans=True)
# Make all the violin statistics marks red:
for partname in ('cbars','cmins','cmaxes','cmeans'):
    vp = violinz[partname]
    vp.set_edgecolor('mediumblue')
    vp.set_linewidth(1)

# Make the violin body blue with a red border:
for vi in violinz['bodies']:
    vi.set_facecolor('steelblue')
    vi.set_edgecolor('mediumblue')
    vi.set_linewidth(0.25)
    vi.set_alpha(0.5)
axs.xaxis.set_major_locator(MaxNLocator(integer=True))
axs.axhline(L_tot_2017_measured, color='r', linestyle='dashed', linewidth=1, label="Measured 2017 Total Luminosity")
axs.legend(loc='upper right')
y1, y2 = axs.get_ylim()
ax2.set_ylim(relative(y1), relative(y2))
axs.set_xlabel('Nr. of Fills', fontsize=12)
axs.set_ylabel(r'Total Luminosity [$\mathrm{fb}^{-1}$]', fontsize=12)
ax2.set_ylabel(r'$L_\mathrm{tot}$/Measured $L_\mathrm{tot}$', fontsize=12)
plt.savefig('ViolinPlot17.pdf')
plt.show()


#2018
L_tot_2018_measured=np.sum(L_int_summary_18/1e9)

f=open('Data/L_tot_2018_4Par.txt',"r")
lines=f.readlines()
L_tot_2018=[]
for x in lines:
    L_tot_2018.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2018_4Par_Measured_Real_1Fill.txt',"r")
lines=f.readlines()
L_tot_1Fill_18=[]
for x in lines:
    L_tot_1Fill_18.append(float(x.split(' ')[0])/1e9)  

f.close()


f=open('Data/L_tot_2018_4Par_Measured_Real_2Fills.txt',"r")
lines=f.readlines()
L_tot_2Fill_18=[]
for x in lines:
    L_tot_2Fill_18.append(float(x.split(' ')[0])/1e9)  

f.close()

f=open('Data/L_tot_2018_4Par_Measured_Real_3Fills.txt',"r")
lines=f.readlines()
L_tot_3Fill_18=[]
for x in lines:
    L_tot_3Fill_18.append(float(x.split(' ')[0])/1e9)  

f.close()

def relative(y):
    return y/L_tot_2018_measured

pos = [int(len(FillNumber18)), int(len(FillNumber18))-1, int(len(FillNumber18))-2, int(len(FillNumber18))-3]
data = [L_tot_2018, L_tot_1Fill_18, L_tot_2Fill_18, L_tot_3Fill_18]

fig, axs=plt.subplots()
ax2 = axs.twinx()
    
axs.axhline(L_tot_2018, color='gray', alpha=0.4, linestyle='dashed', linewidth=1)
violinz=axs.violinplot(data, pos, points=20, widths=0.3, showmeans=True)
# Make all the violin statistics marks red:
for partname in ('cbars','cmins','cmaxes','cmeans'):
    vp = violinz[partname]
    vp.set_edgecolor('hotpink')
    vp.set_linewidth(1)

# Make the violin body blue with a red border:
for vi in violinz['bodies']:
    vi.set_facecolor('pink')
    vi.set_edgecolor('hotpink')
    vi.set_linewidth(0.25)
    vi.set_alpha(0.8)
    
axs.xaxis.set_major_locator(MaxNLocator(integer=True))
axs.axhline(L_tot_2018_measured, color='r', linestyle='dashed', linewidth=1, label="Measured 2018 Total Luminosity")
axs.legend(loc='upper right')
y1, y2 = axs.get_ylim()
ax2.set_ylim(relative(y1), relative(y2))
axs.set_xlabel('Nr. of Fills', fontsize=12)
axs.set_ylabel(r'Total Luminosity [$\mathrm{fb}^{-1}$]', fontsize=12)
ax2.set_ylabel(r'$L_\mathrm{tot}$/Measured $L_\mathrm{tot}$', fontsize=12)
plt.savefig('ViolinPlot18.pdf')
plt.show()