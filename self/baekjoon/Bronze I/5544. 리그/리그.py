def calculate(n, results):
    scores = [0] * (n + 1)
    for result in results:
        A, B, C, D = result
        if C > D:
            scores[A] += 3

        elif C < D:
            scores[B] += 3

        else:
            scores[A] += 1
            scores[B] += 1

    teamScores = [(scores[i], i) for i in range(1, n + 1)]
    teamScores.sort(key=lambda x: (-x[0], x[1]))
    ranks = [0] * (n + 1)
    current_rank = 1
    for i in range(n):
        if i > 0 and teamScores[i][0] < teamScores[i - 1][0]:
            current_rank = i + 1

        ranks[teamScores[i][1]] = current_rank

    return ranks[1:]


n = int(input().strip())
results = []
for _ in range(n * (n - 1) // 2):
    results.append(list(map(int, input().split(' '))))

ranks = calculate(n, results)
for rank in ranks:
    print(rank)
