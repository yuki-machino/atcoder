N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
beat = 0
for i in range(N+1):
    if i == 0:
        if A[i] < B[i]:
            beat += A[i]
            B[i] -= A[i]
        else:
            beat += B[i]
            B[i] = 0
    elif i == N:
        if A[i] <= B[i-1]:
            beat += A[i]
            B[i-1] -= A[i]
        else:
            beat += B[i-1]
    else:
        if A[i] <= B[i-1]:
            beat += A[i]
            B[i-1] -= A[i]
        elif A[i] - B[i-1] <= B[i]:
            beat += A[i]
            B[i] -= (A[i] - B[i-1])
        else:
            beat += B[i-1] + B[i]
            B[i] = 0
print(beat) 

    