sentence = 'Be happy!'

print(list(sentence))


chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]  # 바로 접니다..
minsu = [90, 60, 70]

student = [chulsu, younghee, yong, minsu]

for scores in student:
    total = 0
    for tt in scores:
        total = total + tt
    av = total/3
    print(scores, total, av)


N = [1,2,3,4,5,6,7,8,9,10]
print(N[::-1])
print(N[-4:])
print(N[:-4])
