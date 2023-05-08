while True:
    cnt = 0
    str = input()
    if str == "#":
        break
    for i in range(len(str)):
        if str[i] == "A" or str[i] == "a" or str[i] == "E" or str[i] == "e"or str[i] == "I" or str[i] == "i" or str[i] == "O" or str[i] == "o" or str[i] == "U" or str[i] == "u":
            cnt += 1
    print(cnt)
