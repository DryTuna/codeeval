"""
DESCRIPTION:
Two words are friends if they have a Levenshtein distance of 1
(For details see Levenshtein distance). That is, you can add,
remove, or substitute exactly one letter in word X to create
word Y. A word’s social network consists of all of its friends,
plus all of their friends, and all of their friends’ friends,
and so on. Write a program to tell us how big the social network
for the given word is, using our word list.

INPUT SAMPLE:           OUTPUT:

recursiveness           1
elastic                 3
macrographies           1
END OF INPUT
aa
aahed
aahs
aalii
...
...
zymoses
zymosimeters
"""
import sys


def distance(x):
    return x


if __name__ == '__main__':
    r = open(sys.argv[1], 'r')
    while True:
        a = str(r.readline())
        if len(a) > 0:
            print distance(a)
        else:
            break
    r.close()