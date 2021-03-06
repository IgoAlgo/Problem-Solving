"""
Reference
1. https://wlstyql.tistory.com/72

"""

from collections import deque

N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]


# print(visited[1][1][1][1])
# quit()
def pos_init():
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i,j
            elif B[i][j] == 'B':
                bx, by = i,j
    visited[rx][ry][bx][by] = True
    q.append((rx, ry, bx, by, 1))


def move(x, y, dx, dy):
    cnt = 0
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i]) 
            if B[nbx][nby] != 'O':
                if B[nrx][nry] == 'O':
                    return print(depth)
                if (nrx, nry) == (nbx, nby):
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth+1))
    print(-1)

solve()

            

    



                