num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
        #print(sum)
num2=sum
print(num2)
sum2=0
for j in range(1,num2):
    if num2%j==0:
        sum2=sum2+j
        #print(sum2)
print(sum2)
if sum2==num:
    print("AMECABLE NUMBER PAIR")
else:
    print("NOT A AMECABLE NUMBER PAIR")