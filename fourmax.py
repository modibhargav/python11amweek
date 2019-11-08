a=int(input("Enter Num1 :"))
b=int(input("Enter Num2 :"))
c=int(input("Enter Num3 :"))
d=int(input("Enter Num4 :"))
if a>b:
    if a>c:
        if a>d:
            print("%d is max"%a)
        else:
            print("%d is max"%d)    
elif b>c:
    if b>d:
        print("%d is max"%b)
elif c>d:
    print("%d is max"%c)
else:
    print("%d is max"%d)
    
    
