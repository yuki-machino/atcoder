N = int(input())
a = 0
i = 1
while N//i != 0:
    if N//(i*10) != 0:
        a += i*10 - i
        i = i*100
    else:
        a += N - i +1
        i = i*100
print(a)
        