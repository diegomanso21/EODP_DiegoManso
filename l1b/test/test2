from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt
from config.globalConfig import globalConfig

#Read your outputs
reference = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/output' #LucSotoResults
outdir = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/myoutputs' #My results
outdir_noeq = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/myoutputs_noeq' #MY results no_eq
outdir_ism = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/input' #MyISMesults

#Compare outputs
sigma3 = 1-0.997

myglobal = globalConfig()
bands = myglobal.bands

t_eq = []
t_isrf = []
t_isrf2 = []
t_eeq = []
for i in range(len(bands)):
    t_eq.append('l1b_toa_'+'eq_'+str(bands[i])+'.nc')
    t_isrf.append('ism_toa_'+'isrf_'+str(bands[i])+'.nc')
    t_isrf2.append('ism_toa_'+'isrf_'+str(bands[i]))
    t_eeq.append(('l1b_toa_'+str(bands[i])+'.nc'))


for j in range(len(t_eq)):
    toa_l1b = readToa(outdir,t_eeq[j])
    toa_input = readToa(reference,t_eeq[j])
    #toa_l1b_eq = readToa(outdir_noeq,t_eeq[j])
    #toa_lib_eq_input = readToa(reference,t_eq[j])

    counter = 0
    counter_eq = 0
    tolerance = toa_input.shape[0]*toa_input.shape[1]*sigma3

    result =np.zeros((toa_l1b.shape[0],toa_l1b.shape[1]))
    #result_eq =np.zeros((toa_l1b_eq.shape[0],toa_l1b_eq.shape[1]))

    for i in range(toa_l1b.shape[0]):
        for ii in range(toa_l1b.shape[1]):
            result[i, j] = toa_l1b[i, ii] - toa_input[i, ii]
            #result_eq[i, ii] - toa_l1b_eq[i, ii] - toa_lib_eq_input[i, ii]

            if np.abs(result[i, ii] > sigma3):
                counter += 1

            #if np.abs(result_eq[i, ii] > sigma3):
            #    counter_eq += 1
    print('Band ' + bands[j])
    #print('Number of values different in'+ t_eq[j]' is '+ str(counter))
    #print('Number of values different in' + t_noeq[j] ' is ' + counter_eq)
    if counter < tolerance:
        print('Test with eq ' + t_eeq[j] + ' complies the 3-sigma criteria')
    else:
        print('Test with eq ' + t_eeq[j] + ' do not complies the 3-sigma criteria')