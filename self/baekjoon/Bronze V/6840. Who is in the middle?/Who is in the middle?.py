numList = []
for i in range(3):
  numList.append(int(input()))
numList.remove(max(numList))
numList.remove(min(numList))
print(*numList)
