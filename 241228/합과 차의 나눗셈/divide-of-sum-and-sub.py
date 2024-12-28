def Cal():
    num=input()
    num=num.split()
    a=int(num[0])
    b=int(num[1])
    print(round((a+b)/(a-b),2))
Cal()
