"""
"""

import itertools

with open('input', 'r') as fp:
    text = fp.read()

moves = {'s': (0, -1),
         'sw': (-1, -1),
         'nw': (-1, 0),
         'n': (0, 1),
         'ne': (1, 1),
         'e': (1, 0),
         'se': (1, 0)}

def vector_add(a, b):
    return a[0] + b[0], a[1] + b[1]

farthest = 0
pos = (0, 0)
for move in text.split(','):
    pos = vector_add(pos, moves[move])
    farthest = max([farthest, sorted(pos)[1]])

print max(abs(c) for c in pos)
print farthest
