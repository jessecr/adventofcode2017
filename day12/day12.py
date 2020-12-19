"""
"""

import re
from collections import defaultdict

with open('input', 'r') as fp:
    text = fp.read()

conns = {}
for line in text.splitlines():
    pieces = re.findall('\d+', line)
    conns[pieces[0]] = [n for n in pieces[1:] if n != pieces[0]]

groups = {}
all_seen = set()
for program in conns:
    if program in all_seen:
        continue

    to_visit = [program]
    seen = set(to_visit)

    while to_visit:
        connected = conns[to_visit.pop()]
        new = set(connected) - seen
        to_visit.extend(list(new))
        seen.update(new)

    groups[program] = seen
    all_seen.update(seen)

# Part 1
if '0' in groups:
    print len(groups['0'])
else:
    for group in groups.values():
        if '0' in group:
            print len(group)
            break

# Part 2
print len(groups)
