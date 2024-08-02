abc = list(map(int, input().split(' ')))
odd = []
for i in range(3):
    if (abc[i] % 2) != 0:
        odd.append(abc[i])

result = 1
if not odd:
    for i in range(3):
        result *= abc[i]

else:
    for i in range(len(odd)):
        result *= odd[i]

print(result)
