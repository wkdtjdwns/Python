on = []
people = 0

for _ in range(1, 11):
    down, up = list(map(int,input().split()))
    people = people - down + up
    on.append(people)

on.sort()
print(on[-1])
