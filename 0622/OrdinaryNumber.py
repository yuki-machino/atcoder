num = int(input())
numbers = [ int(i) for i in input().split()]
count = 0
for i in range(len(numbers)):
    if i == 0:
        continue
    elif i == num-1:
        continue
    else:
        if numbers[i] < numbers[i-1] and numbers[i] > numbers[i+1]:
            count +=1
        elif numbers[i] > numbers[i-1] and numbers[i] < numbers[i+1]:
            count +=1
print(count)