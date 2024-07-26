s1, s2 = map(int, input().split(' '))
a1 = [list(map(int, input().split(' '))) for _ in range(s1)]
a2 = [list(map(int, input().split(' '))) for _ in range(s2)]
for i in range(s1):
    if a1[i][0] != a1[i][1]:
        print("Wrong Answer")
        exit()

for i in range(s2):
    if a2[i][0] != a2[i][1]:
        print("Why Wrong!!!")
        exit()

print("Accepted")
