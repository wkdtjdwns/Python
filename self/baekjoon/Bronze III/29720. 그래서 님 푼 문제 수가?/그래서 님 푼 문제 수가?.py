import sys
input = sys.stdin.readline

n, m, k = map(int, input().split(' '))
minValue = max(n - (m * k), 0)
maxValue = n - m * (k - 1) - 1

print(minValue, maxValue)
