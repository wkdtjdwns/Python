t = int(input())
for _ in range(t):
    _ = input()
    n = int(input())
    candies = [int(input()) for i in range(n)]

    print("YES" if sum(candies) % n == 0 else "NO")
