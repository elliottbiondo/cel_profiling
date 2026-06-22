# CUDA_VISIBLE_DEVICES=1 CELER_ENABLE_PROFILING=1 ORANGE_BIH_MAX_LEAF_SIZE=1 nsys profile \
#    --trace=cuda,nvtx,osrt \
#    --nvtx-domain-include celeritas \
#    --osrt-backtrace-stack-size=16384 \
#    --backtrace=fp \
#    -o atlas_case58 \
#    -f true \
#    /scratch/veb/build/celeritas-release-orange-prof/bin/celer-sim inp-orange.json

CUDA_VISIBLE_DEVICES=1 TMPDIR=$HOME/tmp/ncu ORANGE_BIH_MAX_LEAF_SIZE=1 ncu --set full --kernel-name launch_action_impl --replay-mode application --launch-skip 641 --launch-count 1 -o atlas-case58 \
/scratch/veb/build/celeritas-release-orange-prof/bin/celer-sim inp-orange.json


~
