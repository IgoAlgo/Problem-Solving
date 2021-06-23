import sys

"""
빼거나 나눌 때 횟수의 최솟값 

test cases 

5 25 
"""


n, k = map(int, sys.stdin.readline().split())
ret = 0
while n != 1:
    temp = n % k
    if temp != 0:
        n -= temp
        ret += temp
    else:
        n //= k
        ret += 1

print(ret)
