r = 31
M = 1234567891

def H(string):
    num = 0
    for i in range(len(string)):
        num += ((ord(string[i].lower())-96) * (r**i))

    return num % M

if __name__ == "__main__":
    string = input("문자열을 입력하세요 : ")
    print(H(string))