year1, mouth1, day1 = map(int, input().split(' '))
year2, mouth2, day2 = map(int, input().split(' '))

man = 0
if (year2 > year1) and ((mouth2 > mouth1) or (mouth2 == mouth1) and (day2 >= day1)):
    man = year2 - year1

else:
    man = year2 - year1 - 1

if man < 0:
    man = 0
age = year2 - year1 + 1
yearAge = year2 - year1

print(man)
print(age)
print(yearAge)
