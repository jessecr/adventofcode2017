"""
http://adventofcode.com/2017/day/1
"""

def main(inp):
    """
    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list.
    The list is circular, so the digit after the last digit is the first digit
    in the list.
    """
    i = 0
    as_str = str(inp)
    to_sum = []
    for i in range(len(as_str) - 1):
        if as_str[i] == as_str[i + 1]:
            to_sum.append(int(as_str[i]))

    if as_str[-1] == as_str[0]:
        to_sum.append(int(as_str[0]))

    return sum(to_sum)

# -----
# Part 2
# -----

def main_2(inp):
    """
    The captcha requires you to review a sequence of digits (your puzzle input)
    and find the sum of all digits that match the next digit in the list.
    The list is circular, so the digit after the last digit is the first digit
    in the list.
    """
    i = 0
    as_str = str(inp)
    to_sum = []
    str_len = len(as_str)
    incr = str_len / 2
    for i in range(str_len):
        compare_idx = (i + incr) % str_len
        if as_str[i] == as_str[compare_idx]:
            to_sum.append(int(as_str[i]))

    return sum(to_sum)

if __name__ == '__main__':
    with open('input', 'r') as fp:
        inp = int(fp.readline().strip())

    print("Part 1 {}".format(main(inp)))
    print("Part 2 {}".format(main_2(inp)))

