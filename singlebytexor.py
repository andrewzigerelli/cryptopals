#!/usr/bin/python
import sys
from fixedxor import xor
from helper import *


#main
def main():
    enc = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    freq = freq_score(enc)
    freq_char = freq[0][1]
    #print(freq_char)
    #print(hex2ascii(enc))

    #assume this freq_char maps to space
    #http://fitaly.com/board/domper3/posts/136.html
    space = ascii2hex(" ")
    key_char = xor(space, freq_char)
    #create full length key and decrypt
    key = key_char * int(len(enc) / 2)

    msg = xor(key, enc)
    msg = hex2ascii(msg)
    print(msg)


def freq_score(string):
    """returns a sorted list of pairs sorted by char frequency
    assumes the input string is byte representation i.e. ascii hex string"""

    #get bytes (chars)
    string = [string[2 * i:2 * i + 2] for i in range(0, int(len(string) / 2))]

    #get freq
    freq = [(string.count(char) / len(string), char) for char in set(string)]
    freq = sorted(freq, reverse=True)
    return freq


if __name__ == "__main__":
    main()
