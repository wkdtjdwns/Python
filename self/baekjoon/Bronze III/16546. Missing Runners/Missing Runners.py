n = int(input())
nums = list(map(int, input().split(' ')))

result = 0
for i in range(n - 1):
    result += i + 1
    result -= nums[i]

print(result + n)
