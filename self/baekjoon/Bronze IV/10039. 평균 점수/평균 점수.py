scores = []
for i in range(5):
    scores.append( int( input() ) )
    if scores[i] < 40:
        scores[i] = 40

sum = 0
for j in range(5):
    sum += scores[j]

print(sum // 5)
