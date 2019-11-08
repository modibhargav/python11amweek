no=int(input("enter number:"))
rev=0
while no>0:
    r=int(no%10)
    rev=rev*10+r
    no=int(no/10)
print("rev=",rev)
