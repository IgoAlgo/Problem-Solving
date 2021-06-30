a = [[0,2],[5,6]]

b = [1,2]

print(list(map(lambda x: [x[0][0],x[0][1],x[1]], zip(a,b))))