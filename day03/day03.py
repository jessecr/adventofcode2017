"""
http://adventofcode.com/2017/day/3
"""
import math

def get_coordinate(nth):
    """ Returns the x,y coordinates of the nth element in the spiral sequence """
    if nth == 1:
        return 0, 0

    # The side of each spiral has an odd numbered length
    # Find the odd-numbered square roots that the square root of our number
    # is between (eg if nth=14, it is between the square roots 3 and 5)
    sqrt = math.sqrt(nth)
    if sqrt.is_integer() and int(sqrt) % 2:
        nth_odd_root = int(sqrt / 2)
        return (nth_odd_root, -nth_odd_root)

    floor_root = int(math.sqrt(nth))
    if not floor_root % 2:
        # Even number, and we want the nearest odd square roots
        floor_root -= 1
    ceil_root = floor_root + 2
    # While each side will have the same length as the upper square root, the length
    # of the each unique side (ie doesn't repeat corners) is one less
    section_len = ceil_root - 1

    floor_square = floor_root ** 2
    # Diff is how far into this spiral the number is, starting from 0
    diff = nth - floor_square - 1
    # print 'diff', diff

    # Sides are 0 - right, 1 - top, 2 - left, 3 - bottom
    side = diff / section_len
    # print 'side', side
    # Place is where the number sits along the given side
    place = diff % section_len

    # Convert this all to coordinates
    # Sides 0 and 2 each vary in the y-axis, and sides 1 and 3 each vary in x-axis
    # pos is the distance from the center to the side that our number is on
    pos = (ceil_root - 1) // 2
    # If it's the left or bottom side, then it's negative
    if side >= 2:
        pos *= -1

    half = ceil_root // 2
    # offset is the distance from the center of the side of our number
    # print 'Place', place
    offset = place - half + 1
    if side in (1, 2):
        offset *= -1
    # print 'Offset', offset

    x = pos
    y = offset

    if side % 2:
        x, y = y, x

    return x, y

def main(inp):
    x, y = get_coordinate(inp)

    return x + y

def get_surrounding(grid, coordinate):
    """ Returns the sum of all squares that are adjacent to a coordinate in a grid """
    offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    total = 0
    for offset in offsets:
        to_check = coordinate[0] + offset[0], coordinate[1] + offset[1]
        total += grid.get(to_check, 0)

    return total

def print_grid(grid):
    sorted(grid.items(), key=lambda x: x[0], reverse=True)

def main_part_2(inp):
    """
    As a stress test on the system, the programs here clear the grid and then
    store the value 1 in square 1. Then, in the same allocation order as shown
    above, they store the sum of the values in all adjacent squares, including diagonals.

    So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum
        of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

    Returns the first value that is larger than the input
    """
    grid = {}
    grid[(0, 0)] = 1
    i = 2
    while True:
        coord = get_coordinate(i)
        total = get_surrounding(grid, coord)
        # print i, coord, total
        if total > inp:
            print grid
            # print_grid(grid)
            return total

        grid[coord] = total
        i += 1

    print grid

from itertools import count
from collections import defaultdict

def sum_spiral():
    a, i, j = {}, 0, 0
    a[0,0] = 1
    sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                for l in range(j-1,j+2))
    for s in count(1, 2):
        print s
        for _ in range(s):   i += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s):   j += 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): i -= 1; a[i,j] = sn(i,j); yield a[i,j]
        for _ in range(s+1): j -= 1; a[i,j] = sn(i,j); yield a[i,j]
        print sorted(dict(a).items(), key=lambda x: x[0])

def part2(n):
    for x in sum_spiral():
        if x>n: return x

if __name__ == '__main__':
    print part2(700)


    # print("Part 1 {}".format(main(361527)))
    # print("Part 2 {}".format(main_part_2(361527)))
    # print get_coordinate(9)
    # for i in range(1, 35):
    #     coord = get_coordinate(i)
    #     print i, coord
    #     print
    # main(1024)
