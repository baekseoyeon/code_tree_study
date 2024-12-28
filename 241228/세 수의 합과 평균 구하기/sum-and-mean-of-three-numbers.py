def Cal():
    num=input()
    num=num.split()
    a=int(num[0])
    b=int(num[1])
    c=int(num[2])
    print(a+b+c)
    print(round((a+b+c)/len(num)))
Cal()