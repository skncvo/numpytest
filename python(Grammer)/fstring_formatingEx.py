#fstring : (f"{변수}")
name = "카밀"
age = 11
print(f"도란 챔피언은 {name}이고, 나이는 {age}이다.")
#(f"{pi:.2f}")
pi = 3.1415926535
print(f"PI : {pi:.2f}")
#(now:%Y-%m-%d %H:%M)//Y:year, m:month, d:date, H:Hour, M:minute
from datetime import datetime
now = datetime.now()
print(f"현재 시간은 {now:%Y-%m-%d %H:%M}입니다.")

#fomat() : ("{변수}".format(변수 = "")) 
print("Newjeans is {M} and {H} ".format(M= "minji", H = "Haerin"))

