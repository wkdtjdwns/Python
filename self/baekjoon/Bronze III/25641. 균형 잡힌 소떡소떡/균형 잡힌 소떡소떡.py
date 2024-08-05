N = int(input())
s = input()
st = list(reversed(s))

while True:
    if st.count('s') == st.count('t'):
        break

    else:
        st.pop(-1)

st.reverse()
print(''.join(st))
