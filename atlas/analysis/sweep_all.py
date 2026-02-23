import os
import numpy as np
import subprocess
import shutil
import sys

###############################################################################

def sweep_depth_limit(node):
    trials = range(1, 11)
    
    outdir = "{}/depth_limit".format(node)
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir)
    
    for trial in trials:
        env = os.environ.copy()
        env["ORANGE_BIH_MAX_LEAF_SIZE"] = "100"
        env["ORANGE_BIH_DEPTH_LIMIT"] = str(trial)
    
        with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
            subprocess.run(["celer-sim", "run.json"], env=env, stdout=f_out, stderr=f_err, check=False)

###############################################################################

def sweep_max_leaf_size(node):

    trials = [int(x) for x in np.logspace(0, 4.5, 10)]
    
    outdir = "{}/max_leaf_size".format(node)
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir)
    
    for trial in trials:
        env = os.environ.copy()
        env["ORANGE_BIH_MAX_LEAF_SIZE"] = str(trial)
    
        with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
            subprocess.run(["celer-sim", "run.json"], env=env, stdout=f_out, stderr=f_err, check=False)

###############################################################################

def sweep_track_slots(node):

    def write_temp_with_track_slots(num_track_slots):
        with open("run.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            data["num_track_slots"] = num_track_slots
    
        with open("temp.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")

    trials = [2**x for x in range(15, 21)]
    
    outdir = "{}/track_slots".format(node)
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir)
    
    for trial in trials:
    
        write_temp_with_track_slots(trial)
    
        with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
            subprocess.run(["celer-sim", "temp.json"], stdout=f_out, stderr=f_err, check=False)
    
        os.remove("temp.json")

###############################################################################

def sweep_part_cands(node):
    trials = [3**x for x in range(0, 8)]
    
    outdir = "{}/part_cands".format(node)
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir)
    
    for trial in trials:
        env = os.environ.copy()
        env["ORANGE_BIH_MAX_LEAF_SIZE"] = "100"
        env["ORANGE_BIH_PART_CANDS"] = str(trial)
    
        with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
            subprocess.run(["celer-sim", "run.json"], env=env, stdout=f_out, stderr=f_err, check=False)


###############################################################################
# DRIVER
###############################################################################s

node = sys.argv[1]

#sweep_track_slot(node)
#sweep_max_leaf_size(node)
#sweep_depth_limit(node)
sweep_part_cands(node)
