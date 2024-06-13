nums = set()
result = 0

for _ in range(5):
    a = int(input())
    if a in nums:
        result -= a
        nums.discard(a)

    else:
        nums.add(a)
        result += a

print(result)
