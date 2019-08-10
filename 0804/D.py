S = input()
r = 0
l = 0
s = [0]*len(S)
for i in range(len(S)-1):
    if S[i] == 'R' and S[i+1] == 'L':
        r += 1
        s[i] += (r + 1) //2
        s[i+1] += r//2
        r = 0
    elif S[i] == 'R':
        r += 1
S = list(reversed(S))
s.reverse()
for i in range(len(S)-1):
    if S[i] == 'L' and S[i+1] == 'R':
        l += 1
        s[i] += (l + 1) //2
        s[i+1] += l//2
        l = 0
    elif S[i] == 'L':
        l += 1
s.reverse()
for i in s:
    print(i, end =' ' )
        

    
    