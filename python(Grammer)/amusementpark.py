def read(text):
    ridname, rs = text.split(":")
    ridname = ridname.strip()
    rs = rs.strip()

    cmmin = cmmax = None

    if "~" in rs:
        parts = rs.split("~")
        cmmin = int(parts[0].strip().replace("cm", "").strip())  # 하한 추출 및 변환
        cmmax = int(parts[1].strip().replace("cm", "").strip())  # 상한 추출 및 변환
    elif "이상" in rs and "이하" in rs:
        pass  # 문제에 이런 케이스가 없으므로 구현하지 않음
    else:
        if "이상" in rs:
            cmmin = int(rs.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환
        elif "이하" in rs:
            cmmax = int(rs.split("cm")[0].strip())  # 숫자 부분만 추출 후 정수 변환

    return ridname, cmmin, cmmax



if __name__ == "__main__":
    ridname, cmmin, cmmax = read(input())
    print("이름:", ridname)
    print("하한:", cmmin)
    print("상한:", cmmax)