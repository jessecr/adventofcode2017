"""
http://adventofcode.com/2017/day/5
"""

def main(steps):
    """ Returns the number of steps to exit the list """
    num_steps = len(steps)
    count = 0
    i = 0
    while -1 < i < num_steps:
        to_move = steps[i]
        steps[i] += 1
        i += to_move

        count += 1

    return count

def part2(steps):
    num_steps = len(steps)
    count = 0
    i = 0
    while -1 < i < num_steps:
        to_move = steps[i]
        if to_move >= 3:
            steps[i] -= 1
        else:
            steps[i] += 1
        i += to_move

        count += 1

    return count

if __name__ == '__main__':
    steps = []
    with open('input', 'r') as fp:
        for line in fp:
            steps.append(int(line.strip()))

    print main(steps[:])
    print part2(steps[:])
