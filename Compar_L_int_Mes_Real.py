import numpy as np
import matplotlib.pyplot as plt
import LoadData as ld
import LuminosityOptimization as lo
from NumOpt16_2par_sec import L_int_2016_2Par
from NumOpt16_4par_sec import L_int_2016_4Par
from NumOpt16_3par_sec import L_int_2016_3Par
from  NumOpt17_2par_sec import L_int_2017_2Par
from  NumOpt17_3par_sec import L_int_2017_3Par
from  NumOpt17_4par_sec import L_int_2017_4Par
from  NumOpt18_2par_sec import L_int_2018_2Par
from NumOpt18_3par_sec import L_int_2018_3Par
from NumOpt18_4par_sec import L_int_2018_4Par
from RealIntegratedLuminosity import L_int_summary_16, L_int_summary_17, L_int_summary_18

fig, ax1= plt.subplots()
ax1.hist(L_int_2016_4Par/1e9, histtype='step', density=True, label="Real 4 par L_int" )
ax1.hist(L_int_2016_3Par/1e9,  histtype='step', density=True, label="Real 3 par L_int" )
ax1.hist(L_int_2016_2Par/1e9,  histtype='step', density=True, label="Real 2 par L_int" )
ax1.hist(L_int_summary_16/1e9, facecolor="green", alpha=0.3, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel('Integrated Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2016')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2016_tot_comp_real_meas.pdf')
plt.show()

fig, ax1= plt.subplots()
ax1.hist(L_int_2017_4Par/1e9, histtype='step', density=True, label="Real 4 par L_int" )
ax1.hist(L_int_2017_3Par/1e9,  histtype='step', density=True, label="Real 3 par L_int" )
ax1.hist(L_int_2017_2Par/1e9,  histtype='step', density=True, label="Real 2 par L_int" )
ax1.hist(L_int_summary_17/1e9, facecolor="steelblue", alpha=0.5, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel('Integrated Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2017')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2017_tot_comp_real_meas.pdf')
plt.show()

fig, ax1= plt.subplots()
ax1.hist(L_int_2018_4Par/1e9, histtype='step', density=True, label="Real 4 par L_int" )
ax1.hist(L_int_2018_3Par/1e9,  histtype='step', density=True, label="Real 3 par L_int" )
ax1.hist(L_int_2018_2Par/1e9,  histtype='step', density=True, label="Real 2 par L_int" )
ax1.hist(L_int_summary_18/1e9, facecolor="pink", alpha=0.8, density=True, label="Measured Integrated Luminosity")
ax1.set_xlabel('Integrated Luminosity [fb^-1]')
ax1.set_ylabel('Normalized Frequencies')
ax1.set_title('2018')
plt.legend(loc='upper left')
plt.savefig('OptimizationResults/2018_tot_comp_real_meas.pdf')
plt.show()