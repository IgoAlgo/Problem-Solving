import sys

"""
나중 좌표 출력

test cases
5
R R R U D D
"""

n = int(input())
x, y = 1, 1
plans = sys.stdin.readline().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
