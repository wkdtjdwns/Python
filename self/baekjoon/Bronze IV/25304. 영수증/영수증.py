total = int(input())
type = int(input())
sum = 0
for _ in range(type):
    price, cnt = map(int, input().split())
    sum += price*cnt
if total == sum:
    print("Yes")
else:
    print("No")
