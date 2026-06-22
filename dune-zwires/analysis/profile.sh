###Step 1 run nsys systems to get the most expensive kernel:
#CUDA_VISIBLE_DEVICES=1 CELER_ENABLE_PROFILING=1 ORANGE_BVH_MAX_LEAF_SIZE=1 nsys profile \
#    --trace=cuda,nvtx,osrt \
#    --osrt-backtrace-stack-size=16384 \
#    --backtrace=fp \
#    -o dune-zwires-case1 \
#    -f true \
#    /scratch/veb/build/celeritas-release-orange-prof/bin/celer-optical ../inp.json

#    --capture-range nvtx \
#    --nvtx-capture "along-step@celeritas" \
#    --nvtx-domain-include celeritas \

# Step 2 run nys compute on the most expensive kernel
CUDA_VISIBLE_DEVICES=1 TMPDIR=$HOME/tmp/ncu ORANGE_BVH_MAX_LEAF_SIZE=1 ncu --set full --kernel-name launch_action_impl --replay-mode application --launch-skip 5488 --launch-count 1 -o dune-zwires-case65 \
/scratch/veb/build/celeritas-release-orange-prof/bin/celer-optical ../inp.json
