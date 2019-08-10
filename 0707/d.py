N = int(input())
pool = [int(i) for i in input().split()]
sum = 0
sub = 0
for i in range(len(pool)):
    sum += pool[i]
sum = sum/2    
sub = sum
for i in range(0,N-1,2):
    sub -= pool[i]
a = pool[N-1]-sub
print(int(a)*2)
for i in range(len(pool)-1):
    print(int(pool[i]-a)*2)
    a = pool[i]-a