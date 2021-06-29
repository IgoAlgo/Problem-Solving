def solution(s):
    answer = len(s)
    l = len(s)
    for step in range(1, l // 2 + 1):
        cnt = 1
        compressed = ""
        prev = s[0:step]
        for i in range(step, l, step):
            if s[i:i + step] == prev:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt > 1 else prev
                prev = s[i: i + step]
                cnt = 1
        compressed += str(cnt) + prev if cnt > 1 else prev

        answer = min(answer, len(compressed))

    return answer