
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'/Users/diegomanso/Documents/GitHub/EODP/auxiliary'
indir = r"/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-E2E/sgm_out" # small scene
outdir = r"/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/myoutputs2"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
