def solution(n):
    # d[i]: 2xi의 직사각형에 타일을 까는 경우의 수
    # d[i] = d[i-1] + d[i-2] 
    # i 번째에 세로 타일을 까는 경우 + i-1 ~ i에 가로 타일 2장을 깨는 경우
    d = [0] * (n + 1)
    d[1] = 1
    if n >= 2:
        d[2] = 2
    if n >= 3:
        for i in range(3, n + 1):
            d[i] = d[i-1] + d[i-2]
    return d[n]