no=int(input("enter number:"))
num=no
sum=0
mul=1
while no>0:
    r=int(no%10)
    sum=sum+r
    mul=mul*r
    no=int(no/10)
print("sum=",sum)
print("mul=",mul)
if sum==mul:
    print("%d is twin number"%num)
else:
    print("%d is not twin number"%num)
    
