n=int(input())

for i in range(n,101,1):
    if i>89:
        print('A',end=' ')
    elif i>79:
        print('B',end=' ')
    elif i>69:
        print('C',end=' ')
    elif i>59:
        print('D',end=' ')
    else:
        print('F',end=' ')
    i+=i