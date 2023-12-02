n = int(input())

n_odds = []
n_evens = []

nums = list(map(int, input().split()))

for num in nums:
    if num % 2 == 0:
        n_evens.append(num)
    else:
        n_odds.append(num)
res = 0

if len(n_odds) > 0 and len(n_odds) % 2 == 0:
    res += sum(n_odds)
else:
    n_odds.sort(reverse=True)
    res += sum(n_odds[: len(n_odds) - 1])

if n_evens:
    res += sum(n_evens)

print(res)
