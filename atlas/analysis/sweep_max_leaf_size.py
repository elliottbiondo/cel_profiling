import os
import numpy as np
import subprocess
import shutil

trials = [int(x) for x in np.logspace(0, 4.5, 10)]

outdir = "max_leaf_size"
shutil.rmtree(outdir, ignore_errors=True)
os.makedirs(outdir)

for trial in trials:
    print("Trial {}".format(trial))
    env = os.environ.copy()
    env["ORANGE_BIH_MAX_LEAF_SIZE"] = str(trial)

    with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
    #with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(f"{outdir}/sterr_{trial}", "w") as f_err:
        subprocess.run(["celer-sim", "/home/veb/cel_profiling/atlas/run.json"], env=env, stdout=f_out, stderr=f_err, check=False)

