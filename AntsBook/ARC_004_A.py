import math
N = int(input())
x = []
y = []
max_distance = 0
for i in range(N):
    temp_x, temp_y = map(int , input().split())
    x.append(temp_x)
    y.append(temp_y)
for i in range(N):
    for j in range(N):
        if i != j:
            max_distance = max(max_distance,(x[i]-x[j])**2+(y[j]-y[i])**2)
print(math.sqrt(max_distance))

