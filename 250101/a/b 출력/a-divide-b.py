a,b=map(int,input().split())

print(f"{a//b}.",end='')

num=((a%b)*10)//b #몫
num1=((a%b)*10)%b #나머지
for i in range(20):
    print(num,end='')
    num1*=10
    num=num1//b
