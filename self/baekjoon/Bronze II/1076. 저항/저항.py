colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
a = str(colors.index(input()))
b = str(colors.index(input()))
c = str(10 ** colors.index(input()))

print(int(a + b + c[1:]))
