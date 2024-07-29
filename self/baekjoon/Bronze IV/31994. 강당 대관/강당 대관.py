seminars = []
for _ in range(7):
    seminar, num = input().split(' ')
    seminars.append([seminar, int(num)])

seminars.sort(key=lambda x: -x[1])
print(seminars[0][0])
