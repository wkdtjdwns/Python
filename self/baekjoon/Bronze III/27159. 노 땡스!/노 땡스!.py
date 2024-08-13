n = int(input())
cards = list(map(int, input().split(' '))) + [0] 

result = []
temp = []
for i in range(n):
    temp.append(cards[i])

    if (cards[i + 1] - cards[i]) != 1:
        result.append(temp)
        temp = []

total = 0
for j in result:
    total += j[0]

print(total)
