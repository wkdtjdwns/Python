from sys import stdin
word = stdin.readline().rstrip()
n = len(word)
lines = ['.', '.', '#', '.', '.']
for i in range(n):
    if (i + 1) % 3 != 0:
        lines[0] += '.#.'
        lines[1] += '#.#'
        lines[2] += f'.{word[i]}.'
        lines[3] += '#.#'
        lines[4] += '.#.'

    else:
        lines[0] += '..*..'
        lines[1] += '.*.*.'
        lines[2] += f'*.{word[i]}.*'
        lines[3] += '.*.*.'
        lines[4] += '..*..'

    if (i + 1) % 3 == 1:
        lines[0] += '.'
        lines[1] += '.'
        lines[2] += '#'
        lines[3] += '.'
        lines[4] += '.'

if n % 3 == 2:
    lines[0] += '.'
    lines[1] += '.'
    lines[2] += '#'
    lines[3] += '.'
    lines[4] += '.'

for line in lines:
    print(line)
