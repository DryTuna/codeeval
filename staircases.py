def staircase(n):
    result = [[1]]
    for i in xrange(2, n+1):
        temp = []
        for j in result:
            for x in xrange(0,len(j)):
                j[x] += 1
                if j not in temp:
                    temp.append(j[:])
                j[x] -= 1
        temp.append([1 for one in xrange(i)])
        result = temp
    return result

if __name__ == "__main__":
    for i in xrange(2, 6):
        print str(staircase(i))
