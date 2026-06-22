ORANGE_BIH_STRUCTURE=1 ORANGE_BVH_STUCTURE=1 CUDA_VISIBLE_DEVICES=1 ORANGE_BIH_MAX_LEAF_SIZE=1 ORANGE_BIH_PART_CANDS=3 /scratch/veb/build/celeritas-release-orange/bin/celer-optical ../inp.json 1> out-orange.json
echo "ORANGE"
jq ".result.time.total" out-orange.json
jq '.result.time.actions.["along-step"]' out-orange.json

CUDA_VISIBLE_DEVICES=1 CUDA_HEAP_SIZE=10000000 CUDA_STACK_SIZE=32000 /scratch/veb/build/celeritas-release/bin/celer-optical ../inp.json 1> out-vg1.json
echo "VG1"
jq ".result.time.total" out-vg1.json
jq '.result.time.actions.["along-step"]' out-vg1.json
