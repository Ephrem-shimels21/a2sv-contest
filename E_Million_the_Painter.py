n = int(input())
segment = list(input())

pre = ""
last = ""
c_count = 0
b_similar = 0
if segment[0] == "?":
    b_similar += 1
if segment[-1] == "?":
    b_similar += 1
for i in range(len(segment) - 1):
    if segment[i] != "?" and segment[i] == segment[i + 1]:
        print("NO")
        break
    elif segment[i + 1] == "?" and segment[i] != "?":
        pre = segment[i]
    elif segment[i] == "?" and segment[i + 1] != "?":
        last = segment[i + 1]
        if pre == last:
            b_similar += 1
    elif segment[i] == "?":
        c_count += 1
else:
    if b_similar > 0 or c_count > 0:
        print("YES")
    else:
        print("NO")
