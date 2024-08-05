n = int(input())
nums = list(map(int, input().split(' ')))
sum = 0
result = 0
for i in range(len(nums) - 1, 0, -1):
    sum += nums[i]
    result += nums[i - 1] * sum

print(result)
