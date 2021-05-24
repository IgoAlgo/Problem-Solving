# graph is represented in adjacent matrix -> find the number of connected components
from collections import deque

# explores all nodes of a connected component
def bfs(graph, visited, start, n):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in range(n):
            if graph[now][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        # find connected component
        if not visited[i]:
            # explores all nodes of the component
            bfs(computers, visited, i, n)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))