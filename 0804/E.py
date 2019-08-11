def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
total = sum(A)
divisors = make_divisors(total)
divisors.sort()
divisors.reverse()
original_K = K

for d in divisors:
    rest = []
    k = K = original_K
    for a in A:
        if a % d < d/2:
            if a % d < K:
                rest.append(0)
                K -= a % d
            elif K > 0:
                if d - (a % d - K) <= k:
                    k -= (d - (a % d - K))
                    rest.append(0)
                    K = 0
                elif d - (a % d - K) > k:
                    rest.append((a % d - K) + k)
                    k = 0
                    K = 0    
            elif K == 0:
                if d - (a % d) <= k:
                    k -= (d - (a % d))
                    rest.append(0)
                elif d - (a % d) > k:
                    rest.append((a % d) + k)
                    k = 0
        else:
            if d - (a % d) <= k:
                k -= (d - (a % d))
                rest.append(0)
            elif d - (a % d) > k and K == 0:
                rest.append((a % d) + k)
                k = 0
            else:
                if (a % d) + k <= K:
                    rest.append(0)
                    K -= (a % d) + k 
                    k = 0
                else:
                    rest.append((a % d) + k- K)
                    K = 0
    
    if sum(rest) <= 7:
        if k == 0:
            print(d)
        elif (k - K) % d  == 0:
            print(d)
        exit(0)        
        
            
    
