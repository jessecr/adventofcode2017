"""
"""

import string
import itertools

with open('input', 'r') as fp:
    lines = fp.readlines()

rows = len(lines)
cols = len(lines[0])
# Directions: d, l, u r
d = 'd'
row = 0
col = lines[row].find('|')
letters = []
for i in itertools.count():
    cell = lines[row][col]
    if cell == ' ':
        break
    if cell in string.ascii_uppercase:
        letters.append(cell)
    elif cell == '+':
        # Corner
        if d in 'ud':
            if col + 1 < cols and lines[row][col + 1] == '-':
                d = 'r'
                col += 1
            elif col - 1 >= 0 and lines[row][col - 1] == '-':
                d = 'l'
                col -= 1
        else:
            if row + 1 < rows and lines[row + 1][col] == '|':
                d = 'd'
                row += 1
            elif row - 1 >= 0 and lines[row - 1][col] == '|':
                d = 'u'
                row -= 1
        continue
    if d == 'd':
        row += 1
    elif d == 'u':
        row -= 1
    elif d == 'r':
        col += 1
    elif d == 'l':
        col -= 1

print ''.join(letters)
print i
