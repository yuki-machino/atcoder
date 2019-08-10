num = int(input())
difficulty = [int(i) for i in input().split()]
difficulty.sort()
K = 0
if difficulty[int(num/2)] != difficulty[int(num/2 - 1)]:
    K = difficulty[int(num/2)] - difficulty[int(num/2 - 1)]
else:
    K = 0
print (K)