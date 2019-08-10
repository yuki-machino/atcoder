import copy
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
B = sorted(A,reverse=True)
for a in A:
    if a < B[0]:
        print(B[0])    
    else:
        print(B[1])    