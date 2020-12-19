"""
"""

step = 367

def part1():
    b = [0]
    c = 0
    for i in xrange(1, 2018):
        movement = c + step
        c = (movement % i) + 1
        b.insert(c, i)

    print b[c + 1]

def part2():
    """ We only need to track the most recent value added after 0 (at index 1) """
    iterations = 5 * 10 ** 7
    last = None
    c = 0
    for i in xrange(1, iterations + 1):
        c = (step + c) % i
        if c == 0:
            last = i
        c += 1

    print last

part1()
part2()
