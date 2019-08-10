N,M = map((int),input().split())
nodes = []
results = []
for i in range(N):
    nodes.append([])
for i in range(N):
    resuts.append([])
for i in range(M):
    A,B=map((int),input().split())
    nodes[A-1].append(B)
    nodes[B-1].append(A)

    
        
