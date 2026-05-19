CUDA_VISIBLE_DEVICES=1 ORANGE_BIH_MAX_LEAF_SIZE=1 /scratch/veb/build/celeritas-release-orange/bin/celer-optical inp-orange.json 1> out-orange.json
echo "ORANGE"
jq ".result.time.total" out-orange.json
jq '.result.time.actions.["along-step"]' out-orange.json

CUDA_VISIBLE_DEVICES=1 CUDA_HEAP_SIZE=10000000 CUDA_STACK_SIZE=32000 /scratch/veb/build/celeritas-release/bin/celer-optical inp-vg1.json 1> out-vg1.json
echo "VG1"
jq ".result.time.total" out-vg1.json
jq '.result.time.actions.["along-step"]' out-vg1.json
