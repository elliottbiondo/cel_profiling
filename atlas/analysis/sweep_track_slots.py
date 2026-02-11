import os
import numpy as np
import subprocess
import shutil
import json


def write_temp_with_track_slots(num_track_slots):

    with open("/home/veb/cel_profiling/atlas/run.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data["num_track_slots"] = num_track_slots

    with open("temp.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")



trials = [2**x for x in range(15, 21)]

outdir = "track_slots"
shutil.rmtree(outdir, ignore_errors=True)
os.makedirs(outdir)

for trial in trials:

    print("Starting trial: {}\n", trial)

    write_temp_with_track_slots(trial)

    with open(f"{outdir}/stdout_{trial}.json", "w") as f_out, open(os.devnull, "w") as f_err:
        subprocess.run(["celer-sim", "temp.json"], stdout=f_out, stderr=f_err, check=False)

    os.remove("temp.json")








