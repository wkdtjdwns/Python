damage = [list(map(int, input().split())) for _ in range(3)]
h = int(input())
second = 0

while True:
    for i in damage:
        c, d = i[0], i[1]
        if second % c == 0:
            h -= d

    if h <= 0:
        print(second)
        break

    else:
        second += 1
