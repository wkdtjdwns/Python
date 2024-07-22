n = int(input())
a = list(map(int, input().split(' ')))
next = -1
battery = 0
y = 1
for i in range(n):
    if a[i] != next:
        battery += 2
        y = 2

    else:
        battery += 2 * y
        y *= 2

    next = a[i]

    if battery >= 100:
        battery = 0
        next = -1
        y = 1

print(battery)
