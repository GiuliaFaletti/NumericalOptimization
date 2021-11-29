import numpy as np
import matplotlib.pyplot as plt
import LoadData as ld
#import matplotlib.cm as cm


plt.rcParams.update({
  "text.usetex": True,
  "font.family": "Helvetica",
  "font.size": 12
})

f=open('Data/ts_16_4Par.txt',"r")
lines=f.readlines()
ts_16_4Par=[]
for x in lines:
    ts_16_4Par.append(float(x.split(' ')[0]))  

f.close()


f=open('Data/res_2016_4Par.txt',"r")
lines=f.readlines()
res_2016_4Par=[]
for x in lines:
    res_2016_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2016_4Par_1Fill.txt',"r")
lines=f.readlines()
res_2016_4Par_1Fill=[]
for x in lines:
    res_2016_4Par_1Fill.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2016_4Par_2Fill.txt',"r")
lines=f.readlines()
res_2016_4Par_2Fill=[]
for x in lines:
   res_2016_4Par_2Fill.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2016_4Par_3Fill.txt',"r")
lines=f.readlines()
res_2016_4Par_3Fill=[]
for x in lines:
   res_2016_4Par_3Fill.append(float(x.split(' ')[0]))  

f.close()

ts_16_4Par=np.array(ts_16_4Par)
res_2016_4Par=np.array(res_2016_4Par)
res_2016_4Par_1Fill=np.array(res_2016_4Par_1Fill)
res_2016_4Par_2Fill=np.array(res_2016_4Par_2Fill)
res_2016_4Par_3Fill=np.array(res_2016_4Par_3Fill)

fig, ax=plt.subplots()
ax.hist(ts_16_4Par/3600, color='olivedrab', density=True, alpha=0.3, label=r"Real Times")
ax.hist(res_2016_4Par/3600, color='green', density=True, alpha=0.3, label=r"Optimized Times")
ax.hist(res_2016_4Par_1Fill/3600, density=True, color='deepskyblue', alpha=0.7, histtype='step', label=r"One Fill Deleted", linewidth=1.75)
ax.hist(res_2016_4Par_2Fill/3600, density=True, histtype='step', color='midnightblue', label=r"Two Fills Deleted", linewidth=1.25)
ax.hist(res_2016_4Par_3Fill/3600, density=True, histtype='step', color='red', label=r"Three Fills Deleted", linewidth=0.75)
ax.set_xlabel(r"Time [h]")
ax.set_ylabel("Normalized Frequencies")
ax.set_title('2016')
plt.legend(loc='best')
plt.savefig('Opt_Times_Distrib_2016.pdf')
plt.show()



f=open('Data/ts_17_4Par.txt',"r")
lines=f.readlines()
ts_17_4Par=[]
for x in lines:
    ts_17_4Par.append(float(x.split(' ')[0]))  

f.close()


f=open('Data/res_2017_4Par.txt',"r")
lines=f.readlines()
res_2017_4Par=[]
for x in lines:
    res_2017_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2017_4Par_1Fill.txt',"r")
lines=f.readlines()
res_2017_4Par_1Fill=[]
for x in lines:
    res_2017_4Par_1Fill.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2017_4Par_2Fill.txt',"r")
lines=f.readlines()
res_2017_4Par_2Fill=[]
for x in lines:
   res_2017_4Par_2Fill.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2017_4Par_3Fill.txt',"r")
lines=f.readlines()
res_2017_4Par_3Fill=[]
for x in lines:
   res_2017_4Par_3Fill.append(float(x.split(' ')[0]))  

f.close()

ts_17_4Par=np.array(ts_17_4Par)
res_2017_4Par=np.array(res_2017_4Par)
res_2017_4Par_1Fill=np.array(res_2017_4Par_1Fill)
res_2017_4Par_2Fill=np.array(res_2017_4Par_2Fill)
res_2017_4Par_3Fill=np.array(res_2017_4Par_3Fill)

fig, ax=plt.subplots()
ax.hist(ts_17_4Par/3600, color='mediumblue', density=True, alpha=0.2, label=r"Real Times")
ax.hist(res_2017_4Par/3600, color='steelblue', density=True, alpha=0.5, label=r"Optimized Times")
ax.hist(res_2017_4Par_1Fill/3600, density=True, color='deepskyblue', histtype='step', label=r"One Fill Deleted", linewidth=1.75)
ax.hist(res_2017_4Par_2Fill/3600, density=True, histtype='step', color='midnightblue', label=r"Two Fills Deleted", linewidth=1.25)
ax.hist(res_2017_4Par_3Fill/3600, density=True, histtype='step', color='red', label=r"Three Fills Deleted", linewidth=0.75)
ax.set_xlabel(r"Time [h]")
ax.set_ylabel("Normalized Frequencies")
ax.set_title('2017')
plt.legend(loc='best')
plt.savefig('Opt_Times_Distrib_2017.pdf')
plt.show()




f=open('Data/ts_18_4Par.txt',"r")
lines=f.readlines()
ts_18_4Par=[]
for x in lines:
    ts_18_4Par.append(float(x.split(' ')[0]))  

f.close()


f=open('Data/res_2018_4Par.txt',"r")
lines=f.readlines()
res_2018_4Par=[]
for x in lines:
    res_2018_4Par.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2018_4Par_1Fill.txt',"r")
lines=f.readlines()
res_2018_4Par_1Fill=[]
for x in lines:
    res_2018_4Par_1Fill.append(float(x.split(' ')[0]))  

f.close()

f=open('Data/res_2018_4Par_2Fill.txt',"r")
lines=f.readlines()
res_2018_4Par_2Fill=[]
for x in lines:
   res_2018_4Par_2Fill.append(float(x.split(' ')[0]))  

f.close()
f=open('Data/res_2018_4Par_3Fill.txt',"r")
lines=f.readlines()
res_2018_4Par_3Fill=[]
for x in lines:
   res_2018_4Par_3Fill.append(float(x.split(' ')[0]))  

f.close()

ts_18_4Par=np.array(ts_18_4Par)
res_2018_4Par=np.array(res_2018_4Par)
res_2018_4Par_1Fill=np.array(res_2018_4Par_1Fill)
res_2018_4Par_2Fill=np.array(res_2018_4Par_2Fill)
res_2018_4Par_3Fill=np.array(res_2018_4Par_3Fill)

fig, ax=plt.subplots()
ax.hist(ts_18_4Par/3600, color='indianred', density=True, alpha=0.5, label=r"Real Times")
ax.hist(res_2018_4Par/3600, color='pink', alpha=0.85, density=True, label=r"Optimized Times")
ax.hist(res_2018_4Par_1Fill/3600, density=True, color='deepskyblue', histtype='step', label=r"One Fill Deleted", linewidth=1.75)
ax.hist(res_2018_4Par_2Fill/3600, density=True, histtype='step', color='midnightblue', label=r"Two Fills Deleted", linewidth=1.25)
ax.hist(res_2018_4Par_3Fill/3600, density=True, histtype='step', color='red', label=r"Three Fills Deleted", linewidth=0.75)
ax.set_xlabel(r"Time [h]")
ax.set_ylabel("Normalized Frequencies")
ax.set_title('2018')
plt.legend(loc='best')
plt.savefig('Opt_Times_Distrib_2018.pdf')
plt.show()