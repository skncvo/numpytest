#새로운 리스트의 포함 될 요소(x*2), for x in numbers if x%2==0(짝수인 경우)
numbers = [1,2,3,4,5,6]
doubled_numbers = [x*2 for x in numbers if x%2 ==0]
print(doubled_numbers)

#range(시작값, 끝값, 증가값)
for i in range(0,10,5):
    print(i)

#enumurate(리스트, 시작값): 인덱스와 함께 얻기기
names = ['alice', 'bob', 'charlie']
for i, name in enumerate(names):
    print(i, name)

#zip(리스트, 리스트): 리스트의 요소를 여러 변수로 정리리
ages = [14, 20, 17]
for age, name in zip(ages, names):
    print(name, age)

#enumurate + zip
for i, (age, name) in enumerate(zip(ages, names)):
    print(i, age, name)