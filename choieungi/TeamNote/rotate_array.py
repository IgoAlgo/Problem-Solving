# rotate left n*m array

def rotate(space, n, m):
    new_space = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_space[n-j-1][i] = space[i][j]
    return new_space


test_space = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

return_val = rotate(test_space,len(test_space), len(test_space[0]))

for i in return_val:
    print (i)
"""
[3, 6, 9]
[2, 5, 8]
[1, 4, 7]
"""
