def Score():
    A_e,A_m = map(int,input().split())
    B_e,B_m = map(int,input().split())

    if A_m>B_m and A_e>B_e:
        print("1")
    else:
        print("0")

Score()