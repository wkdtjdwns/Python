n = int(input())
prices = [int(input()) for _ in range(n)]

m = int(input())
total = 0
for _ in range(m): total += prices[int(input()) - 1]

print(total)
