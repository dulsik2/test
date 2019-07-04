#4 : 나
n = int(input('>>'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(1,n):
    print(' '*i,end='')
    for j in range(n-i):
        print('*',end=' ')
    print()

#4 : 답지 + 나 쪼끔~
number_of_stars, number_of_space= 1, n - 1
for i in range(2 * n - 1) :
    for j in range(number_of_space) :
        print(end = ' ')
    for j in range(number_of_stars) :
        print('*',end=' ')
    print()
    if i < n-1 :
        number_of_stars += 1
        number_of_space -= 1
    else :
        number_of_stars -= 1
        number_of_space += 1