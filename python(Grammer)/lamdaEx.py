def printx(x):
    print("x + y:",x)

# def sum(x,y):
#     return x+y

# n = sum(10,20)

# printx(n)

#lambda -> (lambda x,y: x+y) == def sum(x,y) return x+y
#lambda 매개변수: 함수 내용
n = (lambda x,y: x+y)(10,20)
printx(n)

m = (lambda x,y: x+y)("asdf","ghjkl")
printx(m)

#map(함수, 리스트)
print(list(map(lambda x: x**2, range(5))))

from functools import reduce

#reduce(함수, 시퀀스(문자열, 리스트, 튜플))
print(reduce(lambda x,y: x+y, range(5)))

print(list(filter(lambda x: x<7, range(10))))
print(list(filter(lambda x: x%2 ==0, range(10))))

