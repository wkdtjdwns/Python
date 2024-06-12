n = int(input())
times = list(map(int, input().split(' ')))
total = (len(times) - 1) * 8

for t in times:
    total += t

print(total // 24, total % 24)
