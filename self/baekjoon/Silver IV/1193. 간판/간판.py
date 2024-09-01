def check(ganPan):
    l = len(ganPan)
    for start in range(l):
        if ganPan[start] == name[0]:
            for end_idx in range(start, l):
                if ganPan[end_idx] == name[-1]:
                    gap = (end_idx - start) // (n - 1)
                    cnt = 0
                    while cnt < n:
                        if ganPan[start + gap * cnt] == name[cnt]:
                            cnt += 1
                            continue
                        break

                    else:
                        return 1
    return 0

N = int(input())
name = input()
n = len(name)
ganPans = list(input() for _ in range(N))
cnt = 0
for ganPan in ganPans:
    cnt += check(ganPan)

print(cnt)
