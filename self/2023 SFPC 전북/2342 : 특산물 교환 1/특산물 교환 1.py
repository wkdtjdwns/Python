n = int(input())
m = int(input())
have = n - m
cnt = 0

coin_values = [500, 100, 50, 10]

for coin_value in coin_values:
    cnt += have // coin_value
    have %= coin_value

print(cnt)
