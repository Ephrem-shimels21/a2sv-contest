import math


def find_wagon(demand, time):
    l = 1
    r = max(demand)
    min_wag = float("inf")

    while l <= r:
        mid = (l + r) // 2

        curr_time = 0
        for i in range(len(time)):
            amount = math.ceil(demand[i] / mid)
            curr_time += amount * time[i]
        if curr_time <= k:
            min_wag = min(min_wag, mid)
            r = mid - 1
        else:
            l = mid + 1

    if min_wag == float("inf"):
        return -1
    return min_wag


test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    demand = list(map(int, input().split()))
    time = list(map(int, input().split()))

    print(find_wagon(demand, time))
