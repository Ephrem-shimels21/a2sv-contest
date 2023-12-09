test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    num_i = {}

    for idx, num in enumerate(arr):
        if num - idx in num_i:
            count += num_i[num - idx]
        num_i[num - idx] = 1 + num_i.get(num - idx, 0)
    print(count)
