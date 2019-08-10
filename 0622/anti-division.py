A, B, C, D = map((int), input().split())
LCM = 0
for i in range(max(C,D),C*D+1):
    if i % C == 0 and i % D == 0:
        LCM = i
        print("LCM={0}".format(LCM))
        break

A_c = (A-1)//C
B_c = B//C

A_d = (A-1)//D
B_d = B//D

A_lcm = (A-1)//LCM
B_lcm = B//LCM


AB_c = B_c-A_c
AB_d = B_d-A_d
AB_lcm = B_lcm-A_lcm

output = B - (A-1) -(AB_c + AB_d - AB_lcm)
print(output)




