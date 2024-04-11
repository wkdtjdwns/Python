def find_angles(d):
    cnt = 0
    times = []

    for h in range(12):
        for m in range(60):
            hour_angle = h * 30 + m * 0.5
            minute_angle = m * 6

            angle_gap = abs(hour_angle - minute_angle)
            min_gap = min(angle_gap, 360 - angle_gap)

            if min_gap == d:
                cnt += 1
                times.append(f"{h:02d}:{m:02d}") # 변수:02d -> 두 자릿수로 바꿈 (3 -> 03)

    print(cnt)
    for time in times: print(time)

d = int(input())
find_angles(d)
