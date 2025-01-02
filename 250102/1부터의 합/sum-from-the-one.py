n=int(input())

sum_val=0
for i in range(1,101,1):
    if (sum_val+i)>n:
        print(sum_val)
        break
    sum_val+=i
    