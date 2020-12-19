"""
"""

import string
import itertools

with open('input', 'r') as fp:
    moves = fp.read()

def dance(progs):
    for move in moves.split(','):
        if move[0] == 's':
            n = int(move[1:])
            progs = progs[-n:] + progs[:-n]
        elif move[0] == 'p':
            p1, p2 = move[1:].split('/')
            i1 = progs.index(p1)
            i2 = progs.index(p2)
            progs[i1], progs[i2] = progs[i2], progs[i1]
        elif move[0] == 'x':
            i1, i2 = map(int, move[1:].split('/'))
            progs[i1], progs[i2] = progs[i2], progs[i1]

    return progs

base = list(string.ascii_lowercase[:16])
print ''.join(dance(base[:]))

# Luckily there is a transformation cycle that happens pretty early on
progs = base[:]
for i in itertools.count():
    progs = dance(progs)

    if base == progs:
        break

progs = base[:]
for _ in range(10 ** 9 % (i + 1)):
    progs = dance(progs)

print ''.join(progs)
