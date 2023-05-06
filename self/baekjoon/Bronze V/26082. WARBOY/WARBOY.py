com_price, com_performance, warboy_price = map(int, input().split())
print(int(com_performance / com_price * warboy_price * 3))
