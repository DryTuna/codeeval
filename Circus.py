def build_tower(people):
    w_dict = sort_list(people, 0)   # sorted dict by weight
    h_dict = sort_list(people, 1)   # sorted dict by height
    r_dict = {}
    result = []
    for i in w_dict:
        # building a dictionary with value as rank
        r_dict[i] = w_dict[i] + h_dict[i] + min(w_dict[i], h_dict[i])
    r_dict = sorted(r_dict, key = lambda x: -r_dict[x])
    x = y = float('inf')
    for (w, h) in r_dict:
        if w <= x and h <= y:
            result.append((w, h))
            x, y = w, h
    print str(r_dict)
    return result

def min_index(item, dict1, dict2):
    if dict1[item] < dict2[item]:
        return dict1[item]
    else:
        return dict2[item]

def sort_list(people, index):
    x = {}
    y = sorted(people, key = lambda x: x[index])
    for i in range(len(people)):
        x[y[i]] = i
    return x


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
