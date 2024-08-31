n = int(input())
a = list(map(int, input().split(' ')))
index = 0
for i in range(n):
  if a[i] == -1:
    index = i
    break

print(min(a[:index:]) + min(a[index + 1::]))
