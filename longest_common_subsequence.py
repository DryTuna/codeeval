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


def check(x):
    a, b = x.split(';')
    m = []
    n = []
    o = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                m.append(str(a[i]))
                n.append(j)
                o.append(0)
                b = b[:j]+'*'+b[j+1:]
                break
    size = len(n)
    index = 0
    for i in range(size):
        j = i+1
        h = i
        while j < size:
            if n[h] < n[j]:
                m[i] += m[j]
                h = j
            j += 1
        if len(m[i]) > len(m[index]):
            index = i
    return str(m[index])


if __name__ == '__main__':
    r = open(sys.argv[1], 'r')
    while True:
        a = str(r.readline())
        if len(a) > 0:
            print check(a)
        else:
            break
    r.close()
