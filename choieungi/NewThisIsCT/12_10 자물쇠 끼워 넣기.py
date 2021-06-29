def rotate(space, n, m):
    new_space = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_space[n - j - 1][i] = space[i][j]
    return new_space


def check(new_lock):
    l = len(new_lock) // 3
    for i in range(l, 2 * l):
        for j in range(l, 2 * l):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0] * 3 * m for _ in range(3 * m)]
    for i in range(m):
        for j in range(m):
            new_lock[m + i][m + j] = lock[i][j]

    for _ in range(4):
        key = rotate(key, n, n)
        for x in range(m * 2):
            for y in range(m * 2):
                for i in range(n):
                    for j in range(n):
                        new_lock[x + i][y + j] += key[i][j]
                # check lock
                if check(new_lock):
                    return True

                for i in range(n):
                    for j in range(n):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
