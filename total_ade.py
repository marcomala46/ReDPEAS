#! /usr/bin/env python3

import os, pandas as pd, glob
from multiprocessing import Pool
import sys
from io import StringIO
import re

trg_file = sys.argv[1]
total = []
lig = sys.argv[2]

if os.path.dirname(trg_file):
    root = os.path.dirname(trg_file)
else:
    root = '.'

path = f'{root}/*{os.path.splitext(os.path.basename(trg_file))[0]}/*.pdbqt'
    
cwd = os.getcwd()
lig = pd.DataFrame(map(lambda x: x.split(),re.findall('ATOM.*', open(f'{root}/{lig}_PLP.pdbqt').read())))
atoms = lig[~lig[3].isin(['PLP', 'LYS'])][1].astype(int).tolist()

for run in glob.glob(path):
    try:
        os.chdir(os.path.dirname(run))
        ade = os.popen(f'~/G_BIOSCIENZE/ADFRsuite_x86_64Linux_1.0/bin/pythonsh ~/G_BIOSCIENZE/ADFRsuite_x86_64Linux_1.0/CCSBpckgs/ADFR/bin/ade.py -t ../{os.path.basename(trg_file)} -l {os.path.basename(run)}').read()
        os.chdir(cwd)

        idx = [StringIO(ade[x.span()[0]:x.span()[1]]) for x in list(re.finditer('_+.*\n(\s+\d+.*\n)+', ade))]
        lrr, ll = [pd.read_csv(x, skiprows = 1, header=None,keep_default_na=False,
                        delim_whitespace=True) for x in [idx[0], idx[2]]]
        lrr[0] = lrr[0]+1  ### numero atomo sbagliato in LRR, la numerazione parte da 0 anziché da 1
        lrr_energy = lrr[lrr[0].isin(atoms)][2].sum()
        ll[[1,10]] = ll[1].str.split('-',expand=True).astype(int)
        ll_energy = ll[(ll[1].isin(atoms))|(ll[10].isin(atoms))][5].sum()
        energy = ll_energy + lrr_energy
        total.append([os.path.basename(trg_file), os.path.basename(run), lrr_energy])
        print(lrr_energy)
    except:
        pass
os.chdir(cwd)

pd.DataFrame(total).to_csv(f'{os.path.splitext(trg_file)[0]}_energie_totali.csv', index = None)
