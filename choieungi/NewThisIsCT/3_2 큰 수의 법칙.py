n, m, k = map(int, input().split())
data = (map(int, input().split()))
data.sort(reverse=True)

ret, cnt = 0, 0
for _ in range(m):
    if cnt != k:
        ret += data[0]
        cnt += 1
    else:
        ret += data[1]
        cnt = 0

print(ret)