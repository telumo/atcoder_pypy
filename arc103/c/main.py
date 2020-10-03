n = int(input())
v = list(map(int, input().split()))

if len(set(v)) == 1:
    print(int(n / 2))
elif v[0] != v[1]:
    repeat = [v[0], v[1]] * int(n / 2)
    print(len(list(filter(lambda a: a[0] != a[1], list(zip(v, repeat))))))
else:
    # 1 1 1 3 1 3 1 3
    # 1 1 1 1 1 1 1 3
    pass
