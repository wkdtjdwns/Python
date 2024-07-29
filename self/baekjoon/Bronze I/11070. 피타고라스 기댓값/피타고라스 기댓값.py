for _ in range(int(input())):
    n, m = map(int, input().split(' '))
    scores = [[0, 0] for _ in range(n)]
    w = []

    for _ in range(m):
        a, b, p, q = map(int, input().split())
        scores[a - 1][0] += p
        scores[a - 1][1] += q
        scores[b - 1][0] += q
        scores[b - 1][1] += p

    for i in range(n):
        if scores[i][0] == 0 and scores[i][1] == 0: w.append(0)
        else: w.append(1000 * scores[i][0] ** 2 / (scores[i][0] ** 2 + scores[i][1] ** 2))

    print(int(max(w)))
    print(int(min(w)))
