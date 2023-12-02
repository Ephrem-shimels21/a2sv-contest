test = int(input())

for _ in range(test):
    strr = input()

    if len(strr) > 10:
        print(strr[0] + str(len(strr) - 2) + strr[-1])
    else:
        print(strr)
