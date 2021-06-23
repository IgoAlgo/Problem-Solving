s = list(map(int, input())) # change string to int list

def check_str(s, find):
    idx = 0
    cnt = 0
    flag = False
    while True:
        if idx == len(s): return cnt

        if s[idx] is not find :
            flag = False
            idx += 1

        elif s[idx] == find and not flag:
            idx += 1
            flag = True
            cnt += 1

        elif s[idx] == find and flag:
            idx += 1

print(min(check_str(s, 0), check_str(s, 1)))