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

def main():
    parser = OptionParser()
    parser.add_option("-d", "--dictionary", default="words.txt")

    (opts, args) = parser.parse_args()

    load_words(opts.dictionary)

if __name__ == "__main__":
    main()
