n = int(input())
result = []
for i in range(n):
    result.append(input())
    
k = int(input())
if k == 2:
    for i in range(n):
        result[i] = result[i][::-1]
        
elif k == 3:
    result = result[::-1]
    
for i in range(n):
    print(result[i])
