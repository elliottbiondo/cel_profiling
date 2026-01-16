The file:

primaries_full_detector.jsonl was originally:

mc23_13p6TeV.601229.PhPy8EG_A14_ttbar_hdamp258p75_SingleLep.celeritas_Primaries.HITS.pool.root.jsonl

from Julien. Julien says that this is "a dump of EM primaries offloaded to
Celeritas from 10 ttbar events". In this version, the full ATLAS detector
geometry was present.

The primaries_LArEndcapNeg0x6cd79ea0.root file was created using the `primary-converter` tool in the `utils` repo on `celeritas-project`. The file:

~/opt/celeritas/utils/primaries-converter/src/JsonEventReader.cc

was was modified to ONLY reader particles born in the world volume of atlas-full-run4_LArEndcapNeg0x6cd79ea0.gdml:

        auto [x, y, z] = p.position;
        auto r = std::hypot(x, y);
        if (z > -3189  && z < -3185  && r < 1000 ||
            z > -3185  && z < -542   && r < 2260 ||
            z > -542   && z < -498.1 && r < 2506 ||
            z > -498.1 && z < 12     && r < 3795 ||
            z > 12     && z < 46     && r < 47)
        {
            result.push_back(std::move(p));
        }

The following command was then run:

~/opt/celeritas/utils/primaries-converter/convert primaries_full_detector.jsonl -o primaries_LArEndcapNeg0x6cd79ea0.root



An example of reading these files in found in make_csv.C, which you can run via:

root make_csv.C

Then exiting with .q

