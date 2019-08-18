N,Y = map(int,input().split())
x = y = z = 0
for i in range(N,-1,-1):
    if i*10000 <= Y:
        charge = Y - i*10000
        rest = N - i
        for j in range(rest,-1,-1):
            if j*5000 <= charge:
                if charge - j*5000 - (rest-j)*1000 == 0:
                    print('{0} {1} {2}'.format(i, j ,rest-j))
                    exit(0)
print('-1 -1 -1')
