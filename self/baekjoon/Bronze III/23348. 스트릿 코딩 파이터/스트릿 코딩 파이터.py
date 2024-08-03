level = list(map(int, input().split(' ')))
n = int(input())
grades = []
for _ in range(n):
    grade = 0
    for _ in range(3):
        a = list(map(int, input().split(' ')))
        for i in range(3):
            grade += a[i] * level[i]

    grades.append(grade)

print(max(grades))
