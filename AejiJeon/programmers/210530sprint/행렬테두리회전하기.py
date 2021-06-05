def solution(rows, columns, queries):
    result = []
    matrix = [[] for _ in range(rows)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i - 1].append((i - 1) * columns + j)

    for x1, y1, x2, y2 in queries:
        # (x1, y1) 숫자 저장
        temp = matrix[x1 - 1][y2 - 1]
        min_value = int(1e9)

        # 위쪽
        min_value = min(min(matrix[x1 - 1][y1 - 1 : y2 - 1]), min_value)
        matrix[x1 - 1][y1:y2] = matrix[x1 - 1][y1 - 1 : y2 - 1]

        # 왼쪽
        for i in range(x1, x2):
            min_value = min(matrix[i][y1 - 1], min_value)
            matrix[i - 1][y1 - 1] = matrix[i][y1 - 1]

        # 아래쪽
        min_value = min(min(matrix[x2 - 1][y1:y2]), min_value)
        matrix[x2 - 1][y1 - 1 : y2 - 1] = matrix[x2 - 1][y1:y2]

        # 오른쪽
        for i in range(x2 - 2, x1 - 2, -1):
            min_value = min(matrix[i][y2 - 1], min_value)
            matrix[i + 1][y2 - 1] = matrix[i][y2 - 1]

        matrix[x1][y2 - 1] = temp
        min_value = min(min_value, temp)

        result.append(min_value)

    return result