"""
http://adventofcode.com/2017/day/2
"""
from itertools import combinations

def main(inp):
    """
    For each row, determine the difference between the largest value and the
    smallest value; the checksum is the sum of all of these differences.
    """
    diffs = []
    for row in inp.splitlines():
        cells = sorted([int(v) for v in row.split('\t')])
        diffs.append(cells[-1] - cells[0])

    return sum(diffs)

def main_part_2(inp):
    """
    For each row determine the only two numbers that are evenly divisble by each
    other and divide them. Return the sum of all the dividends
    """
    quotients = []
    for row in inp.splitlines():
        cells = [int(v) for v in row.split('\t')]
        cells.sort(reverse=True)
        # Compare each cell to all cells that have a smaller number until we
        # find the number that produces a whole number after division
        num_cells = len(cells)
        match = None
        for pair in combinations(cells, 2):
            quotient = pair[0] / float(pair[1])
            if quotient.is_integer():
                quotients.append(int(quotient))
                break
        else:
            raise ValueError("No whole number quotient found: {}".format(row))

        # Without itertools
        #
        # for i in range(num_cells):
        #     j = i + 1
        #     while j < num_cells:
        #         div = cells[i] / float(cells[j])
        #         if div.is_integer():
        #             match = div
        #             break
        #         j += 1

        #     if match is not None:
        #         break

        # quotients.append(int(match))

    return sum(quotients)

if __name__ == '__main__':
    with open('input', 'r') as fp:
        data = fp.read()

    print("Part 1 {}".format(main(data)))
    print("Part 2 {}".format(main_part_2(data)))
