n = int(input())
p = int(input())
sale = [0]

if n >= 5:
    sale.append(500)

if n >= 10:
    sale.append(p // 10)

if n >= 15:
    sale.append(2000)

if n >= 20:
    sale.append(p // 4)

result = p - max(sale)
if result < 0:
    result = 0

print(result)
