"""
"""

img = '''.#.
..#
###'''

def get_rulebook_example():
    rules = {}
    for line in ['../.# => ##./#../...',
                 '.#./..#/### => #..#/..../..../#..#']:
            pat, rule = line.strip().split(' => ')
            rules[pat] = rule
    return rules


def get_rulebook():
    with open('input', 'r') as fp:
        rules = {}
        for line in fp:
            pat, rule = line.strip().split(' => ')
            rules[pat] = rule

    return rules

def get_squares(board):
    """ Yields sub-regions of a board according to the rules """
    board_size = len(board)
    if board_size % 2 == 0:
        size = 2
    elif board_size % 3 == 0:
        size = 3
    else:
        return

    squares = []
    for r in range(0, board_size, size):
        for col in range(0, board_size, size):
            squares.append([board[row][col:col + size] for row in range(r, r + size)])

    return squares

def rotations(square):
    """ Returns all possible rotations for a given square.
    A square can be rotated in 90 degree increments, and can be flipped. This
    results in 8 possible orientations for each square (4 x 2)
    """
    size = len(square)
    flipped = [square[size - r - 1][:] for r in range(size)]
    orientations = [square, flipped]
    for sq in [square, flipped]:
        rot3 = [sq[r][c] for c in range(3) for c in range(3)[::-1]]
        rot3 = [sq[r][c] for r in range(3)[::-1] for c in range(3)[::-1]]
        rot3 = [sq[r][c] for c in range(3)[::-1] for c in range(3)]

        orientations.append(rot1)
        orientations.append(rot2)
        orientations.append(rot3)

    return orientations

def flatten(sq):
    """ Flattens a square """
    return '/'.join([''.join(row) for row in sq])

def expand(flat):
    """ Expands a flat square """
    return [list(row) for row in flat.split('/')]

def part1():
    rules = get_rulebook()
    board = [list(row) for row in img.splitlines()]
    for _ in range(1):
        squares = get_squares(board)
        new_squares = []
        for square in squares:
            for rot in rotations(square):
                flat = flatten(rot)
                if flat in rules:
                    new_sq = rules[flat]
                    new_squares.append(expand(new_sq))
                    break
            else:
                raise ValueError("Could not find matching rule for {}".format(square))

part1()
board = '''123
456
789'''
board = '''12
34'''
# rotations([list(p) for p in board.splitlines()])
