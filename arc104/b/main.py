n, s = tuple(input().split())
n = int(n)
total = 0
for start in range(n):
    d = {"A": 0, "T": 0, "C": 0, "G": 0}
    for end in range(start, n):
        d[s[end]] += 1
        if d['A'] == d['T'] and d['C'] == d['G']:
            total += 1

print(total)
