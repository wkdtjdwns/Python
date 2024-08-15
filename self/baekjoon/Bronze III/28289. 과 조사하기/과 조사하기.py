result = [0] * 4
for _ in range(int(input())):
    students = list(map(int, input().split(' ')))

    if students[0] == 1:
        result[3] += 1
        continue

    if students[1] == 1 or students[1] == 2: result[0] += 1
    elif students[1] == 3: result[1] += 1
    else: result[2] += 1

for r in result:
    print(r)
