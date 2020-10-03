S = input()

yesterday = False
total = 0
for s in S:
    if s == "R":
        if yesterday:
            total += 1
        else:
            total = 1
        yesterday = True
    else:
        yesterday = False

print(total)
