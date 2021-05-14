# continuous graph에 대해서만 적용됨
from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n)]
    for a, b in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    INF = 1e9
    # 1번 노드부터 다른 노드까지의 최단 거리를 담는 array
    distance = [INF] * n
    distance[0] = 0

    # bfs 알고리즘을 사용하여 최단 거리 구하기
    queue = deque()
    queue.append(0)
    while queue:
        now = queue.popleft()
        for adj in graph[now]:
            if distance[adj] == INF:
                distance[adj] = distance[now] + 1
                queue.append(adj)
    print(distance)
    # count = 0
    # max_value = max(distance)
    # for i in range(n):
    #     if max_value == distance[i]:
    #         count += 1

    # array에서 최댓값을 갖는 element 개수 구하기
    return distance.count(max(distance))


# test
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))