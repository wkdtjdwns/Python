a = []
for _ in range(int(input())):
    a.append(int(input()))

result = a[-1]
if a[2] - a[1] == a[1] - a[0]:
    result += (a[1] - a[0])

elif a[2] // a[1] == a[1] // a[0]:
    result *= (a[1] // a[0])

print(result)
