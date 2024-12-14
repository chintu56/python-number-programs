num=int(input("enter the number:"))
res=0
tem=num
while tem>0:
    dig=tem%10
    res=res*10+dig
    tem=tem//10

if(num==res):
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")