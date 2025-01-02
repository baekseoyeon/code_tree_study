n=int(input())

class_cnt=0
corridor_cnt=0
bathroom_cnt=0

for i in range(1,n+1):
    if i%12==0:
        bathroom_cnt+=1

    elif i%3==0:
        corridor_cnt+=1

    elif i%2==0:
        class_cnt+=1

print(class_cnt,corridor_cnt,bathroom_cnt)