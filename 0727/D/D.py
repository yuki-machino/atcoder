S = input()
head = 0
skip_head = True

for i, s in enumerate(S):
    
    if s == '0' and skip_head:
        continue:
    else:
        skip_head = False
        head = i
        total += (10**len(S) - 1 - 5)//13 + 1
        
    if s = '?':
        total += (10**len(S) - 1 - 5)//13 + 1
    else:
        if len(S) > 2:
            total += (int(s) * 10**(len(S)-1) + ((10**(len(S)-1) -1) ) + 5) // 13 + 1 # (x999... -5)//13 + 1 
            total -= (int(s) * 10**(len(S)-1) + 5 ) // 13 + 1 # (x999... +5)-(x000.... -5)// 13 + 1 
    


                
print(result%(10**9+7))