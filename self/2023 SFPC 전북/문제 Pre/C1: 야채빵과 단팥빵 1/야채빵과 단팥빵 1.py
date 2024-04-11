from datetime import datetime, timedelta

s_date = input()
e_date = input()
s_year, s_month, s_day = map(int, s_date.split('.'))
e_year, e_month, e_day = map(int, e_date.split('.'))

veg_bread = 0
red_bean_bread = 0

cur_date = datetime(s_year, s_month, s_day)
end_date = datetime(e_year, e_month, e_day)

while cur_date <= end_date:
    if cur_date.weekday() == 4:
        m = cur_date.month
        d = cur_date.day
        veg_bread += m + d
        red_bean_bread += (m + d) * 2

    cur_date += timedelta(days = 1)

print(veg_bread, red_bean_bread)
