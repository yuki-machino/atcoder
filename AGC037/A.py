S = input()
count = 1
strings = []
strings.append(S[0])
stack = ''
for s in S[1:]:
    stack += s
    if strings[-1] == stack:
        continue
    else:
        strings.append(stack)
        stack = ''
        count+=1    

print(count)