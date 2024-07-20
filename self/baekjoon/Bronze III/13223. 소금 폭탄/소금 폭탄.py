now = list(map(int, input().split(':')))
salt = list(map(int, input().split(':')))

nowTime = now[0] * 3600 + now[1] * 60 + now[2]
saltTime = salt[0] * 3600 + salt[1] * 60 + salt[2]

if nowTime >= saltTime:
    saltTime += 24 * 3600

result = saltTime - nowTime

h = str(result // 3600).zfill(2)
m = str((result % 3600) // 60).zfill(2)
s = str(result % 60).zfill(2)

print('{}:{}:{}'.format(h, m, s))
