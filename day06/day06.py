"""
http://adventofcode.com/2017/day/6
"""

def main(banks):
    """ Returns the number of redistributions of blocks among available banks
    until a configuration is produced that has already been seen
    """
    num_banks = len(banks)
    seen = {}
    count = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = count
        # Reverse sort by the value of the banks, using an enumerated list to be able to determine
        # the index of the highest value in cases where there are duplicates
        banks_sort = sorted(enumerate(banks), key=lambda x: x[1], reverse=True)
        # Get the number of blocks, reset to 0, and start redistributing
        index = banks_sort[0][0]
        blocks = banks[index]
        banks[index] = 0
        while blocks:
            index += 1
            if index == num_banks:
                # Loop back to the first bank
                index = 0
            banks[index] += 1
            blocks -= 1

        count += 1

    return count, count - seen[tuple(banks)]

if __name__ == '__main__':
    steps = []
    with open('input', 'r') as fp:
        banks = map(int, fp.readline().split('\t'))

    print main(banks)
