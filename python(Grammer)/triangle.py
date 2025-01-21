len = int(input('변의 길이: '))

for i in range(len):
    print("* " * (i+1))

area = (len**2)/2
print('넓이: ', area)