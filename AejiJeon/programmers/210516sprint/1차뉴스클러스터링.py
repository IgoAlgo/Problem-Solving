# J(A, B) = n(A & B) / n(A | B)
# A is empty and B is empty -> J(A, B) = 1

# 다중집합

# return -> int ( J(A, B) * 65536 )

# 알파벳 대문자, 소문자 구별 x

# python collections 모듈이 Counter 함수 사용

# example
# Counter(A) = Counter({1: 2, 2: 2, 3: 1}) Counter(B) = Counter({1: 1, 2: 2, 4: 1, 5: 1})
# Counter(A) & Counter(B) = Counter({1: 1, 2: 2})
# Counter(A) | Counter(B) = Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1})


from collections import Counter


def solution(str1, str2):

    str1_arr = []
    str2_arr = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_arr.append((str1[i] + str1[i + 1]).lower())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_arr.append((str2[i] + str2[i + 1]).lower())

    # 공집합인 경우 J(A, B) = 1
    # return int(1* 65536)
    if not str1_arr and not str2_arr:
        return 65536

    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)

    intersect_num = len(list((counter1 & counter2).elements()))
    union_num = len(list((counter1 | counter2).elements()))

    return int((intersect_num / union_num) * 65536)


# test
print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))