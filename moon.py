weight_earth=float(input("Enter Your Weight :"))
if weight_earth<=0:
    print("Enter a Valid Weight")
else:
    Weight_moon=(weight_earth/9.81)*1.622
    print("Your Weight On Moon is :",Weight_moon)
    
