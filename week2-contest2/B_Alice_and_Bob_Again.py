test = int(input())

for _ in range(test):
    ans = ""
    b = input()
    ans = b[:2]
    for i in range(2, len(b) - 1, 2):
        ans += b[i : i + 2][1]
    print(ans)
