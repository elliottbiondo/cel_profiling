#!/usr/bin/env python3
import json
import matplotlib.pyplot as plt
plt.rcParams['axes.axisbelow'] = True


cases = list(range(11)) + [15, 20, 25]

results = []
for g in cases:
    with open(f'out_{g}.json') as f:
        data = json.load(f)
    results.append(data['result']['time']['total'])

print(cases, results)

plt.grid()
plt.scatter([x + 2 for x in cases], results)
plt.xlabel("State size, i.e., total number of universe levels")
plt.ylabel("Runtime (s)")
plt.xlim([0, 30])
plt.title("Notional DUNE with varying number of void shells, InlineSingletons::none}")
plt.savefig("out.pdf")

