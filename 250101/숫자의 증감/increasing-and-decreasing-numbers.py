c,n=input().split()
n=int(n)

if c=='A':
    i=1
    while i<n+1:
        print(i,end=' ')
        i+=1
else:
    i=n
    while n>0:
        print(i,end=' ')
        i-=1

