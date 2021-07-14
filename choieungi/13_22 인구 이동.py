import sys
from collections import deque


def bfs(space, a, b, visited):
    location = []
    q = deque([(a,b)])
    peoples = 0
    while len(q):
        x, y = q.popleft()
        visited[x][y] = True
        location.append((x,y))
        peoples += space[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(space[nx][ny] - space[x][y])
                if l <= diff <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    if len(location) > 1:
        avg = int(peoples/len(location))
        for x, y in location:
            space[x][y] = avg

        return 1
    return 0


Input = sys.stdin.readline
n, l, r = map(int, input().split())
space = [list(map(int, Input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0

while True:
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(space, i, j, visited)

    visited = [[False] * n for _ in range(n)]
    if cnt:
        ans += 1
    else:
        break


print(ans)
