import sys
from collections import deque

Input = sys.stdin.readline

n, target = map(int, Input().split())
MAX = 100001
space = [0]*MAX

def bfs(start):
    cnt = 0
    q = deque([start])

    while len(q):
        idx = q.popleft()
        for i in range(3):
            num = 0
            if i == 0:
                num = idx + 1
            elif i == 1:
                num = idx - 1
            elif i == 2 :
                num = idx * 2

            if num < 0 or num >= MAX:
                continue

            if space[num] != 0:
                continue

            q.append(num)
            space[num] = space[idx] + 1

            if num == target :
                print(space)
                return space[num]



if n > target:
    print(n-target)

elif n == target:
    print(0)

else:
    print(bfs(n))

