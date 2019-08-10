S = input()
flag = False
count0 = 0
count1 = 0
count2 = 0
count3 = 0
for i in S:
    if i == S[0]:
        count0 += 1
    if i == S[1]:
        count1 += 1
    if i == S[2]:
        count2 += 1
    if i == S[3]:
        count3 += 1

if count0==2 and count1 == 2 and count2 == 2 and count3 == 2:
    print('Yes')
else:
    print('No')