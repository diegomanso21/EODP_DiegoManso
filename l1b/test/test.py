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
tolerance = 0.01e-2
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

            if np.abs(result[i, ii] > tolerance):
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

    #if counter_eq < tolerance:
    #    print('Test with no eq ' + t_eq[j] + ' complies the 3-sigma criteria')
    #else:
    #    print('Test with no eq ' + t_eq[j] + ' do not complies the 3-sigma criteria')


#3. Plot results

    #Reference toa(output) and test toa(myoutputs)
    toa_ref = readToa(reference,t_eeq[j])
    center_value_ref = int(toa_ref.shape[0]/2)

    toa_myout = readToa(outdir,t_eeq[j])
    center_value_myout = int(toa_myout.shape[0] / 2)

    toa_noeq = readToa(outdir_noeq,t_eeq[j])
    center_value_noeq = int(toa_noeq.shape[0]/2)

    toa_isrf = readToa(outdir_ism,t_isrf[j])
    center_value_isrf = int(toa_isrf.shape[0] / 2)

    fig1 = plt.figure()
    ax1 = plt.axes()

    plt.plot(toa_myout[center_value_myout, :], 'k')

    plt.plot(toa_noeq[center_value_noeq, :], 'r')

    plt.plot(toa_isrf[center_value_isrf, :], 'b')

    plt.title('TOA_l1b VNIR-'+ str(j))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    plt.grid(True)
    ax1.legend(['Equalized TOA L1b', 'No Equalized TOA L1b', 'ISRF TOA'])
    fig1.savefig(r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/Figuras/ComparisonTOA_VNIR'+str(j)+'_graph.png')
    #plt.show()

    fig2 = plt.figure()
    ax2 = plt.axes()
    plt.plot(toa_ref[center_value_ref, :], 'b-')

    plt.plot(toa_myout[center_value_myout, :], 'k')


    plt.title('TOA_l1b VNIR-'+ str(j))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    plt.grid(True)
    ax2.legend(['Reference TOA', 'TOA Test L1b Output'])
    fig2.savefig(r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/Figuras/Sigma3_VNIR'+str(j)+'_graph.png')


###############
    toa_ism = readToa(outdir_ism,t_isrf[j])
    center_value = int(toa_ism.shape[0]/2)
    fig2,ax2 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(center_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax2.plot(toa_ism[center_value,:],'k')
    #fig2.savefig(outdir+'/'+t3[inn]+'_graph.png')
    #plt.show()

    toa_1 = readToa(outdir,t_eq[j])
    center_value_1 = int(toa_1.shape[0]/2)
    fig4,ax4 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(center_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax4.plot(toa_1[center_value_1,:],'k')
    #fig4.savefig(outdir+'/'+te[inn]+'equalized'+'_graph.png')
    #plt.show()



    toa_eq = readToa(outdir_noeq,t_eeq[j])
    mid_value = int(toa_eq.shape[0]/2)
    fig3,ax3 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(mid_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax3.plot(toa_eq[mid_value,:],'k')
    #fig3.savefig(outdir_eq+'/'+t4[inn]+'_non_equalized'+'_graph.png')
    #plt.show()








