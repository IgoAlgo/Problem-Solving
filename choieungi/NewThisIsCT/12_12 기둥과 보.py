def check_possible(ans):
    for x, y, installed in ans:
        if installed == 0:
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                continue

            return False

        elif installed == 1:
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 0:
            answer.remove([x, y, stuff])
            if not check_possible(answer):
                answer.append([x, y, stuff])

        elif operate == 1:
            answer.append([x, y, stuff])
            if not check_possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)