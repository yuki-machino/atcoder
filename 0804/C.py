N = int(input())
H = [int(i) for i in input().split()]
H.reverse()
for i in range(len(H)-1):
    if H[i]+1 < H[i+1]:
        print('No')
        exit(0)
    if H[i]+1 == H[i+1]: 
        H[i+1] -= 1
print('Yes')
    