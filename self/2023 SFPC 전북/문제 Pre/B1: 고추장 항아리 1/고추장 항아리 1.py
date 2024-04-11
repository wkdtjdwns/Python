n = int(input())
num = int(n / 5)
price = 150000 * num
if (n%5 != 0): num += 1
print(num, price)
