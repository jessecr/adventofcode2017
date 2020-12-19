"""
"""

divisor = 2147483647
af = 16807
bf = 48271
a_last = 116
b_last = 299

total = 0
for _ in range(4 * 10 ** 7):
    a_last = (a_last * af) % divisor
    b_last = (b_last * bf) % divisor
    if '{:016b}'.format(a_last)[-16:] == '{:016b}'.format(b_last)[-16:]:
        total += 1

print total

a_values = []
b_values = []
while True:
    a_last = (a_last * af) % divisor
    b_last = (b_last * bf) % divisor
    if not a_last % 4:
        a_values.append('{:016b}'.format(a_last)[-16:])
    if not b_last % 8:
        b_values.append('{:016b}'.format(b_last)[-16:])

    if len(a_values) >= 5000000 and len(b_values) >= 5000000:
        break

print len([1 for a, b in zip(a_values, b_values) if a == b])
