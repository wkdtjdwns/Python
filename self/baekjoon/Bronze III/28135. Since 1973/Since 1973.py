n = int(input())
result = 0
for i in range(n):
    result += 1
    if str(i).find("50") > -1:
        result += 1

print(result)
