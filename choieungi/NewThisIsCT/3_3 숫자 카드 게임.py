import sys

"""
이차원 배열에서 각 행의 최솟값들 중 최댓값을 찾는 문제 

test cases 

3 3
3 1 2 
4 1 4
2 2 2

"""

n, m = map(int, sys.stdin.readline().split())
data = iter(map(int, sys.stdin.readline().split()) for _ in range(n))

print(max(map(min, data)))


"""
map(func, iterator)-> iterator의 값들을 func에 적용한 iterator을 return , max -> iterator 중 max
iterator? -> 값을 하나씩 꺼낼 수 있는 객체 , 매직 메서드인 next를 통해 pop 가능 ,


print(max(map(max, data))) # -> 이차원 배열 최댓값, 최댓값 중 최댓값
print(max(map(min, data))) # -> 행의 최솟값 중 최댓값
print(min(map(max, data))) # -> 행의 최댓값 중 최솟값
print(min(map(min, data))) # -> 이차원 배열 최솟값, 최솟값 중 최솟값 

"""


