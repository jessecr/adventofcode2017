"""
"""
# Hacky but whatever
import sys
import itertools
from path import Path
sys.path.append(Path(__file__).parent.parent.parent)
from adventofcode2017.day10 import day10

def build_binary_grid():
    inp = 'ugkiagan'
    # inp = 'flqrgnkx'
    rows = []
    for i in range(128):
        hash = day10.knot_hash('{}-{}'.format(inp, i))
        rows.append(''.join(['{:04b}'.format(int(c, 16)) for c in hash]))

    return rows

def part1():
    total = sum(map(int, itertools.chain(*build_binary_grid())))
    print total

def find_adjacent_in_row(row, idx):
    """ Returns a list of indices of used cells that are adjacent to the given index
    for the given row
    """
    adjacent = list(itertools.takewhile(lambda x: row[x], xrange(idx - 1, 0, -1)))
    adjacent.extend(itertools.takewhile(lambda x: row[x], xrange(idx + 1, 128)))

    return adjacent

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

def find_adjacent(rows, r, c, seen=None):
    cell = rows[r][c]
    if seen is None:
        seen = set()
    seen.add((r, c))
    for rc, cc in DIRECTIONS:
        nr = r + rc
        nc = c + cc
        if 127 >= nr >= 0 and 127 >= nc >= 0:
            cell2 = rows[nr][nc]
            if cell2 == '1' and (nr, nc) not in seen:
                find_adjacent(rows, nr, nc, seen)

    return seen

def part2():
    rows = build_binary_grid()
    seen = set()
    group = 0
    for r, row in enumerate(rows):
        for c in range(128):
            if row[c] == '1' and (r, c) not in seen:
                group += 1
                seen.update(find_adjacent(rows, r, c))

    print group


part2()
