def Cal():
    num=input()
    num=num.split()
    a=int(num[0])
    b=int(num[1])
    a+=b
    b+=a
    print(a,b)
Cal()