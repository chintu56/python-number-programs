start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
for num in range(start,end+1):
    #num=int(input())
    #print(num)
    num_sq=num**2
    #print(num_sq)
    sum=0
    temp=num
    while temp>0:
        rem=temp%10
        sum=sum*10+rem
        temp=temp//10
    num_rev=sum
    #print(num_rev)
    num_rev_sq=num_rev**2
    #print(num_rev_sq)
    tem=str(num_rev_sq)
    tem1=tem[::-1]
    num_rev_sq_rev=int(tem1)
    #print(num_rev_sq_rev)
    if num_sq==num_rev_sq_rev:
        #print("ADAM NUprintMBER")
        print(num)
    #else:
        #1print("NOT A ADAM NUMBER")


