from common.io.writeToa import readToa
import numpy as np

from config.globalConfig import globalConfig
myglobal = globalConfig()
bands = myglobal.bands


reference = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-L1C/output'
outdir = r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-L1C/L1C_test'
tolerance = 0.01e-2
sigma_3 = 1-0.997

toa = []
for i in range(len(bands)):
    toa.append('l1c_toa_'+str(bands[i])+'.nc')

for j in range(len(bands)):
    toa_l1c = readToa(outdir,toa[j])
    toa_l1c_input = readToa(reference,toa[j])
    toa_l1c_sort = np.sort(toa_l1c)
    toa_l1c_input_sort = np.sort(toa_l1c_input)
    result =np.zeros(toa_l1c.shape[0])
    counter = 0
    for i in range(toa_l1c.shape[0]):
            result[i] = toa_l1c_sort[i]-toa_l1c_input_sort[i]

            if np.abs(result[i]>tolerance):
                counter += 1

    points_treshold = toa_l1c.shape[0]*sigma_3

    print('---------------------')
    if counter < points_treshold:
        print('Test ' + toa[j] + ' complies the 3-sigma criteria')
    else:
        print('Test ' + toa[j] + ' NO complies the 3-sigma criteria')

    lat_l1c = readToa(outdir,toa[j])

    #plotL1cToa(lat_l1c, lon_l1c, toa_l1c, band)

    def plotL1cToa(self, lat_l1c, lon_l1c, toa_l1c, band):
        jet = cm.get_cmap('jet', len(lat_l1c))
        toa_l1c[np.argwhere(toa_l1c < 0)] = 0
        max_toa = np.max(toa_l1c)
        # Plot stuff
        fig = plt.figure(figsize=(20, 10))
        clr = np.zeros(len(lat_l1c))
        for ii in range(len(lat_l1c)):
            clr = jet(toa_l1c[ii] / max_toa)
            plt.plot(lon_l1c[ii], lat_l1c[ii], '.', color=clr, markersize=10)
        plt.title('Projection on ground', fontsize=20)
        plt.xlabel('Longitude [deg]', fontsize=16)
        plt.ylabel('Latitude [deg]', fontsize=16)
        plt.grid()
        plt.axis('equal')
        plt.savefig(self.outdir + 'toa_' + band + '.png')
        plt.close(fig)