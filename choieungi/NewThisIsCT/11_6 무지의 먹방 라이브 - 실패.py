from collections import deque
def solution(food_times, k,):
    idx_food_times = deque([food, idx+1] for idx, food in enumerate(food_times))
    # idx_food_times.rotate(1)
    # print(idx_food_times)
    while k != 0:
        idx_food_times.rotate(1)
        if idx_food_times[0][0]:
            idx_food_times[0][0] -= 1
            k -= 1
    print(idx_food_times)
    return idx_food_times[0][1]


print(solution([3,1,2], 5))