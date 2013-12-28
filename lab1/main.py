import string, logging, itertools
from collections import defaultdict, Counter

# read input data and decode it from hex
def read_file(filename):
    with open(filename) as lines:
        for line in lines:
            yield line.strip().decode('hex')

# make two strings one sized (with the repeations of the shortest one)
def normalize_lengths(s1, s2):
    if len(s1) < len(s2):
        k = (len(s2) / len(s1)) + 1
        s1 = (s1 * k)[:len(s2)]
    elif len(s2) < len(s1):
        k = (len(s1) / len(s2)) + 1
        s2 = (s2 * k)[:len(s1)]

    return s1, s2

# God bless StackOverflow!
def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

# get all texts xorred each with every
def combinations(data):
    for word1, word2 in itertools.combinations(data, 2):
        yield word1, word2, sxor(word1, word2)

# get possible letter matches
def possible_matches(data):
    possibilities = defaultdict(list)

    # if the xorred texts' symbol is a letter - it was probably xorred with a space.
    # so this is the same letter yet either a upper or down-cased.
    # that means: the key will contain either letter from source1 xorred with space,
    # either corresponding letter from source2 xorred with space.
    for word1, word2, xorred in data:
        for (i, char) in enumerate(xorred):
            if char in string.letters:
                possibilities[i].extend([ ord(word1[i]) ^ 32, ord(word2[i]) ^ 32 ])

    return possibilities

# get the part of the key
def possible_key(possibilities):
    # get the letter at each position, which was hit most times at that position as the key
    return "".join(chr(Counter(item).most_common(1)[0][0]) for item in possibilities.values())

if __name__ == '__main__':
    data = list(read_file('input.txt'))
    possibilities = possible_matches(combinations(data))

    key = possible_key(possibilities)
    print("key (hex): {0}".format(key.encode('hex')))

    for i, target in enumerate(data):
        print("text[{0}]: {1}".format(i, sxor(target, key)))
