import math

def Fat():
    h,w=map(int,input().split())
    b=w/((h/100)**2)
    print(math.floor(b))
    if b>=25:
        print("Obesity")
Fat()
