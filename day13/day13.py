"""
"""

with open('input', 'r') as fp:
    text = fp.read()

text2 = '''0: 3
1: 2
4: 4
6: 4'''

layers = {}
for line in text.splitlines():
    layer, depth = map(int, line.split(': '))
    layers[layer] = depth

def part1():
    severity = 0
    for i, r in layers.items():
        # The number of seconds it takes for this scanner to complete a loop and
        # return to the starting/top position, shifted to start at zero (like layers do)
        loop = (r * 2) - 2
        if i >= loop and i % loop == 0:
            severity += i * r

    print severity

def is_a_multiple(a, b):
    """ Returns True if a a can be evenly divided by b """
    return a % b == 0

def add_interval(num, intervals):
    """ Adds an interval to the list if it is not already present and is not a
    multiple of another interval
    """
    if num not in intervals:
        for i, n in enumerate(intervals[:]):
            if is_a_multiple(num, n):
                break
            elif is_a_multiple(n, num):
                # An existing interval is a multiple of our number. Swap them
                intervals[i] = num
                break
        else:
            # Not a multiple
            intervals.append(num)

def increment_offset(offset, intervals):
    """ Returns a new offset that has been increased by at least 1 such that it is
    not a multiple of any of the numbers in intervals
    """
    pass

def part2():
    offset = 0
    intervals = {}
    for i, r in layers.items():
        if r == 1:
            raise ValueError("Scanner at depth {} has a range of 1 and cannot"
                             " be avoided".format(i))

        # Determine the interval in seconds between when the scanner is at the top
        # Offset it to start at 0 like the depths do
        loop = (r * 2) - 2
        intervals[i] = loop

    # Start the offset at 1 because the first scanner will always trigger with no offset
    offset = 1
    while True:
        for i, interval in intervals.items():
            seconds = i + offset
            if seconds >= interval and seconds % interval == 0:
                offset += 1
                break
        else:
            break

    print offset


part1()
part2()
