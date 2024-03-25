def find_count(left, right):
    print(left, right)
    count = 0
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l][0] > right[r][0]:
            res[left[l][1]] += 1
            count += 1
            r += 1
        elif left[l][0] <= right[r][0]:
            l += 1
            if l < len(left) - 1:
                res[left[l][1]] += count

    for i in range(l + 1, r):
        res[right[i][1]] += count

    l = 0
    r = 0
    count = 0

    while l < len(left) and r < len(right):
        if right[r][0] > left[l][0]:
            res[right[r][1]] += 1
            l += 1
            count += 1
        elif right[r][0] <= left[l][0]:
            r += 1
            if r < len(right) - 1:
                res[right[r][1]] += count

    for i in range(r + 1, l):
        res[left[i][1]] += count
    print("and the result", res)


def sort_strength(left, right):
    i = 0
    j = 0
    sorted_strength = []

    if left[0][0] > right[0][0]:
        sorted_strength.append(right[0])
        j += 1
    else:
        sorted_strength.append(left[0])
        i += 1

    sorted_strength.extend(left[i:])
    sorted_strength.extend(right[j:])

    return sorted_strength


def find_str(arr, le, ri):
    if ri == le + 1:
        return arr[le:ri]

    mid = (le + ri) // 2

    left = find_str(arr, le, mid)
    right = find_str(arr, mid, ri)

    find_count(left, right)
    arr = sort_strength(left, right)
    # print(res)

    # for i in range(len(left)):
    #     for j in range(len(right)):
    #         if left[i] > right[j]:
    #             res[i] += 1

    #         elif right[j] > left[i]:
    #             res[j + len(left)] += 1
    #     res[i] += left[i]

    # start = len(left)

    # for a in range(len(right)):
    #     res[a + start] += right[a]
    # res = [(x, i) for i, x in enumerate(res)]

    return arr


test = int(input())

for _ in range(test):
    n = int(input())
    res = [0] * 2**n
    strength = list(map(int, input().split()))
    strength = [(x, i) for i, x in enumerate(strength)]
    ans = find_str(strength, 0, 2**n)

    for i in range(len(ans)):
        res[ans[i][1]] += ans[i][0]
        # print(ans[i][1],ans[i] res)
    final = [str(x) for x in res]
    print(" ".join(final))
