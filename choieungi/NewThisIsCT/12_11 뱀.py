import sys
from collections import deque

Input = sys.stdin.readline

n = int(Input())
apple_number = int(Input())

space = [[0]*n for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

for _ in range(apple_number):
    x, y = map(int, Input().split())
    space[x-1][y-1] = 1

move_number = int(Input())

move_list = [tuple(map(lambda x: 1 if x == "D" else (3 if x == "L" else int(x)), Input().split())) for _ in range(move_number)]
move_list = deque(move_list)

# MARK: - Game Start
second = 0
snake = [[0, 0]]
my_direction = 1

while True:
    nx = snake[-1][0] + direction[my_direction][0]
    ny = snake[-1][1] + direction[my_direction][1]
    second += 1

    if nx >= n or nx < 0 or ny >= n or ny < 0:
        print(second)
        break
    if [nx, ny] in snake and [nx, ny] != snake[-1]:
        print(second)
        break

    if space[nx][ny] == 1:
        snake.append([nx, ny])
        space[nx][ny] = 0
    else:
        snake.pop(0)
        snake.append([nx, ny])

    if move_list:
        if second == move_list[0][0]:
            my_direction = ((my_direction + move_list.popleft()[1]) % 4)



