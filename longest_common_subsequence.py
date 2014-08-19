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
    m = [-1 for i in a]
    n = [-1 for i in a]
    index = 0
    maping = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                m[i] = index
                n[index] = j
                maping.append(a[i])
                index += 1
                b = b[:j]+'*'+b[j+1:]
                break
    x = rank(m, n)
    res = ""
    temp = [-1, -1]
    for (i, j) in x:
        if i > temp[0] and j > temp[1]:
            res += str(maping[i])
            temp[0] = i
            temp[1] = j
    return res


def rank(m, n):
    x = [i for i in m if i > -1]
    y = [i for i in n if i > -1]
    i = 0
    res = {}
    while i < len(x):
        num = len(x)-i + len(y)-y[x[i]] + min(len(x)-i,len(y)-y[x[i]])
        res[(i, y[x[i]])] = num
        i += 1
    return sorted(res, key = lambda x: -res[x])


if __name__ == '__main__':
    r = open(sys.argv[1], 'r')
    while True:
        a = str(r.readline())
        if len(a) > 0:
            print check(a)
        else:
            break
    r.close()
