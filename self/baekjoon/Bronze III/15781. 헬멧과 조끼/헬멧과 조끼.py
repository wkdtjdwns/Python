n, m = map(int, input().split(' '))
h = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

hMax, aMax = max(h), max(a)
print(hMax + aMax)
