from collections import deque

# 0 <= minute
def add_minutes(time, minute):
    # "09:00" + 59분

    h, m = time.split(":")
    # 9
    h = int(h)
    # 0
    m = int(m)

    m = m + minute

    h = (h + m // 60) % 24
    m = m % 60

    # "09: 59"
    return "{0:02d}:{1:02d}".format(h, m)


# 0 <= minute < 60
def sub_minutes(time, minute):
    # "09:00" - 25 분

    h, m = time.split(":")
    # 9
    h = int(h)
    # 0
    m = int(m)

    m = m - minute
    if m < 0:
        h -= 1
        m += 60

    if h == -1:
        h = 23

    # "08: 40"
    return "{0:02d}:{1:02d}".format(h, m)


# return true if time1 <= time2 else false
def time_comparator(time1, time2):
    h1, m1 = time1.split(":")
    h2, m2 = time2.split(":")

    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    return True if h1 < h2 or (h1 == h2 and m1 <= m2) else False


def solution(n, t, m, timetable):
    # sorting
    timetable.sort(key=lambda x: (int(x.split(":")[0]), int(x.split(":")[1])))
    timetable = deque(timetable)

    bus_times = [add_minutes("09:00", t * i) for i in range(n)]
    people_in_bus = [[] for _ in range(n)]

    for i, time in enumerate(bus_times):
        if not timetable:
            break
        # time_comparator 사용
        while (
            timetable
            and time_comparator(timetable[0], time)
            and len(people_in_bus[i]) < m
        ):
            people_in_bus[i].append(timetable.popleft())

    # 맨 마지막에 도착하는 버스에 크루들이 탑승한 후에도 버스가 빈 경우
    if len(people_in_bus[n - 1]) < m:
        return bus_times[n - 1]
    # 맨 마지막에 도착하는 버스에 크루들이 탑승한 후에 버스가 꽉 찬 경우
    else:
        return sub_minutes(people_in_bus[n - 1][-1], 1)


# test

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(
    solution(
        10,
        60,
        45,
        [
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)
