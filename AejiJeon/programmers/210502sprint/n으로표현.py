# 최솟값이 8보다 크면 -1을 return해야 함
# 즉, 숫자 n을 최대 8번까지 사용할 수 있다..!!
# 최솟값을 구해야 하니까
# 숫자를 1번 사용하는 경우부터 탐색..(1->2->...)
# 만약 number를 표현할 수 있는 경우를 찾는 순간 바로 return시키기
# 8번까지 시도 했는데 return이 안 된 경우는 -1을 return!

# N을 n개 사용해서 만들 수 있는 수는
# N을 n개 연속으로 붙여서 만들어지는 수(NNNN...N(i번 반복))와
# N을 j개 사용해서 만들 수 있는 숫자 op i - j개 사용해서 만들 수 있는 숫자들로 구성
# op(+, -, *, /), j=1,2,..., i-1

# 점화식
# s[i]: N을 i개 사용해서 만들 수 있는 수들의 집합이라고 하면
# s[i] = U(j = 1, 2, ..., i-1, op = +, -, *, /){s[j] op s[i-j]} U {NN...N(i번 반복)}


def solution(N, number):
    # i 번째 set은 N을 i개 사용해서 만들 수 있는 숫자들이 담겨짐
    s = [set() for i in range(9)]
    # N 숫자가 연속으로 i개 붙어있는 수들을 각 집합에 담아줌
    # ex) s[5]: N=7을 5개 사용해서 만들 수 있는 숫자들의 집합 -> 77777d을 넣어줌
    for i in range(1, 9):
        s[i].add(int(str(N) * i))

    # bottom up 방식으로 dp 알고리즘 수행
    for i in range(1, 9):
        # N을 i개 사용해서 만들 수 있는 숫자들은
        # 위에서 담아준 NNNN...N(i번 반복) 숫자와
        # N을 j개 사용해서 만들 수 있는 숫자 op i - j개 사용해서 만들 수 있는 숫자로 나타낼 수 있음
        # op(+, -, *, /), j=1,2,..., i-1
        for j in range(1, i):
            for a in s[j]:
                for b in s[i - j]:
                    s[i].add(a + b)
                    s[i].add(a - b)
                    s[i].add(a * b)
                    if b != 0:
                        s[i].add(a // b)
        # s[i] 집합에 들어갈 모든 원소들을 집어 넣은 후
        # number가 s[i]에 있으면(N을 i개 사용해서 number을 표현할 수 있음)
        # i(N 사용 횟수의 최솟값) return
        if number in s[i]:
            return i
    # N을 최대 8개 사용해서도 number을 만들 수 없는 경우
    return -1


print(solution(5, 12))
print(solution(2, 11))