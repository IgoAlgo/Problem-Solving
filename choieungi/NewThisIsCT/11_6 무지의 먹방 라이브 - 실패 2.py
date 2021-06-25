import heapq

def solution(food_times, k,):
    idx_food_times = [[food, idx+1] for idx, food in enumerate(food_times)]
    heapq.heapify(idx_food_times)
    # food_time, idx = heapq.heappop(idx_food_times)
    # print(list(map(lambda x: [x[0] - food_time, x[1]], idx_food_times)))

    while True:
        print(idx_food_times, k)
        if idx_food_times[0][0] * len(idx_food_times) <= k:
            k -= idx_food_times[0][0] * len(idx_food_times)
            food_time, idx = heapq.heappop(idx_food_times)
            idx_food_times = map(lambda x: [x[0] - food_time, x[1]], idx_food_times)
            idx_food_times = list(filter(lambda x: x[0] != 0, idx_food_times))
            #print (idx_food_times)
        else:
            idx_food_times.sort(key = lambda x: x[1])
            return idx_food_times[(k)%len(idx_food_times)][1]



print(solution([8,6,4], 15))