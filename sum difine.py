no=int(input("enter the number:"))
mul=1
while no>0:
    r=int(no%10)
    mul=mul*r
    no=int(no/10)
print("mul=",mul)
          
