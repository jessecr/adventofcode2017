"""
http://adventofcode.com/2017/day/8
"""

import operator
from collections import defaultdict

with open('input', 'r') as fp:
    text = fp.read()

text2 = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

registers = {}
ops = {'inc': operator.add, 'dec': operator.sub}
comps = {'>': operator.gt,
         '<': operator.lt,
         '<=': operator.le,
         '>=': operator.ge,
         '==': operator.eq,
         '!=': operator.ne}

values = set()
for line in text.splitlines():
    reg1, op, amt, _, reg2, comp, amt2 = line.strip().split()
    if comps[comp](registers.get(reg2, 0), float(amt2)):
        val = ops[op](registers.get(reg1, 0), float(amt))
        values.add(val)
        registers[reg1] = val

print max(registers.items(), key=lambda x: x[1])
print max(values)
