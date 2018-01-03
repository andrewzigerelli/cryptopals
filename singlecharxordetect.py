#!/usr/bin/python
from singlebytexor import freq_score, singlebytexor
from operator import itemgetter


def main():
    lines = []
    for line in open("4.txt"):
        lines.append(line.rstrip())

    freq_scores = [freq_score(line) for line in lines]
    freq_max = [score[0] for score in freq_scores]

    index, maxx = max(enumerate(freq_max), key=itemgetter(1))

    #get all maxes
    max_freq = maxx[0]
    maxes=[index[0] for index in enumerate(freq_max) if index[1][0] == max_freq]

    #get all ciphertexts
    ciphers = [lines[index] for index in maxes]
    #decrypt
    msgs = [singlebytexor(cipher) for cipher in ciphers]
    print(msgs)

if __name__ == "__main__":
    main()
