"""
게임 개발

test codes
4 4 
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1

output
3
"""

import sys

# input
_input = sys.stdin.readline
n, m = map(int, _input().split())
check = [[0] * m for _ in range(n)]  # space for check
x, y, direction = map(int, _input().split())

# data for ps
space = [list(map(int, _input().split())) for _ in range(n)]
move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # up right down left
check[x][y] = 1  # check my location
cnt = 0  # check for 4 times
ans = 1  # count answer

while True:
    """
    # debugging code 
    
    for i in check:
        print(i)
    print(x, y, direction)
    print()
    """
    left = (direction+3) % 4  # direction to turn left
    nx, ny = x + move[left][0], y + move[left][1]

    # requirement for 2
    if not check[nx][ny] and not space[nx][ny]:  # If the place is not visited and can go, go ahead.
        check[nx][ny] = 1
        x, y = nx, ny
        direction = left
        ans += 1
        cnt = 0
        continue

    elif (check[nx][ny] or space[nx][ny]) and cnt != 4:  # If I visited or can't go, turn left
        direction = left
        cnt += 1
        continue

    # requirement for 3
    if cnt == 4:  # if I can't go and visited for four direction, go back with maintaining the direction.
        temp_direction = (direction + 2) % 4  # It is
        nx, ny = x + move[temp_direction][0], y + move[temp_direction][1]

        if space[nx][ny]:  # if I can't go because backward is sea(can't go), then break and return the answer.
            break

        # If we can go backward, so go back (backward must be that we visited so just need to move)
        x, y = nx, ny
        cnt = 0

print(ans)
