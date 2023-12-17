test = int(input())
s = "Yes" * 50
for _ in range(test):
    substring = input()

    if substring in s:
        print("YES")
    else:
        print("NO")
