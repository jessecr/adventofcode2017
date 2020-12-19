"""
"""

import re
import itertools
from collections import namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y', 'z'])
Particle = namedtuple('Particle', ['p', 'v', 'a'])
pattern = re.compile('p=<([\d,-]+)>, v=<([\d,-]+)>, a=<([\d,-]+)>')
particles = []
# fp = '''p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
# p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'''.splitlines()
with open('input', 'r') as fp:
# if True:
    for line in fp:
        match = pattern.match(line)
        # data = [Point(*map(int, match.group(i).split(','))) for i in range(1, 4)]
        data = [map(int, match.group(i).split(',')) for i in range(1, 4)]
        particle = Particle(*data)
        particles.append(particle)

def part2():
    destroyed = []
    for i in range(1000):
        points = defaultdict(list)
        for i, particle in enumerate(particles):
            if i in destroyed:
                continue

            particle.v[0] += particle.a[0]
            particle.v[1] += particle.a[1]
            particle.v[2] += particle.a[2]

            particle.p[0] += particle.v[0]
            particle.p[1] += particle.v[1]
            particle.p[2] += particle.v[2]

            points[tuple(particle.p)].append(i)

        for parts in points.values():
            if len(parts) > 1:
                destroyed.extend(parts)

    print len(particles) - len(destroyed)

def mdist(pos):
    return sum([abs(v) for v in pos])

def get_position(part, seconds):
    """ Returns the manhattan distance of a particle after seconds """
    vel_start = part.v
    acc = part.a
    pos = []
    for i in range(3):
        if acc[i] != 0:
            vel_end = vel_start[i] + (acc[i] * seconds)
            delta = sum(xrange(vel_start[i] + acc[i], vel_end + acc[i], acc[i]))
        else:
            delta = vel_start[i] * seconds

        pos.append(part.p[i] + delta)

    return pos

def part1():
    """ Find the particle that remains the closest to 0,0,0 for 500 seconds """
    closest = []
    for t in itertools.count(100, 100):
        res = sorted([(mdist(get_position(v, t)), i) for i, v in enumerate(particles)])
        closest.append(res[0][1])

        if len(closest) > 5 and len(set(closest[-5:])) == 1:
            print closest[-1]
            break

part2()
