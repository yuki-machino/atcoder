L, R = map(int, input().split())
l_mod = L % 2019
r_mod = R % 2019
if R >2019+L:
    print(0)
else:
    mod = (l_mod*(l_mod+1)) % 2019
    for i in range(l_mod,r_mod):
        for j in range(i+1,r_mod+1):
            if mod>(i*j)%2019:
                mod=(i*j)%2019
    print(mod)