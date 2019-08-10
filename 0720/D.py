N = int(input())
A = [int(i) for i in input().split()]
for i in range(N//2 + 1):
    j = N//2 - i + 1
    su = 0
    if A[j] == 1:
        for k in range(N//j):
            su += A[k*j + j-1]
        if su == 1:
            A[j] = 0
        elif su > 1:
            print(-1)
            exit(1)
    elif A[j] == 0:
        for k in range(N//j):
            su += A[k*j + j-1]
        if su > 1:
            print(-1)
            exit(1)

print(sum(A))
for i in range(N):
    if A[i] == 1:
        print(i+1, end =' ')
print()
    