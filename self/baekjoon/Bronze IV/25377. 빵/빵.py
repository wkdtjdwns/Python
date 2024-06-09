n = int(input())

sign = 0
minTime = 999999999999999
for _ in range(n):
    a, b = map(int, input().split(' '))
    
    if (b - a) < 0:
        continue
        
    else:
        minTime = min(minTime, b)
        sign = 1
        
if sign == 0:
    print(-1)

else:
    print(minTime)
