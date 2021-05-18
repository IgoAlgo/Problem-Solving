# a 원소 1개인 집합 s1  -> a
# 원소 2개인 집합 s2 에서 s2 - s1 = {b} -> a b
# 원소 3개인 집합 s3 에서 s3 - s2 = {c} -> a b c

# string 집합을 어떻게 나누지


def solution(s):
    # s에서 양 끝 '{' '}' 제거
    s = s[1:-1]

    set_arr = []
    temp_set = set()
    temp_str = ""

    # string으로 표현된 집합의 원소(집합)들을 set_arr 배열에 담아줌
    for c in s:
        # 해당 숫자가 포함된 수를 만들어 줌
        if c.isdigit():
            temp_str += c
        # ',' 바로 전에 '}'이 아닌 숫자가 나오는 경우
        # temp_set 집합에 넣어줌
        elif c == "," and temp_str:
            temp_set.add(int(temp_str))

            temp_str = ""
        # '}' 전의 숫자를 temp_set 집합에 넣어줌
        elif c == "}":
            temp_set.add(int(temp_str))
            set_arr.append(temp_set)
            temp_str = ""
            temp_set = set()
    # 집합의 원소 수가 적은 순서대로 정렬
    set_arr.sort(key=lambda x: len(x))
    answer = []

    diff_set = set()

    # set_arr에서 인접해 있는 집합들의
    # 차집합에 속해있는 숫자를 하나씩 넣어줌
    for _set in set_arr:

        answer.append(list(_set - diff_set)[0])
        diff_set = _set

    return answer


# test
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))