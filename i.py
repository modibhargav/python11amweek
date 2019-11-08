P=int(input("Enter Price :"))
R=int(input("Enter Rate  :"))
N=int(input("Enter Number :"))

if P<=0:
    print("Enter Valid  Price")

elif R<=0:
    print("Enter Valid  Rate")

elif N<=0:
    print("Enter Valid  Number")

else :
    i=(P*R*N)/100
    print("Your Intersest is",i)
