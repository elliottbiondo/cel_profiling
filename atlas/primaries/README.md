The file:

primaries_full_detector.jsonl was originally:

mc23_13p6TeV.601229.PhPy8EG_A14_ttbar_hdamp258p75_SingleLep.celeritas_Primaries.HITS.pool.root.jsonl

from Julien. Julien says that this is "a dump of EM primaries offloaded to
Celeritas from 10 ttbar events". In this version, the full ATLAS detector
geometry was present.

The primaries_full_detector.root file was created using the `primary-converter` tool in the `utils` repo on `celeritas-project`:

../opt/celeritas/utils/primaries-converter/convert primaries_full_detector.jsonl


An example of reading these files in found in make_csv.C, which you can run via:

root make_csv.C

Then exiting with .q

