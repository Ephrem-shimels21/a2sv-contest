test = int(input())


for _ in range(test):
    ln, m = map(int, input().split())
    decr = list(input())
    w = list(input())
    total_w = 0

    for c in w:
        total_w += ord(c)

    l = 0
    window = 0

    for i in range(m):
        window += ord(decr[i])

    for r in range(m, ln):
        if window == total_w:
            print("YES")
            break
        window -= ord(decr[l])
        window += ord(decr[r])
        l += 1

    else:
        if window == total_w:
            print("YES")
        else:
            print("NO")
