n = int(input())
result = []

for i in range(1, n + 1):
    first = n
    second = i
    temp = [n, i]

    while True:
        next = first - second
        if next >= 0:
            temp.append(next)
            first = second
            second = next

        else:
            if len(temp) > len(result):
                result = temp
            break

print(len(result))
print(*result)
