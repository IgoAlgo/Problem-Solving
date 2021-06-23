def solution(s, basis):
    block = s.split(str(basis))  # change basis to '' in string. ex) "001100" -> ['','','11','','']
    return len(block) - block.count('')  # count the sequence number


s = input()
print(min(solution(s, 0),solution(s,1)))
