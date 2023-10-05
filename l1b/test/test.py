from common.io.writeToa import readToa
import numpy as nu
import matplotlib.pyplot as plt
from config.globalConfig import globalConfig

#Compare outputs
#1. Read LUSS
toa.luss = readToa(directory,filename)
#2.  Read your outputs
#3. Compare



myglobal = globalConfig()
bands = myglobal.bands

reference = '/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/output' #LucSotoResults
outdir = '/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/myoutputs' #My results
outdir2 = '/home/luss/my_shared_folder/lib_out_ism' #MyISMesults
outdir_eq = '/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/myoutputs_noequal' #MY results no_eq

tol = 0.01e-2
three_sigma = 1-0.997

namee = []
name2 = []
name3 = []
name4 = []

for i in range(len(bands)):
    namee.append('l1b_toa_'+'eq_'+str(bands[i])+'.nc')
    name2.append('ism_toa_'+'isrf_'+str(bands[i])+'.nc')
    name3.append('ism_toa_'+'isrf_'+str(bands[i])+'.nc')
    name4.append(('l1b_toa_'+str(bands[i])+'.nc'))

for inn in range(len(namee)):
    toa_l1b = readToa(outdir,namee[inn])
    toa_input = readToa(reference,namee[inn])
    toa_l1b_eq = readToa(outdir_eq,name4[inn])
    toa_lib_eq_input = readToa(outdir_eq,name4[inn])
    counter = 0
    counter_eq = 0
    points_treshold = toa_input.shape[0]*toa_input.shape[1]*three_sigma

    result =np.zeros((toa_l1b.shape[0],toa_l1b.shape[1]))
    result_eq =np.zeros((toa_l1b_eq.shape[0],toa_l1b_eq.shape[1]))



