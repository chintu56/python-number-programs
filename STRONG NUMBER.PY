n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    temp=temp//10
if sum==n:
    print("STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")