from functools import reduce

num = []
for x in input().split():
    num.append(int(x))

add = reduce(lambda a, b: a + b, num)
minus = reduce(lambda a,b: a - b, num)
multi = reduce(lambda a,b: a * b, num)
division = reduce(lambda a,b:  a / b, num)

print(add, minus, multi, division)