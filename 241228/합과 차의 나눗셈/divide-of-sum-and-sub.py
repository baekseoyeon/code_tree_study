def Cal():
    num=input()
    num=num.split()
    a=int(num[0])
    b=int(num[1])
    print(f"{(a+b)/(a-b):.2f}")

Cal()
