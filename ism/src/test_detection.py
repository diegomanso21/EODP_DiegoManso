from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt
from config.globalConfig import globalConfig

reference = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/output' #OutputResults
outdir = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/myoutputs4' #My results

myglobal = globalConfig()
bands = myglobal.bands

tolerance = 0.01e-2
sigma3 = 1-0.997


toa_e = []
toa_detection = []
toa_ds = []
toa_prnu = []
toa_ism_name =[]

for i in range(len(bands)):
    toa_e.append('ism_toa_'+'e_'+str(bands[i])+'.nc')
    toa_detection.append('ism_toa_'+'detection_'+str(bands[i])+'.nc')
    toa_ds.append('ism_toa_'+'ds_'+str(bands[i])+'.nc')
    toa_prnu.append(('ism_toa_'+'prnu_'+str(bands[i])+'.nc'))
    toa_ism_name.append(('ism_toa_'+str(bands[i])+'.nc'))

for inn in range(len(toa_e)):

    toa_ism_ds = readToa(outdir,toa_ds[inn])
    toa_ism_detection= readToa(outdir,toa_detection[inn])
    toa_ism_e = readToa(outdir,toa_e[inn])
    toa_ism_prnu = readToa(outdir,toa_prnu[inn])
    toa_ism = readToa(outdir,toa_ism_name[inn])

    toa_ism_e_input = readToa(reference,toa_e[inn])
    toa_ism_ds_input = readToa(reference,toa_ds[inn])
    toa_ism_detection_input= readToa(reference,toa_detection[inn])
    toa_ism_prnu_input = readToa(reference,toa_prnu[inn])
    toa_ism_input = readToa(reference,toa_ism_name[inn])

    result_e =np.zeros((toa_ism_e.shape[0],toa_ism_e.shape[1]))
    result_ds =np.zeros((toa_ism_ds.shape[0],toa_ism_ds.shape[1]))
    results_detection = np.zeros((toa_ism_detection.shape[0],toa_ism_detection.shape[1]))
    results_prnu= np.zeros((toa_ism_prnu.shape[0],toa_ism_prnu.shape[1]))
    results_toa = np.zeros((toa_ism.shape[0], toa_ism.shape[1]))


    counter_e = 0
    counter_ds = 0
    counter_detection = 0
    counter_prnu = 0
    counter_toa = 0


    for i in range(toa_ism_e.shape[0]):
        for j in range(toa_ism_e.shape[1]):

            result_e[i,j]=toa_ism_e[i,j]-toa_ism_e_input[i,j]
            result_ds[i,j]=toa_ism_ds[i,j]-toa_ism_ds_input[i,j]
            results_detection[i,j]=toa_ism_detection[i,j]-toa_ism_detection_input[i,j]
            results_prnu[i,j]=toa_ism_prnu[i,j]-toa_ism_prnu_input[i,j]
            results_toa[i,j] = toa_ism[i,j]-toa_ism_input[i,j]

            if np.abs(result_e[i,j]>tolerance):
                counter_e += 1
            if np.abs(result_ds[i,j]>tolerance):
                counter_ds+= 1
            if np.abs(results_detection[i,j]>tolerance):
                counter_detection += 1
            if np.abs(results_prnu[i,j]>tolerance):
                counter_prnu += 1
            if np.abs(results_prnu[i, j] > tolerance):
                counter_toa += 1

    points_treshold = toa_ism.shape[0]*toa_ism.shape[1]*sigma3
    print('Band ' + bands[inn])
    if counter_e < points_treshold:
        print('Test ' + toa_e[inn] + ' complies the 3-sigma criteria')
    else:
        print('Test ' + toa_e[inn] + ' NO complies the 3-sigma criteria')

    if counter_ds < points_treshold:
        print('Test ' + toa_ds[inn] + '  complies the 3-sigma criteria')
    else:
        print('Test ' + toa_ds[inn] + ' NO complies the 3-sigma criteria')

    if counter_detection < points_treshold:
        print('Test ' + toa_detection[inn] + ' complies the 3-sigma criteria')
    else:
        print('Test ' + toa_detection[inn] + ' NO complies the 3-sigma criteria')

    if counter_prnu < points_treshold:
        print('Test ' + toa_prnu[inn] + ' complies the 3-sigma criteria')
    else:
        print('Test ' + toa_prnu[inn] + ' N£O complies the 3-sigma criteria')
    if counter_toa < points_treshold:
        print('Test ' + toa_ism_name[inn] + ' complies the 3-sigma criteria')
    else:
        print('Test ' + toa_ism_name[inn] + ' NO complies the 3-sigma criteria')
    print('---------------------')
