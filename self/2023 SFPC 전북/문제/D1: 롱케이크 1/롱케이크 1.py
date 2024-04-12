n = int(input())
piece_nums = list(map(int, input().split()))

cut_one_num = 0
cut_two_num = 0

for i in range(n):
    j = piece_nums[0]

    if j+1 in piece_nums and j-1 in piece_nums: cut_two_num += 1
    elif j+1 in piece_nums or j-1 in piece_nums: cut_one_num += 1
    piece_nums.pop(0)

print(cut_one_num, cut_two_num)
