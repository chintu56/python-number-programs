num=int(input())
temp=num
while temp>=10:
    sum=0
    while temp>0:
        rem=temp%10
        sum=sum+rem
        temp=temp//10
    temp=sum
if sum==1:
    print("MAGIC NUMBER")
else:
    print("NOT A MAGIC NUMBER")