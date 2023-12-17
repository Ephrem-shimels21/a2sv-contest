test = int(input())


for _ in range(test):
    arr = list(map(int, input().split()))
    n = len(arr)
    kene = arr[0]
    # arr.sort()

    # idx = arr.index(kene)

    # print(n - (idx + 1))

    count = 0
    for num in arr[1:]:
        if num > kene:
            count += 1
    print(count)
