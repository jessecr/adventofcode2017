"""
http://adventofcode.com/2017/day/9
"""

with open('input', 'r') as fp:
    text = fp.read()

def process(text):
    total, group, garbage_count, i = 0, 0, 0, 0
    garbage = False
    char_count = len(text)
    while i < char_count:
        c = text[i]
        i += 1
        if c == '!':
            i += 1
            continue

        if garbage:
            if c == '>':
                garbage = False
            else:
                garbage_count += 1
        elif c == '{':
            group += 1
            total += group
        elif c == '}':
            group -= 1
        elif c == '<':
            garbage = True

    return total, garbage_count


inp = []
inp.append('{}')
inp.append('{{{}}}')
inp.append('{{},{}}')
inp.append('{{{},{},{{}}}}')
inp.append('{<a>,<a>,<a>,<a>}')
inp.append('{{<ab>},{<ab>},{<ab>},{<ab>}}')
inp.append('{{<!!>},{<!!>},{<!!>},{<!!>}}')
inp.append('{{<a!>},{<a!>},{<a!>},{<ab>}}')

print process(text)
