import sys
from collections import deque

Input = sys.stdin.readline

n, m, k, x = map(int, Input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, Input().split())
    graph[a].append(b)


def bfs(graph,distance, start):
    distance[start] = 0
    q = deque([start])
    while len(q):
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                q.append(i)

bfs(graph,distance, x)

flag = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)