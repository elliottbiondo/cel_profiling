import os
import numpy as np
import subprocess
import shutil

trials = [int(x) for x in range(1, 11)]

outdir = "depth_limit"
shutil.rmtree(outdir, ignore_errors=True)
os.makedirs(outdir)

for trial in trials:
    print("Trial {}".format(trial))
    env = os.environ.copy()
    env["ORANGE_BIH_MAX_LEAF_SIZE"] = "100"
    env["ORANGE_BIH_DEPTH_LIMIT"] = str(trial)

    with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
        subprocess.run(["celer-sim", "/home/veb/cel_profiling/atlas/run.json"], env=env, stdout=f_out, stderr=f_err, check=False)

