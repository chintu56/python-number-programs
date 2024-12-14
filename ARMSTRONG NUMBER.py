num=int(input("enter the number:"))
pow=len(str(num))
res=0
tem=num
while tem>0:
    dig=tem%10
    res=res+dig**pow
    tem=tem//10
if(num==res):
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")

