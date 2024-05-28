stList = list()

for i in range(24):
    stList.append(0)

num = int(input())
numList = input().split()

for i in range(num):
    stList[int(numList[i])] += 1

for i in range(1, len(stList)):
    print(stList[i], end=' ')
