a, b = map(int, input().split())
result = 0

while a >= 2:
    if b >= a - 1:
        print(2 * a - 1)
        break

    else: a -= 1
