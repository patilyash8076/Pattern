for i in range(1,6):        #i = 1,2,3,4,5
    for j in range(6-i):   #j = 5,4,3,2,1
        print(' ',end='')
    for k in range(i):
        print('*', end="")
    print('\n')
