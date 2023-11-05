from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt
from config.globalConfig import globalConfig

reference = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/output' #OutputResults
outdir = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/myoutputs' #My results

myglobal = globalConfig()
bands = myglobal.bands

tolerance = 0.01e-2
sigma3 = 1-0.997

# TEST ISM OPTICAL

toa_optical = []
toa_isrf = []
for i in range(len(bands)):
    toa_optical.append('ism_toa_'+'optical_'+str(bands[i])+'.nc')
    toa_isrf.append('ism_toa_'+'isrf_'+str(bands[i])+'.nc')

for inn in range(len(bands)):
    toa_ism = readToa(outdir,toa_optical[inn])
    toa_ism_input = readToa(reference,toa_optical[inn])
    toa_isrf_ism = readToa(outdir,toa_isrf[inn])
    toa_isrf_ism_input = readToa(reference,toa_isrf[inn])

    difference =np.zeros((toa_ism.shape[0],toa_ism.shape[1]))
    difference_isrf =np.zeros((toa_isrf_ism.shape[0],toa_isrf_ism.shape[1]))

    counter =0
    counter_isrf = 0
    for i in range(toa_ism.shape[0]):
        for j in range(toa_ism.shape[1]):
            difference[i,j]=toa_ism[i,j]-toa_ism_input[i,j]
            difference_isrf[i,j] = toa_isrf_ism[i,j]-toa_isrf_ism_input[i,j]

            if np.abs(difference[i,j]>tolerance):
                counter += 1
            if np.abs(difference[i,j]>tolerance):
                counter_isrf+= 1

    points_treshold = toa_ism.shape[0]*toa_ism.shape[1]*sigma3

    print('Band ' + bands[inn])
    if counter < points_treshold:
        print('Test ' + toa_optical[inn] + ' complies the 3-sigma criteria')
        print('Number of TOA values different with reference is ' + str(counter))
    else:
        print('Test ' + toa_optical[inn] + ' no complies the 3-sigma criteria')

    if counter_isrf < points_treshold:
        print('Test ' + toa_isrf[inn] + ' complies the 3-sigma criteria')
        print('Number of TOA values different with reference is ' + str(counter_isrf))
    else:
        print('Test ' + toa_isrf[inn] + ' no complies the 3-sigma criteria')
    print('------------------------')

    center_value = int(toa_ism.shape[0] / 2)
    fig1 = plt.figure()
    ax1 = plt.axes()
    plt.plot(toa_ism_input[center_value, :], 'b-')
    plt.plot(toa_ism[center_value, :], 'k')

    plt.title('TOA OPTICAL VNIR-'+ str(inn))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    plt.grid(True)
    ax1.legend(['Reference TOA', 'TOA Test ISM Optical Output'])
    fig1.savefig(r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/Figuras_test/Sigma3_Optical_VNIR'+str(inn)+'_graph.png')

    fig2 = plt.figure()
    ax2 = plt.axes()
    plt.plot(toa_isrf_ism_input[center_value, :], 'b-')
    plt.plot(toa_isrf_ism[center_value, :], 'k')

    plt.title('TOA ISRF VNIR-'+ str(inn))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    plt.grid(True)
    ax2.legend(['Reference TOA', 'TOA Test ISM ISRF Output'])
    fig2.savefig(r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/Figuras_test/Sigma3_ISRF_VNIR' + str(inn) + '_graph.png')