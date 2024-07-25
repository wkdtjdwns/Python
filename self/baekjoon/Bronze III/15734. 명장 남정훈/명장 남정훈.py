l, r, a = map(int, input().split(' '))
minValue, maxValue = min(l, r), max(l, r)

t = min(a, maxValue - minValue)
minValue += t
a -= t

result = minValue * 2 + (a // 2 * 2 if a else 0)
print(result)
