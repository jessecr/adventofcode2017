"""
http://adventofcode.com/2017/day/4
"""

from collections import Counter

def main(phrases):
    """ Returns the number of phrases that have no repeating words """
    good = 0
    for phrase in phrases:
        count = Counter(phrase.split())
        if count.most_common(1)[0][1] == 1:
            # Means the most common item only occurs once
            good += 1

    return good

def main_2(phrases):
    good = 0
    for phrase in phrases:
        seen = set()
        for word in phrase.split():
            if word in seen:
                break
            seen.add(word)
        else:
            good += 1

    return good

def part2(phrases):
    good = 0
    sort_letters = lambda word: ''.join(sorted(word))
    for phrase in phrases:
        count = Counter([sort_letters(word) for word in phrase.split()])
        if count.most_common(1)[0][1] == 1:
            good += 1

    return good

if __name__ == '__main__':
    with open('input', 'r') as fp:
        phrases = []
        for line in fp:
            if line.strip():
                phrases.append(line.strip())

    print main(phrases)
    print part2(phrases)
