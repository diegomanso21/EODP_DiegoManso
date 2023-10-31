
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

#Para la parte l1b
# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'/Users/diegomanso/Documents/GitHub/EODP/auxiliary'
#/Users/diegomanso/Documents/GitHub/EODP/auxiliary
#indir = r"/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-ISM/myoutputs2"
indir = r"/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Material/EODP_TER_2021/EODP_TER_2021/EODP-TS-L1B/input"
outdir = r"/Users/diegomanso/Desktop/UC3M/2ºMiSE/EOP/Data/EODP-TS-L1B/myoutputs_noeq"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
