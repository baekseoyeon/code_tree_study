# n=int(input())
# for i in range(1,n+1,1):
#     if i in [3,6,9]:
#         print('0',end=' ')
#     else:
#         print(i,end=' ')

n=int(input())
i=1
while i<n+1:
    if any(c in str(i) for c in ['3','6','9']) or (i%3==0):
        print('0',end=' ')
    else:
        print(i,end=' ')
    i=int(i)
    i+=1