import argparse
import json
from pathlib import Path

def make_dot(universe_id, tree):
    lines = []
    lines.append('digraph "bih_{}" {{'.format(universe_id))
    lines.append("  graph [rankdir=TB];")
    lines.append('  node [shape=box, fontname="Helvetica"];')

    for i, node in enumerate(tree):
        if node[0] == "i":
            axis = node[1]
            left_plane = float(node[3][0])
            right_plane = float(node[3][1])
            label = "{}=({:.2f}, {:.2f})".format(axis, left_plane, right_plane)
            lines.append('  n{} [label="{}"];'.format(i, label))
        else:
            vols = ", ".join("{}".format(v) for v in node[1])
            lines.append('  n{} [label="vols=[{}]"];'.format(i, vols))

    for i, node in enumerate(tree):
        if node[0] == "i":
            left_child = node[2][0]
            right_child = node[2][1]
            lines.append('  n{} -> n{} [label="L"];'.format(i, left_child))
            lines.append('  n{} -> n{} [label="R"];'.format(i, right_child))

    lines.append("}")
    return "\n".join(lines)

def print_diagnostic(bih_data):

    depth = bih_data["depth"]
    nvol = bih_data["num_finite_bboxes"]
    ninf = bih["num_infinite_bboxes"]
    template = "{:>8} {:>8} {:>8} {:>8}"

    out = template.format("uid", "depth", "num_vols", "num_inf")
    for i in range(len(structure)):
        out += template.format(i, depth[i], nvol[i], ninf[i])


def main():
    parser = argparse.ArgumentParser(
        description="Print BIH summary and write bih_<universe>.dot files."
    )
    parser.add_argument("json_file", type=Path, help="Path to output JSON")
    parser.add_argument(
        "universe",
        nargs="*",
        type=int,
        help="Optional universe index(es). If omitted, write all.",
    )
    args = parser.parse_args()
    
    # Read all necessary data from json
    with args.json_file.open("r") as f:
        bih_data = json.load(f)["internal"]["orange"]["bih_metadata"]

    # Figure out what universes to write dot file for
    if len(args.universe) > 0:
        uids = args.universe
    else:
        uids = list(range(len(bih_data["structure"])))

    # Write dot files for the selected universes
    for uid in uids:
        with open("bih_{}.dot".format(uid), "w") as f:
            f.write(make_dot(uid, bih_data["structure"][uid]["tree"]))


if __name__ == "__main__":
    main()
