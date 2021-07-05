import sys
from collections import deque

from typing import List, Any

Input = sys.stdin.readline

n, m, start = map(int, Input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
for _ in range(m):
    p, q = map(int, Input().split())
    graph[p].append(q)
    graph[q].append(p)


def recursion_dfs(graph, visited, start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            recursion_dfs(graph, visited, i)


def stack_dfs(graph, start):
    ans = []  # type: List[Any]
    visited = [False] * (n + 1)
    stack = [start]
    while len(stack):
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.extend(sorted(graph[v], reverse=True)) # 깊이가 같을 시, 번호가 낮은 노드를 우선 탐색
            ans.append(v)
    print(*ans)


def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print (v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


recursion_dfs(graph,visited,start)
print()
stack_dfs(graph,start)

bfs(graph,bfs_visited,start)