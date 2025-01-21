def palindrome(s):
    s = s.lower()
    #s = s.replace(" ", "")
    s = s.strip()

    return s[:] == s[::-1]

if  __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome(x) == x:
            print(f"'{x}' is a palindrome")
        else :
            print(f"'{x}' is not a palindrome")
