#!/usr/bin/python2.6

from optparse import OptionParser
import cPickle as pickle
import os

def create_pickle_file(src, dst):
    word_struct = {}

    for word in open(src):
        word = word.strip()
        current = word_struct

        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault('words', []).append(word)

    pickle.dump(word_struct, open(dst, "wb"))

def load_words(dict_path):
    pckl_file = dict_path.replace(".txt", ".pckl")
    if not os.path.exists(pckl_file):
        create_pickle_file(dict_path, pckl_file)

    return pickle.load(open(pckl_file))

DOUBLE_LETTER = "DL"
TRIPLE_LETTER = "TL"
DOUBLE_WORD = "DW"
TRIPLE_WORD = "TW"
BASE_MULTIPLIERS = [
    ((0, 3), TRIPLE_WORD),    ((0, 6), TRIPLE_LETTER),
    ((1, 2), DOUBLE_LETTER),  ((1, 5), DOUBLE_WORD),
    ((2, 1), DOUBLE_LETTER),  ((2, 4), DOUBLE_LETTER),
    ((3, 0), TRIPLE_WORD),    ((3, 3), TRIPLE_LETTER),
    ((4, 2), DOUBLE_LETTER),  ((4, 6), DOUBLE_LETTER),
    ((5, 1), DOUBLE_WORD),    ((5, 5), TRIPLE_LETTER),
    ((6, 0), TRIPLE_LETTER),  ((6, 4), DOUBLE_WORD),
]

CENTERS = [
    (( 3,  7), DOUBLE_WORD),
    (( 7,  3), DOUBLE_WORD),
    ((11,  7), DOUBLE_WORD),
    (( 7, 11), DOUBLE_WORD),
]
# BASE_MULTIPLIERS are reflected left -> right
MULTIPLIERS = BASE_MULTIPLIERS \
        + [((y, 14 - x), v) for ((y, x), v) in BASE_MULTIPLIERS]

# then top -> bottom
MULTIPLIERS += [((14 - y, x), v) for ((y, x), v) in MULTIPLIERS]

MULTIPLIERS += CENTERS

mult_dict = dict(MULTIPLIERS)

div_row = " +" + "----+" * 15
def main():
    parser = OptionParser()
    parser.add_option("-d", "--dictionary", default="words.txt")

    (opts, args) = parser.parse_args()

    load_words(opts.dictionary)

    print div_row
    for x in range(0, 15):
        row = []
        for y in range(0, 15):
            row.append(mult_dict.get((x, y), "  "))
        print " | " + " | ".join(row) + " | "
        print div_row

if __name__ == "__main__":
    main()
