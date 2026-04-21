ORANGE_BIH_MAX_LEAF_SIZE=1 /scratch/veb/build/celeritas-release-orange/bin/celer-sim inp-orange.json 1> out-orange.json
echo "ORANGE"
jq ".result.runner.time.total" out-orange.json
jq '.result.runner.time.actions.["along-step-uniform-msc"]' out-orange.json
jq '.result.runner.time.actions.["along-step-neutral"]' out-orange.json


CUDA_HEAP_SIZE=10000000 CUDA_STACK_SIZE=32000 /scratch/veb/build/celeritas-release/bin/celer-sim inp-vg1.json 1> out-vg1.json
echo "VG1"
jq ".result.runner.time.total" out-vg1.json
jq '.result.runner.time.actions.["along-step-uniform-msc"]' out-vg1.json
jq '.result.runner.time.actions.["along-step-neutral"]' out-vg1.json
