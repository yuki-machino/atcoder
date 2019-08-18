N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
count =0
i = B.index(max(B))
while B != A: 
    if max(B) < max(A):
        count =-1
        break
    
    if i+1 >= N:
        while B[i] > B[i-1] and B[i] > B[0] :
            B[i] = B[i] - B[0] - B[i-1]
            count += 1
            if B == A:
                break
    else:
        while B[i] > B[i-1] and B[i] > B[i+1] :
            B[i] = B[i] - B[i+1] - B[i-1]
            count += 1
            if B == A:
                break
    i = i+1
    if i == N:
        i = 0
    
    
print(count)