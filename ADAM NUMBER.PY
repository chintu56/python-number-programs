"""
Adam number is a number when reversed, the square of the number and 
the square of the reversed number should be numbers which are reverse of each other.
 For Example : (12)^2 = 144 (21)^2 = 441 144 is the reversed of 441 441 is the reversed of 144 
 So, 12 is an Adam number..
 
"""

num=int(input("Enter the number:"))
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
    print("ADAM NUMBER")
else:
    print("NOT A ADAM NUMBER")

