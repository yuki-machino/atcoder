A, B = map(int,input().split())
K = (A+B) / 2
if float.is_integer(K):
    print(int(K))
else:
    print('IMPOSSIBLE')
