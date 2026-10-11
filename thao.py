# Câu 1
a= input("Enter your full name: ")
print("Hello",a,"!!!") 
# Câu 2
r=float(input("Input the radius of the circle line: "))
p=3.14
s=p*r**2
c=2*r*p
print(f"The area of a circle with a radius of {r:g} is: {round(s, 1)}")
print(f"The circumference of a circle with a radius of {r:g} is: {round(c, 1)}")
# Câu 3
import math 
print("Enter the two sides of a square triangle:")
a=float(input())
b=float(input())
c=math.sqrt(a**2+b**2)
print(f"The first side is: {a:g}, the second side: {b:g}, there is a district side = {round(c, 2)}")
# Câu 4
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
s=a+b+c+d
tb=s/4
print(f"Sum={s}")
print(f"Average={tb}")
# Câu 5
n=float(input("Initial amount: "))
k=int(input("Savings months: "))
T=float(input("Interest rate/month: "))
m=n*(1+k*T)
print(f"With an initial amount of {n:g}, after {k} months of deposit, the interest rate is {T:g}/month")
print(f"The amount received at the end of the strange: {m}")
# Câu 6
a=input("Full Name: ")
b=float(input("Number of working days: "))
c=float(input("Unit price of workday: "))
d=float(input("Coefficient: "))
e=float(input("Advance: "))
l=c*b*d
t=l-e
print(f"Employee {a}, With Salary={round(l, 1)}, Advance={e:g} and Actual amount received={round(t, 1)}")