for i in range(5,0,-1):     #5,4,3,2,1
    for j in range(5-i):    #0,1,2,3,4   spaces
        print(' ',end='')
    for k in range(i):      # 5,4,3,2,1  pattern printing
        print('*',end='')
    print('\n')
