"""
DESCRIPTION:
You are given two sequences. Write a program to determine the longest
common subsequence between the two strings (each string can have a
maximum length of 50 characters). NOTE: This subsequence need not be
contiguous. The input file may contain empty lines, these need to
be ignored.

INPUT:
The first argument will be a path to a filename that contains two
strings per line, semicolon delimited. You can assume that there is only
one unique subsequence per test case. E.g.
XMJYAUZ;MZJAWXU

OUTPUT:
MJAU
"""
import sys


def check_sequence(a, b):
    y = u''
    for i in a:
        c = 0
        for j in b:
            c += 1
            if i == j:
                y += str(i)
                b = b[c:]
                break
    return y


def check(x):
    a, b = x.split(';')
    y = u''
    while a:
        z = check_sequence(a, b)
        a = a[1:]
        if len(z) > len(y):
            y = z
    return y

if __name__ == '__main__':
    r = open(sys.argv[1], 'r')
    while True:
        a = str(r.readline())
        if len(a) > 0:
            print check(a)
        else:
            break
    r.close()
