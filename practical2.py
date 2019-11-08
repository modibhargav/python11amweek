a=int(input("enter a number :"))
i=1
sum1=0
sum2=0
while(i<=a):
    if i%2==0:
        print("even",i)
        sum1+=i
    else:
        print("odd",i)
        sum2+=i
    i+=1    
print("sum of even",sum1)
print("average of even :",sum1/a)
print("sum of odd",sum2)
print("average of odd :",sum2/a)
