for _ in range(int(input())):
    mm = list(map(int, input().split(' ')))
    result = 0
    for i in range(1, len(mm) - 1):
        for j in range(i + 1, len(mm)):
            if mm[i] > mm[j]:
                mm[i], mm[j] = mm[j], mm[i]
                result += 1

    print(mm[0], result)
