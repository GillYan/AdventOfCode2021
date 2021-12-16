from math import prod
import fileinput

m = [list(map(int, line.strip())) for line in fileinput.input(files = 'input2.txt')]
h, w, part1, part2 = len(m), len(m[0]), 0, []

for r in range(h):
    for c in range(w):
        if any(
            m[r][c] >= m[x][y]
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if 0 <= (x := r + i) < h and 0 <= (y := c + j) < w
        ):
            continue

        part1 += m[r][c] + 1

        visited, visiting = set(), set([(r, c)])

        while visiting:
            a, b = visiting.pop()
            visited.add((a, b))

            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                if 0 <= (x := a + i) < h and 0 <= (y := b + j) < w \
                    and m[x][y] < 9 \
                    and (x, y) not in visited:
                    visiting.add((x, y))

        part2.append(len(visited))

print(part1)
print(sorted(part2)[-3:])
print(prod(sorted(part2)[-3:]))