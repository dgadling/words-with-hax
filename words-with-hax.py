#!/usr/bin/python2.6

from optparse import OptionParser
import cPickle as pickle
import os

def create_pickle_file(src, dst):
    word_struct = {}

    for word in open(src):
        word = word.strip()
        print "Looking at %s, have %s" % (word, word_struct)
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

def main():
    parser = OptionParser()
    parser.add_option("-d", "--dictionary", default="words.txt")

    (opts, args) = parser.parse_args()

    word_struct = load_words(opts.dictionary)
    import pprint
    pprint.pprint(word_struct)

if __name__ == "__main__":
    main()
