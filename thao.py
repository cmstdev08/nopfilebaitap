# Câu 1
a= input("Enter your full name: ")
print("Hello",a,"!!!") 
# Câu 2
r=float(input("Input the radius of the circle line:"))
p=3.14
s=p*r**2
c=2*r*p
print("The area of a circle with a radius of",r,"is:",s)
print("The circumference of a circle with a radius of",r,"is:",c)
# Câu 3
import math 
print("Enter the two sides of a square triangle:")
a=float(input())
b=float(input())
c=math.sqrt(a**2+b**2)
print("The first side is:",a,",the second side:",b,",the is a district side=",round(c, 2))
# Câu 4
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
sum=a+b+c+d
average=sum/4
print("Sum=",sum,)
print("Average=",average)
# Câu 5
n=int(input("Initial amount: "))
k=int(input("Savings months: "))
T=float(input("Interest rate/month: "))
m=n*(1+k*T)
print("With an initial amount of",n,",after",k,"months of deposit, the interest rate is",T,"/month")
print("The amount received at the end of the strange: ",m)
# Câu 6
a=input("Full Name: ")
b=float(input("Number of working days: "))
c=float(input("Unit price of workday: "))
d=float(input("Coefficient: "))
e=float(input("Advance: "))
l=c*b*d
t=l-e
print(f"Employee {a}, With Salary={round(l, 1)}, Advance={e} and Actual amount received={round(t, 1)}")