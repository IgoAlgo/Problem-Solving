def dfs(num, target, path):
    if len(path) == 0:
        return 1 if num == target else 0

    return dfs(num + path[0], target, path[1:]) + dfs(num - path[0], target, path[1:])


def solution(numbers, target):
    count = 0

    count += dfs(0, target, numbers)

    return count


# test
print(solution([1, 1, 1, 1, 1], 3))
