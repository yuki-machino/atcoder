N = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(1,N+1):
    if p[i-1] != i:
        count += 1
    if count >2:
        print('NO')
        exit(0)
print('YES')


        