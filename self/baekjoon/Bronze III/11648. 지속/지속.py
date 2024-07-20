n = input()
cnt = 0
while len(n) > 1:
    result = 1
    for i in n:
        result *= int(i)
        
    n = str(result)
    cnt += 1

print(cnt)
