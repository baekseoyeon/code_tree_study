age_sum=0
cnt=0
while True:
    n=int(input())
    if 19<n<30:
        age_sum+=n
        cnt+=1
    else:
        print(f"{age_sum/cnt:.2f}")
        break
    