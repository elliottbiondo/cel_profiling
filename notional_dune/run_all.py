#!/usr/bin/env python3
import os

template = open("inp_template.json").read()

cases = list(range(11)) + [25, 50, 100]

for g in cases: 
    open("inp_temp.json", "w").write(template.replace("GEONUM", str(g)))
    os.system(f"CUDA_VISIBLE_DEVICES=1 /scratch/veb/build/celeritas-release-orange/bin/celer-optical inp_temp.json 1> out_{g}.json")
    os.remove("inp_temp.json")

for g in cases:
    printf("g:\n\t")
    os.system(f'jq ".result.time.total" out_{g}.json')

