#!/usr/bin/env python3

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
            label = "{}=({:.4f}, {:.4f})".format(axis, left_plane, right_plane)
            lines.append('  n{} [label="{}"];'.format(i, label))
        else:
            vols = ", ".join("{}".format(v) for v in node[1])
            lines.append('  n{} [label="vols=[{}]"];'.format(i, vols))

    for i, node in enumerate(tree):
        if node[0] == "i":
            left_child = int(node[2][0])
            right_child = int(node[2][1])
            lines.append('  n{} -> n{} [label="L"];'.format(i, left_child))
            lines.append('  n{} -> n{} [label="R"];'.format(i, right_child))

    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Print BIH summary and write bih_<universe>.dot files."
    )
    parser.add_argument("json_file", type=Path, help="Path to Celeritas output JSON")
    parser.add_argument(
        "universe",
        nargs="*",
        type=int,
        help="Optional universe index(es). If omitted, write all.",
    )
    args = parser.parse_args()

    with args.json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    bih = data["internal"]["orange"]["bih_metadata"]
    depth = bih["depth"]
    num_vols = bih["num_finite_bboxes"]
    num_inf_vols = bih["num_infinite_bboxes"]
    structure = bih["structure"]

    print("{:>8} {:>6} {:>8} {:>9}".format("univ", "depth", "num_vols", "num_inf"))
    for i in range(len(structure)):
        print(
            "{:>8} {:>6} {:>8} {:>9}".format(
                i, int(depth[i]), int(num_vols[i]), int(num_inf_vols[i])
            )
        )

    if len(args.universe) > 0:
        selected = args.universe
    else:
        selected = list(range(len(structure)))

    for uid in selected:
        tree = structure[uid]["tree"]
        dot = make_dot(uid, tree)
        out_path = Path.cwd() / "bih_{}.dot".format(uid)
        out_path.write_text(dot, encoding="utf-8")


if __name__ == "__main__":
    main()
