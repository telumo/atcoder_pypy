X, K, D = map(int, input().split())

if abs(X) == D:
    print(X if K % 2 == 0 else 0)
elif abs(X / (K * D)) >= 1:
    print(abs(X - K * D))
else:
    count = abs(int(K * D / X))
    remaining_length = abs(X - count * D) if X > 0 else abs(X + count * D)
    remaining_count = K - count
    if remaining_count % 2 == 0:
        print(remaining_length)
    else:
        print(abs(remaining_length - D))
