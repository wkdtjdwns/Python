maxScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, input().split(' ')))
totalScore, isHacker = 0, False
for i in range(9):
    if score[i] > maxScore[i]: isHacker = True
    totalScore += score[i]

if isHacker: print("hacker")
else: print("draw" if totalScore >= 100 else "none")
