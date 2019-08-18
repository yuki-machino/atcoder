import copy
f = open('input.txt', 'r')
N, M = map(int ,f.readline().split())
P = []
for i in range(N):
    P.append(int(f.readline()))
P.sort()
output = 0
if P[0] > M:
    output = M
else:
    P2 = []
    P3 = []
    P4 = []
    for i in range(N):
        if P[i] > M:
            with open('output.txt','w') as out:
                out.write(f"{max(P[i-1])}") 
                exit(0)
    P2 = copy.deepcopy(P)
    for p in P:
        for i in range(N):
            P2.append(p+P[i])
    P3 = copy.deepcopy(P2)
    for p in P:
        for i in range(N*N):
            P3.append(p+P2[i])
    P4 = copy.deepcopy(P3)
    for p in P: 
        for i in range(N*N*N):
            P4.append(p+P3[i])  
P4.sort()
for p in P4:
    if p > M:
        break
    else:
        output = p
with open('output.txt','w') as out:
    out.write(f"{output}")