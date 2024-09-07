a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
cntA = 0
cntB = 0
for cardA, cardB in zip(a, b):
    if cardA > cardB: cntA += 1
    elif cardA < cardB: cntB += 1
        
if cntA > cntB: print('A')
elif cntA < cntB: print('B')
else: print('D')
