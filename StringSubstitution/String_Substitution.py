def String_Substitution(x):
    x = x.split(';')
    s = [(str(x[0]), True)]
    fr = []
    tmp = x[1].split(',')
    i = 0
    while i < len(tmp):
        fr.append((str(tmp[i]), str(tmp[i+1])))
        i += 2
    for (fi, ri) in fr:
        tmp = []
        # print fi, ri
        for (sub, touch) in s:
            if touch:
                head = 0
                tail = 0
                i = 0
                while i < len(sub):
                    if i + len(fi) <= len(sub):
                        if str(sub[i:i+len(fi)]) == fi:
                            tail = i
                            if head != tail:
                                tmp.append((sub[head:tail], True))
                            tmp.append((ri, False))
                            i += len(fi) - 1
                            head = i + 1
                    i += 1
                if len(sub[head:]) > 0:
                    tmp.append((sub[head:], True))
            else:
                tmp.append((sub, touch))
        # print tmp
        s = tmp[:]
    print ''.join(str(k) for (k, j) in s)


if __name__ == "__main__":
    import sys
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.split()
        if len(test) > 0:
            String_Substitution(test[0])
        # print s

    test_cases.close()
