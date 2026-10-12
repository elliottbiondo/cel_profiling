#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
plt.rcParams['axes.axisbelow'] = True


cases = range(10)

results = []
for g in cases:
    with open(f'out_{g}.json') as f:
        data = json.load(f)
    results.append(data['result']['time']['total'])

levels = [x + 1 for x in cases]
per_level = [t / n for t, n in zip(results, levels)]

print(cases, results)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.grid()
s1 = ax1.scatter(levels, results, color='tab:blue', label="Total runtime")
s2 = ax2.scatter(levels, per_level, color='tab:orange', marker='^',
                 label="Runtime per level")

ax1.set_xlabel("State size, i.e., total number of universe levels")
ax1.set_ylabel("Runtime (s)")
ax2.set_ylabel("Runtime per level (s)")
ax1.tick_params(axis='y')
ax2.tick_params(axis='y')

ax1.set_xlim([0, 11])
ax1.set_ylim([0, 20])
ax2.set_ylim([0, max(per_level) * 1.1])

ax1.legend(handles=[s1, s2], loc='upper right')
ax1.set_title("Notional DUNE with varying number of void shells, InlineSingletons::none")
fig.savefig("out.pdf", bbox_inches='tight')
