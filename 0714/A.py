N = int(input())
a = [int(i) for i in input().split(' ')]
numbers = []
numbers.append(a[0])
for i in a:
    if i != numbers[0] and len(numbers) == 1:
        numbers.append(i)
    if i != numbers[0] and i != numbers[1]:
        numbers.append(i)
        break

if len(numbers) == 1:
    if numbers[0] == 0:
        print('Yes')
        exit(0)
    else:
        print('No')
        exit(0)

if len(numbers) == 3:
    if a.count(numbers[0]) != a.count(numbers[1]):
        print('No')
        exit(0)
    if a.count(numbers[0]) != a.count(numbers[2]):
        print('No')
        exit(0)
    if len(a) != a.count(numbers[0])+a.count(numbers[1])+a.count(numbers[2]):
        print('No')
        exit(0)

    if numbers[0]^numbers[1] == numbers[2]:
        print('Yes')
        exit(0)
    elif numbers[0]^numbers[2] == numbers[1]:
        print('Yes')
        exit(0)
    elif numbers[1]^numbers[2] == numbers[0]:
        print('Yes')
        exit(0)
    else:
        print('No')
else:
    if len(a) != a.count(numbers[0])+a.count(numbers[1]):
        print('No')
        exit(0)
    if numbers[0] == 0 or numbers[1] == 0:
        if numbers[0] == 0:
            if a.count(numbers[1]) != 2*a.count(numbers[0]):
                print('No')
                exit(0)
        elif a.count(numbers[0]) != 2*a.count(numbers[1]):
            print('No')
            exit(0)
        print('Yes')
        exit(0)
    else:
        print('No')
        exit(0)   
       
    