test = int(input())

for _ in range(test):
    n, h = map(int, input().split())
    max_he = 0

    for _ in range(n):
        w, l = map(int, input().split())
        max_he += max(w, l)

    if max_he >= h:
        print("YES")
    else:
        print("NO")
