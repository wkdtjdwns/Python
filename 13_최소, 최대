N = int(input())

N_list = list(map(int, input().split()))

# max와 min에 각 각 N_list의 첫번째 요소를 넣어준다.
max = N_list[0]
min = N_list[0]

for i in N_list[1 :]:
    # for문에서 N_list의 2번째 요소부터 마지막 요소까지 차례로 비교해준다.
    if i > max:
        # max보다 크면, max값을 바꿔주고 
        max = i

    elif i < min:
        # min보다 작으면, min값을 바꿔준다.
        min = i

print(min, max)
