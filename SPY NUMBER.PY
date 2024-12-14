n=int(input())
sum=0
pro=1
temp=n
while temp>0:
    rem=temp%10
    sum=sum+rem
    pro=pro*rem
    temp=temp//10
if sum==pro:
    print("spy number")
else:
    print("not a spy number")