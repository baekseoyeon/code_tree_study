count_3=0
count_5=0

for i in range(10):
    n=int(input())
    if n%3==0:
        count_3+=1
    if n%5==0:
        count_5+=1

print(count_3,end=' ')
print(count_5)