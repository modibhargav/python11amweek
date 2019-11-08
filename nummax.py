x=int(input("Enter Num1 :"))
y=int(input("Enter Num2 :"))
z=int(input("Enter Num3 :"))
if x>y:
    if x>z:
        print("%d is max"%x)
    else:
        print("%d is max"%z)
elif y>z:
    print("%d is max"%y)
else:
    print("%d is max"%z)
