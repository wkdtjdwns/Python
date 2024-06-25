a, b = map(int, input().split(' '))
c = int(input())

hour = (b + c) // 60
minute = (b + c) % 60

if (b + c) >= 60:
    if (a + hour) >= 24:
        a -= 24
    
    a += hour
    print(a, minute)
    
else:
    if (a >= 24):
        a-= 24
        
    print(a, (b + c))
