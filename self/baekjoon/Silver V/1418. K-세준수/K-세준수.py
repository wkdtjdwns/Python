n = int(input())
k = int(input())

prime = [True] * (n + 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, n + 1, i):
            prime[j] = False

result = [1] * (n + 1)
for i in range(2, n + 1):
    if prime[i] and i > k:
        for j in range(i, n + 1, i):
            result[j] = 0

print(sum(result) - 1)
