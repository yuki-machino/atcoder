import math
N,D=map(int,input().split())
points = []
num = 0
for n in range(N):
    p = [ int(i) for i in input().split()]
    points.append(p)

for i in range(len(points)):
    for j in range(len(points) - i - 1):
        sum = 0
        for k in range(D):
            sum += (points[i][k]-points[i+j+1][k])**2
        if float.is_integer(math.sqrt(sum)):
            num += 1
print(num)