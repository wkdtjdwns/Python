s = input()
index = 0
for i in s:
    if index >= 10:
        index = 0
        print()

    print(i, end='')
    index += 1
