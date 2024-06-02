n = input()
alphabetList = [0] * 26

for i in n:
    alphabetList[ord(i) - 97] += 1

for i in alphabetList:
    print(i, end=' ')
