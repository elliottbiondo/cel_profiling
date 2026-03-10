CELER_BIH_MAX_LEAF_SIZE=316 /scratch/veb/build/celeritas-release-orange/bin/celer-sim inp-orange.json 1> orange.json
echo "ORANGE"
jq ".result.runner.time.total" orange.json
jq '.result.runner.time.actions.["along-step-neutral"]' orange.json
jq '.result.runner.time.actions.["along-step-uniform-msc"]' orange.json

echo "VG1"
/scratch/veb/build/celeritas-release/bin/celer-sim inp-vg1.json 1> vg1.json
jq ".result.runner.time.total" vg1.json
jq '.result.runner.time.actions.["along-step-neutral"]' vg1.json
jq '.result.runner.time.actions.["along-step-uniform-msc"]' vg1.json
