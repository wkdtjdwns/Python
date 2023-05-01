scoreList = []
score = 0
for i in range(5):
    scoreList.append(int(input()))
    score += scoreList[i]
print(score)
