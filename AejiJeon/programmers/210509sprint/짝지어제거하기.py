def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        # 짝이 있는 경우 -> stack에서 제거
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    # stack이 빈 경우 -> 모든 문자들이 제거 됨
    return 1 if not stack else 0


# test
print(solution("baabaa"))
print(solution("cdcd"))
