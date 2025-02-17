import glob
import pandas as pd

# # --------HAMD
sublist = pd.read_csv('/Volumes/QC/INT/INT_BN246_HC135BP_allMDD/Results/INTvalue_MDD.csv')
allbehavior = pd.read_csv('/Volumes/QC/Data/behaviors/allDataMDD_HAMD.csv')
finalbehavior = pd.merge(allbehavior, sublist, on='subID', how='inner')
finalbehavior.to_csv('./AllData_HAMD_final.csv', index=False)

