nums = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        nums.append(n)

if nums == []:
    print(-1)

else:
    print(sum(nums))
    print(min(nums))
