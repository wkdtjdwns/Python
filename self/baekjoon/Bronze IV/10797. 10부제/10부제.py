day = int(input())
cars = list(map(int, input().split(' ')))

cnt = 0
for i in cars:
    if i == day:
        cnt += 1

print(cnt)
