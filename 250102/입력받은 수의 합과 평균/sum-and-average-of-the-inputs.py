n=int(input())

sum_val=0
cnt=0
for i in range(n):
    c=int(input())
    sum_val+=c
    cnt+=1

print(sum_val, f"{sum_val/cnt:.1f}")