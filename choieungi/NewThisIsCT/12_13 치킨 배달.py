import sys
from itertools import combinations

Input = sys.stdin.readline

n, m = map(int, Input().split())
space = [Input().split() for _ in range(n)]
chicken = []
home = []


def min_distance(case, home):
    ans = 0
    for p,q in home:
        distance = int(1e9)
        for x,y in case:
            distance = min(distance, abs(p-x)+abs(q-y))
        ans += distance
    return ans


for i in range(n):
    for j in range(n):
        if space[i][j] == '1': home.append((i,j))
        elif space[i][j] == '2': chicken.append((i,j))

answer = int(1e9)
for case in combinations(chicken, m):
    answer = min(answer, min_distance(case, home))

print(answer)


