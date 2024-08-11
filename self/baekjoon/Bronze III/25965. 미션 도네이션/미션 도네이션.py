for _ in range(int(input())):
    m = int(input())
    mission = []
    for _ in range(m):
        mission.append(list(map(int, input().split(' '))))

    K, D, A = map(int, input().split(' '))
    result = 0
    for k, d, a in mission:
        score = (K * k - D * d + A * a)
        if score > 0:
            result += score

    print(result)
