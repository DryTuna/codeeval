def build_tower(people):
    r_dict = sort_list(people)
    result = []
    x = y = float('inf')
    for (w, h) in r_dict:
        if w <= x and h <= y:
            result.append((w, h))
            x, y = w, h
    return result


def sort_list(people):
    x = {}
    # sort by first index
    y = sorted(people, key = lambda x: x[0])
    for i in range(len(people)):
        x[y[i]] = [i, 0]

    # sort by second index
    y = sorted(people, key = lambda x: x[1])
    for i in range(len(people)):
        x[y[i]][1] = i

    # compute rank for every pair
    for i in x:
        x[i] = x[i][0] + x[i][1] + min(x[i][0], x[i][1])

    # return sorted list in descending rank order
    return sorted(x, key = lambda i: -x[i])


if __name__ == "__main__":
    people = [(1, 10),
              (2, 11),
              (3, 2),
              (4, 5),
              (5, 8),
              (6, 7),
              (7, 7.5),
              (8, 9),
              (1, 12),
              (12, 1)]
    print str(build_tower(people))

    z = 8
    people = []
    for i in range(z):
        for j in range(z):
            people.append((i, j))
    print str(build_tower(people))