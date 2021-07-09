import sys
from collections import deque

Input = sys.stdin.readline

n, m = map(int, Input().split())
space = []
for _ in range(n):
    temp = (list(map(int, input())))
    space.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(space,a,b):
    q = deque([(a,b)])
    while len(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and space[nx][ny] == 1:
                space[nx][ny] = space[x][y] + 1
                q.append((nx,ny))

bfs(space,0,0)
print(space[n-1][m-1])
