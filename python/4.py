
n=int(input("enter value of n"))
x=int(input("enter value of x"))

sum=1
for i in range(1,n):
    sum=sum+(x**i)/i
    print(sum)

