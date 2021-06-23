import sys

"""
시각 

N시 59 59 까지 3의 개수

5
"""

n = int(input(''))
cnt = 0
for i in range(n+1):
    for j in range(60):
        for w in range(60):
            _time = ("%02d%02d%02d" % (i, j, w))
            if '3' in _time:
                cnt += 1

print(cnt)