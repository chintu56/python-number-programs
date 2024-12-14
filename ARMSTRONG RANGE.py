start=int(input("enter the starting number:"))
end=int(input("enter the ending number:"))
for num in range(start,end):
    pow=len(str(num))
    res=0
    tem=num
    while tem>0:
        digit=tem%10
        res=res+digit**pow
        tem=tem//10
    if(num==res):
        print(num)