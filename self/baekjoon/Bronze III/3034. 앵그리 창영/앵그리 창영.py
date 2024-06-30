n, w, h = map(int, input().split(' '))
d = (w ** 2 + h ** 2) ** 0.5
for _ in range(n):
    num = int(input())
    print("DA" if num <= d else "NE")
