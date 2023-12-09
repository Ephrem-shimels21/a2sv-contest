from collections import defaultdict


test = int(input())

for _ in range(test):
    indxes = defaultdict(lambda: [])
    n = int(input())
    arr = list(map(int, input().split()))
    for index, num in enumerate(arr):
        indxes[num].append(index)
    for key, val in indxes.items():
        if len(val) > 1 and val[-1] - val[0] > 1:
            print("YES")
            break
    else:
        print("NO")
"""
{
    1: [2, 4, 5],
    2: [1, 3]    


}

is dic[num] > 1
arr[-1] - arr[0] > 1 // not neighbours


1 2 2 3 2
{
    1: [0],
    2: [1, 2, 4],
    3: [3]
}
"""


# for _ in range(test):
#     length = int(input())
#     num = "".join(input().split())

#     for idx, num_str in enumerate(num):
#         if num_str in num[idx + 1 :]:
#             occ_idx = num[idx + 1 :].index(num_str) + idx + 1
#             if (occ_idx - idx + 1 >= 3
#                 and num[idx : occ_idx + 1] == num[idx : occ_idx + 1][::-1]
#             ):
#                 print("YES")
#                 break
#     else:
#         print("NO")


# def reversing(numm):
#     numm_i = int(numm)
#     ans = ""

#     while numm_i:
#         re = numm_i % 10
#         ans += str(re)
#         numm_i = numm_i // 10
#     return ans


# for _ in range(test):
#     length = int(input())
#     num = "".join(input().split())

#     i, j = 0, 2
#     printed = False
#     while j <= length and i < len(num) - 2:
#         id1, id2 = j - length, i - length - 1
#         if num[i : j + 1] == (num[id1:id2]):
#             print("YES")
#             printed = True
#             break
#         else:
#             k = j
#             while k < len(num):
#                 ik1, ik2 = k - length, i - length
#                 if num[i : k + 1] == (num[ik1:ik2]):
#                     print("YES")
#                     printed = True
#                     break
#                 k += 1
#         i += 1
#         j += 1
#     if not printed:
#         print("NO")


# for _ in range(test):
#     n = int(input())
#     num_idx = {}
#     arr = "".join(input().split())
#     for idx, num in enumerate(arr):
#         idx_list = num_idx.get(num, [])
#         idx_list.append(idx)
#         num_idx[num] = idx_list
#     # print(num_idx)
#     for key in num_idx:
#         printed = False
#         for id in num_idx[key]:
#             for id2 in num_idx[key][1:]:
#                 if id2 - id >= 2 and arr[id : id2 + 1] == arr[id : id2 + 1][::-1]:
#                     print("YES")
#                     printed = True
#                     break
#         if printed:
#             break
#     else:
#         print("NO")
