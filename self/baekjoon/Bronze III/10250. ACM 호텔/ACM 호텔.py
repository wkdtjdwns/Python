for i in range(int(input())):
    h, w, n = map(int, input().split(' ')) 
    floor = n % h
    roomLine = (n // h) + 1
    
    if floor == 0:
        floor = h
        roomLine -= 1

    print(floor * 100 + roomLine)
