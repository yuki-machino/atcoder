K,S = map(int, input().split())
count = 0
for i in range(K,-1,-1):
    if i <= S:
        z = i
        sum_xy = S - i
        for j in range(K, -1,-1):
            if j <= sum_xy:
                y = j
                if sum_xy - j <= K:
                    count += 1
    else:
        continue
print(count)