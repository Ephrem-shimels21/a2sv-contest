test = int(input())

string = "codeforces"

for _ in range(test):
    letter = input()
    if letter in string:
        print("YES")
    else:
        print("NO")
