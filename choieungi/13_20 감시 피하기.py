import copy
from itertools import combinations


n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

space = []
blank = []
teachers = []

for i in range(n):
    temp = input().split()
    for j in range(n):
        if temp[j] == "X":
            blank.append((i, j))
        if temp[j] == "T":
            teachers.append((i, j))
    space.append(temp)


def dfs(space):
    for teacher_pos in teachers:
        a, b = teacher_pos
        for i in range(4):
            stack = [(a, b)]
            while len(stack):
                x, y = stack.pop()
                if x < 0 or x >= n or y < 0 or y >= n:
                    break

                if space[x][y] == 'S':
                    return False

                if space[x][y] == "O":
                    break

                x += dx[i]
                y += dy[i]
                stack.append((x, y))

    return True


flag = False
for walls in combinations(blank, 3):

    for x, y in walls:
        space[x][y] = "O"

    if dfs(space):
        print("YES")
        flag = True
        break

    for x, y in walls:
        space[x][y] = "X"


if not flag:
    print("NO")

#print(can_check)