test = int(input())

for _ in range(test):
    n = int(input())
    strr = input()
    res = ""
    count = 0
    idx = 0
    pairs = set()

    while idx < n:
        if strr[idx : idx + 2] in pairs:
            idx += 2
            res += strr[idx : idx + 2]
        else:
            res += strr[idx]
            pairs.add(res[idx - 1 : idx + 1])
            idx += 1
        count += 1
        # print(res)

    # print(count, n)
    if count < n:
        print("YES")
    else:
        print("NO")
