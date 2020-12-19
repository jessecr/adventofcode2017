"""
"""

from collections import deque

with open('input', 'r') as fp:
    lines = map(str.strip, fp.readlines())

registers = {}
def get_value(v):
    if v not in registers:
        return int(v)
    return registers[v]

def part1():
    i = 0
    last_sound = None
    while 0 <= i < len(lines):
        pieces = lines[i].split()
        cmd = pieces[0]
        reg = pieces[1]
        regval = registers.get(reg, 0)
        if cmd == 'set':
            registers[reg] = get_value(pieces[2])
        elif cmd == 'add':
            registers[reg] = regval + get_value(pieces[2])
        elif cmd == 'mul':
            registers[reg] = regval * get_value(pieces[2])
        elif cmd == 'mod':
            registers[reg] = regval % get_value(pieces[2])
        elif cmd == 'rcv' and regval != 0:
            registers[reg] = last_sound
            break
        elif cmd == 'jgz' and regval > 0:
            i += get_value(pieces[2])
            continue
        elif cmd == 'snd':
            last_sound = regval

        i += 1


    print last_sound

class Program(object):
    def __init__(self, pid, q, other_q, cmds):
        self.cmds = cmds
        self.pid = pid
        self.i = 0
        self.q = q
        self.other_q = None
        self.registers = {'p': self.pid}
        self.sent = 0

    def send(self, v):
        self.other_q.append(v)
        self.sent += 1

    def receive(self):
        return self.q.popleft()

    def get_value(self, v):
        if v in self.registers:
            return self.registers[v]
        return int(v)

    def run(self):
        while 0 <= self.i < len(self.cmds):
            pieces = self.cmds[self.i].split()
            cmd = pieces[0]
            reg = pieces[1]
            if cmd == 'set':
                self.registers[reg] = self.get_value(pieces[2])
            elif cmd == 'add':
                self.registers[reg] = self.get_register(reg) + self.get_value(pieces[2])
            elif cmd == 'mul':
                self.registers[reg] = self.get_register(reg) * self.get_value(pieces[2])
            elif cmd == 'mod':
                self.registers[reg] = self.get_register(reg) % self.get_value(pieces[2])
            elif cmd == 'rcv':
                try:
                    self.registers[reg] = self.receive()
                except IndexError:
                    break
            elif cmd == 'jgz' and self.get_value(reg) > 0:
                self.i += self.get_value(pieces[2])
                continue
            elif cmd == 'snd':
                self.send(self.get_value(reg))

            self.i += 1

    def get_register(self, r):
        return self.registers.get(r, 0)

def part2():
    q0 = deque()
    q1 = deque()
    p0 = Program(0, q0, q1, lines)
    p1 = Program(1, q1, q0, lines)
    p0.run()
    p1.run()
    while len(q0) or len(q1):
        p0.run()
        p1.run()

    print p1.sent


part1()
part2()
