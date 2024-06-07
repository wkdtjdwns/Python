s, k, h = map(int, input().split(' '))
if (s + k + h) >= 100:
    print("OK")

else:
    club = min(s, k, h)
    if club == s:
        print('Soongsil')

    elif club == k:
        print('Korea')

    else:
        print('Hanyang')
