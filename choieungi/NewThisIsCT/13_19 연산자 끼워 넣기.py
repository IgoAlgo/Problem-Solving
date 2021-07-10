import sys
from collections import deque

n = int(input())
data = list(map(int, input().split()))
add, sub, mal, div = map(int, input().split())

min_val = sys.maxsize
max_val = -sys.maxsize

def dfs(i, data, now):
    global min_val, max_val, add, sub, mal, div

    if i == n :
        min_val = min(min_val, now)
        max_val = max(max_val, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, data, now + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i + 1, data, now - data[i])
            sub += 1

        if mal > 0:
            mal -= 1
            dfs(i + 1, data, now * data[i])
            mal += 1

        if div > 0:
            div -= 1
            dfs(i + 1, data, int(now / data[i]))
            div += 1

dfs(1, data, data[0])

print(max_val)
print(min_val)