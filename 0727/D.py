S = input()
all_remains = [0]*13
for digits, s in enumerate(S[::-1]):
    temp_remains = [0]*13     
    if s == '?':
        if digits == 0:
            for i in range(10):
                temp_remains[i % 13] += 1
        else:
            for i in range(10):
                r = i * (10**digits) % 13
                for j in range(13):
                    temp_remains[ (j + r) % 13] += all_remains[j]
    else:
        if digits == 0:
                temp_remains[int(s)] += 1
        else:
            n = int(s)*(10**digits) % 13
            for j in range(13):
                temp_remains[(j + n) % 13] += all_remains[j]
    all_remains = temp_remains
print(all_remains[5]%(10**9+7))
