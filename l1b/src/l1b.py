
# LEVEL-1B MODULE

from l1b.src.initL1b import initL1b
from common.io.writeToa import writeToa, readToa
from common.src.auxFunc import getIndexBand
from common.io.readFactor import readFactor, EQ_MULT, EQ_ADD, NC_EXT
import numpy as np
import os
import matplotlib.pyplot as plt

class l1b(initL1b):

    def __init__(self, auxdir, indir, outdir):
        super().__init__(auxdir, indir, outdir)

    def processModule(self):

        self.logger.info("Start of the L1B Processing Module")

        for band in self.globalConfig.bands:

            self.logger.info("Start of BAND " + band)

            # Read TOA - output of the ISM in Digital Numbers
            # -------------------------------------------------------------------------------
            toa = readToa(self.indir, self.globalConfig.ism_toa + band + '.nc')

            # Equalization (radiometric correction)
            # -------------------------------------------------------------------------------
            if self.l1bConfig.do_equalization:
                self.logger.info("EODP-ALG-L1B-1010: Radiometric Correction (equalization)")

                # Read the multiplicative and additive factors from auxiliary/equalization/
                eq_mult = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_mult+band+NC_EXT),EQ_MULT)
                eq_add = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_add+band+NC_EXT),EQ_ADD)

                # Do the equalization and save to file
                toa = self.equalization(toa, eq_add, eq_mult) #formula TOA real apuntes
                writeToa(self.outdir, self.globalConfig.l1b_toa_eq + band, toa)

            # Restitution (absolute radiometric gain)
            # -------------------------------------------------------------------------------
            self.logger.info("EODP-ALG-L1B-1020: Absolute radiometric gain application (restoration)")
            toa = self.restoration(toa, self.l1bConfig.gain[getIndexBand(band)])

            # Write output TOA
            # -------------------------------------------------------------------------------
            writeToa(self.outdir, self.globalConfig.l1b_toa + band, toa)
            self.plotL1bToa(toa, self.outdir, band)

            self.logger.info("End of BAND " + band)

        self.logger.info("End of the L1B Module!")


    def equalization(self, toa, eq_add, eq_mult):
        """
        Equlization. Apply an offset and a gain.
        :param toa: TOA in DN
        :param eq_add: Offset in DN
        :param eq_mult: Gain factor, adimensional
        :return: TOA in DN, equalized
        """
        #TODO
        toa_eq = np.zeros(toa.shape)
        for i in range(toa.shape[0]):
            toa_eq[i,:]=(toa[i,:] - eq_add)/eq_mult

        # Porque si en vez de toa_eq uso toa falla?
        return toa_eq

    def restoration(self,toa,gain):
        """
        Absolute Radiometric Gain - restore back to radiances
        :param toa: TOA in DN
        :param gain: gain in [rad/DN]
        :return: TOA in radiances [mW/sr/m2]
        """
        #TODO
        self.logger.debug('Sanity check. TOA in radiances after gain application ' + str(toa[1,-1]) + ' [mW/m2/sr]')
        toa = toa * gain
        return toa

    def plotL1bToa(self, toa_l1b, outputdir, band):
        #TODO

        center_value = int(toa_l1b.shape[0]/2)
        fig = plt.figure()
        plt.plot(toa_l1b[center_value,:],'b')
        plt.title('TOA_l1b')
        plt.xlabel('Across Track [-]')
        plt.ylabel('Radiances [mW/m2/sr]')
        plt.grid(True)
        plt.show()
        #fig.savefig(outputdir+'/l1b_toa_plot_'+band+'.png')
        fig.savefig(r'/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/Figuras/'+ 'l1b_toa_plot_'+band+'.png')

