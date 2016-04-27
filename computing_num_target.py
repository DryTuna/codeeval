import itertools
import parser

def f(num, target):
	list_num = staircase(len(num))
	result = []
	res = []
	for i in list_num:
		opt = operator(len(i)-1)
		for j in opt:
			my = cc(i,num)
			temp = ""+my[0]
			for x in range(0, len(j)):
				temp+=j[x]+""+my[x+1]
				print(temp, j)
			if eval(parser.expr(temp).compile()) == target:
				result.append(str(temp)+"="+str(target))
		
	return result
	
def cc(m, num):
	x = 0
	res = []
	for i in m:
		res.append(num[x:x+i])
		x += i
	return res

def staircase(n):
    result = [[1]]
    for i in range(2, n+1):
        temp = []
        for j in result:
            for x in range(0,len(j)):
                j[x] += 1
                if j not in temp:
                    temp.append(j[:])
                j[x] -= 1
        temp.append([1 for one in range(i)])
        result = temp
    return result[::-1]
    
def operator(n):
	opt = ['+','-','*','/']
	result = []
	for i in itertools.product(opt, repeat=n):
		result += [i]
	return result


print(f("9876", 59))
