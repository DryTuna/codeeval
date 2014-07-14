def build_tower(people):
    w_sort = sort_list(people, 0)
    h_sort = sort_list(people, 1)
    w_dict = {}
    h_dict = {}
    result = []
    for i in range(len(people)):
        w_dict[w_sort[i]] = i
    for i in range(len(people)):
        h_dict[h_sort[i]] = i
    w_index = h_index = len(people)-1
    while w_index > -1 and h_index > -1:
        min_w_i = min_index(w_sort[w_index], w_dict, h_dict)
        min_h_i = min_index(h_sort[h_index], w_dict, h_dict)
        if min_w_i > min_h_i:
            if min_h_i > -1:
                result.append(w_sort[w_index])
                if min_w_i == 0:
                    break
                w_dict[w_sort[w_index]] = -1
                h_dict[w_sort[w_index]] = -1
                w_dict[h_sort[h_index]] = -1
                h_dict[h_sort[h_index]] = -1
                w_index -= 1
                h_index -= 1
            else:
                h_index -= 1
        else:
            if min_w_i > -1:
                result.append(h_sort[h_index])
                if min_h_i == 0:
                    break
                w_dict[h_sort[h_index]] = -1
                h_dict[h_sort[h_index]] = -1
                w_dict[w_sort[w_index]] = -1
                h_dict[w_sort[w_index]] = -1
                w_index -= 1
                h_index -= 1
            else:
                w_index -= 1
    return result


def min_index(item, dict1, dict2):
    if dict1[item] < dict2[item]:
        return dict1[item]
    else:
        return dict2[item]

def sort_list(people, index):
    return sorted(people, key = lambda x: x[index])


if __name__ == "__main__":
    people = [(1, 10),
              (2, 11),
              (3, 2),
              (4, 5),
              (5, 8),
              (6, 7),
              (7, 7.5),
              (8, 9)]
    print str(build_tower(people))
