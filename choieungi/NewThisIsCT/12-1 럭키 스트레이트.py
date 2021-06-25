s = [*map(int, input())]
l = len(s)//2
print("READY"if sum(s[:l])-sum(s[l:])else"LUCKY")