'''
Created on Jun 8, 2015

@author: duytran
'''
import sys

def TwentyFortyEight(x):
    inputs = x.split(';')
    board = [[int(item) for item in row.split()] for row in inputs[2].split('|')]

    if inputs[0] == 'RIGHT':
        print(solve_right(board))
    elif inputs[0] == 'DOWN':
        print(solve_down(board))
    elif inputs[0] == 'UP':
        print(solve_up(board))
    elif inputs[0] == 'LEFT':
        print(solve_left(board))

def solve_right(board):
    temp = [[x for x in row[-1::-1]] for row in board]
    temp = solve_board(temp)
    result = ''
    for row in temp:
        row += [0] * (len(board) - len(row))
        row = row[-1::-1]
        for i in row:
            result += str(i) + ' '
        result = result[:-1] + '|'
    return result[:-1]
    
def solve_left(board):
    temp = solve_board(board)
    result = ''
    for row in temp:
        row += [0] * (len(board) - len(row))
        for i in row:
            result += str(i) + ' '
        result = result[:-1] + '|'
    return result[:-1]

def solve_up(board):
    temp = [i for i in zip(*board)]
    temp = solve_board(temp)
    result = ''
    for row in temp:
        row += [0] * (len(board) - len(row))
    temp = [i for i in zip(*temp)]
    for row in temp:
        for i in row:
            result += str(i) + ' '
        result = result[:-1] + '|'
    return result[:-1]

def solve_down(board):
    temp = [i for i in zip(*board)]
    temp = [[x for x in row[-1::-1]] for row in temp]
    temp = solve_board(temp)
    result = ''
    for row in temp:
        row += [0] * (len(board) - len(row))
    temp = [i for i in zip(*temp)]
    for row in temp[-1::-1]:
        for i in row:
            result += str(i) + ' '
        result = result[:-1] + '|'
    return result[:-1]

def solve_board(board):
    result = []
    for row in board:
        res = []
        wall = 0
        for i in row:
            if (i > 0):
                if wall < len(res):
                    if res[wall] == i:
                        res[wall] = i << 1
                    else:
                        res.append(i)
                    wall += 1
                else:
                    res.append(i)
        result.append(res)
    return result

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        if len(test) > 0:
            TwentyFortyEight(test)
    test_cases.close()