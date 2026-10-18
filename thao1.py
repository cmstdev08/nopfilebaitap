#Câu 1
import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Area={s:.3f}")
else:
    print("Invalid")
#Câu 2
a=float(input("M1="))
b=float(input("M2="))
c=float(input("M3="))
d=float(input("S="))
if d <= 100:
    tien=d*a
elif d <=150:
    tien=100*a+(d-100)*b
else:
    tien=100*a+50*b+(d-150)*c
print(f"Bill={tien:g}")
#Câu 3
a=float(input("x="))
b=float(input("y="))
ch=input("Operation:")
x=f"{a:g}"
y=f"{b:g}"
if ch=="+":
    print(f"{x}+{y}={a+b:.1f}")
elif ch=="-":
    print(f"{x}-{y}={a-b:.1f}")
elif ch=="*":
    print(f"{x}*{y}={a*b:.1f}")
elif ch=="/":
    if b!=0:
        print(f"{x}/{y}={a/b:.1f}")
    else:
        print("Invalid")
else:
    print("Invalid")
#Câu 4
toan = float(input(""))
ly = float(input(""))
hoa = float(input(""))
if toan < 0 or toan > 10 or ly < 0 or ly > 10 or hoa < 0 or hoa > 10:
    print("Invalid")
else:
    tb = (toan * 2 + ly * 3 + hoa) / 6
    if tb < 3:
        print("Poor")
    elif tb < 5:
        print("Weak")
    elif tb < 6:
        print("Average")
    elif tb < 7:
        print("Fair")
    elif tb < 8:
        print("Good")
    elif tb < 9:
        print("Very Good")
    else:
        print("Excellent")
#Câu 5
a = int(input())
if a < 0:
    print("Invalid")
elif a == 0:
    print("Grade A")
elif a < 2:
    print("Grade B")
elif a < 4:
    print("Grade C")
else:
    print("Grade D")
#Câu 6
a=float(input())
b=float(input())
c=float(input())
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print("Invalid")
elif a==b and b==c:
    print("Equilateral triangle")
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("Square triangle")
else:
    print("Ordinary triangle")