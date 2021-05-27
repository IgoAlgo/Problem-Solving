# 처음 부여받은 번호 A, B -> 몇 번째 라운드에서 만나는 지 return
# 서로 붙게 되기 전까지 A, B는 항상 이긴다고 가정

# N = 8, A = 4, B = 7 (A의 숫자가 더 작다고 가정)
# 1 2 3 4 5 6 7 8 (4, 7) ... 1  (A의 번호, B의 번호)
# 1 2 3 4 (2, 4) ... 2
# 1, 2 (1, 2) ... 3 -> A의 번호가 홀수,  A의 번호 + 1 = B의 번호 -> 3 round에서 만남

import math


def solution(n, a, b):
    if a > b:
        a, b = b, a

    for round in range(1, n // 2 + 1):
        if a % 2 == 1 and a + 1 == b:
            return round
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)


# test
print(solution(8, 4, 7))