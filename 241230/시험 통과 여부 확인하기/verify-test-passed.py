n=int(input())

if n >= 80:
    print("pass")
elif 0 <= n < 80:
    print(f"{80-n} more score")
else:
    print("input must be a int type.")