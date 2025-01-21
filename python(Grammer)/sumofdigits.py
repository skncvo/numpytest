def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)

if __name__ == '__main__':
    print(sumOfDigits(486541))
    print(sumOfDigits(643))