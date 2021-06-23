import sys

"""
왕실의 나이트 

"""

n = input()

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, -1, 2, -2, 2, -2]

x_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
x = x_dict[n[0]]
y = int(n[1])

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny > 8 or ny < 1:
        continue
    cnt += 1

print(cnt)
