import sys
from collections import deque


def bfs(space, start):
    q = deque(start)
    temp = []
    while len(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not space[nx][ny]:
                space[nx][ny] = space[x][y]
                temp.append((nx, ny))
    return temp


Input = sys.stdin.readline
n, k = map(int, input().split())
space = [list(map(int, Input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())

virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if space[i][j]:
            virus.append((space[i][j], (i, j)))

virus.sort(key=lambda x: x[0])
for i in range(len(virus)):
    virus[i] = virus[i][1]

for _ in range(s):
    virus = bfs(space, virus)

print(space[X-1][Y-1])

# for i in space:
#     print(i)
