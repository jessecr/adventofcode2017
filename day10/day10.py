"""
"""

import itertools

def get_input():
    with open('input', 'r') as fp:
        return fp.read()

def part1():
    lengths = map(int, get_input().split(','))
    nums = run(lengths)

    print nums[0] * nums[1]

def run(lengths, rounds=1):
    nums = list(range(256))
    pos, skip = 0, 0
    # The problem specifies that no length can be longer than the base list, which
    # means that we only have to support a single loop/wrap around
    all_indices = nums + nums
    for _ in range(rounds):
        for length in lengths:
            start = pos % 256
            indices = all_indices[start:start + length]
            # Pair each index with the index it is being swapped with
            index_swaps = zip(indices, reversed(indices))[:len(indices) // 2]
            for i, j in index_swaps:
                nums[i], nums[j] = nums[j], nums[i]
            pos += length + skip
            skip += 1

    return nums

def part2():
    print knot_hash(get_input())

def knot_hash(inp):
    nums = list(range(256))
    lengths = []
    for c in inp:
        lengths.append(ord(c))
    lengths.extend([17, 31, 73, 47, 23])

    nums = run(lengths, 64)
    dense_hash = []
    for i in range(0, 256, 16):
        dense_hash.append(reduce(lambda x, y: x ^ y, nums[i:i + 16]))

    hexstring = ''.join(['{:0>2}'.format(hex(n)[2:]) for n in dense_hash])

    return hexstring

def main():
    part1()
    part2()
