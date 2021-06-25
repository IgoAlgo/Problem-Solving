import heapq


def solution(food_times, k):
    if sum(food_times) <= k: return -1

    idx_food_times = [[food, idx + 1] for idx, food in enumerate(food_times)]
    heapq.heapify(idx_food_times)
    previous, sum_val = 0, 0
    length = len(idx_food_times)

    while True:
        if (idx_food_times[0][0] - previous) * length <= k - sum_val:
            food_time = heapq.heappop(idx_food_times)[0]
            sum_val += (food_time - previous) * length
            previous = food_time
            length -= 1

        else:
            ret = sorted(idx_food_times, key=lambda x: x[1])
            return ret[(k - sum_val) % len(idx_food_times)][1]


print(solution([8,6,4], 15))