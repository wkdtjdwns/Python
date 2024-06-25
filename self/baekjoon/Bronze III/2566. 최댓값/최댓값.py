nums = [list(map(int, input().split(' '))) for _ in range(9)]

maxNum = 0
maxRow, maxCol = 0, 0
for i in range(9):
    for j in range(9):
        if maxNum <= nums[i][j]:
            maxRow = i + 1
            maxCol = j + 1
            maxNum = nums[i][j]

print(maxNum)
print(maxRow, maxCol)
