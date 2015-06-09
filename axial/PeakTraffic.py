'''
Created on Jun 9, 2015

@author: duytran
'''

import sys

my_dict = {}
flag = {}

def PeakTraffic():
    result = []
    for start in sorted(my_dict, key=sort_key):
        if not flag[start]:
            res = [start]
            for end in my_dict[start]:
                if my_dict[start][end]:
                    res.append(end)
            if len(res) > 2 and sub_set(res, my_dict[start], start):
                result.append(sorted(res, key=sort_key))
                for item in res:
                    flag[item] = True
    for res in result:
        line = ''
        for item in res:
            line += str(item) +', '
        print(line[:-2])

def sort_key(item):
    return item[:-13]

def sub_set(result, mdict, start):
    mdict[start] = True
    for item in result:
        if item not in mdict:
            return False
    return True

def build_graph(line):
    line = line.split()
    start = line[-2]
    end = line[-1]
    if start not in my_dict:
        my_dict[start] = {}
        flag[start] = False
    if end in my_dict:
        if start in my_dict[end]:
            my_dict[start][end] = True
            my_dict[end][start] = True
        else:
            my_dict[start][end] = False
    else:
        my_dict[start][end] = False

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        build_graph(test)
    test_cases.close()
    PeakTraffic()
    
    