from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(graph, start, visited):
        visited[start] = True
        for i in range(n):
            if not visited[i] and graph[start][i]:
                dfs(graph, i, visited)

    def bfs(graph, start, visited):
        visited[start] = True
        q = deque([start])
        while len(q):
            v = q.popleft()
            for i in range(n):
                if not visited[i] and graph[v][i]:
                    q.append(i)
                    visited[i] = True

    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))