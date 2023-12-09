test = int(input())
cmp = "codeforces"

cmp_d = {}

for idx, letter in enumerate(cmp):
    cmp_d[idx] = letter

for _ in range(test):
    count = 0
    str1 = input()
    for idx, letter in enumerate(str1):
        if cmp_d[idx] != letter:
            count += 1
    print(count)
