import math

a = float(input("Enter DS marks out of 100:"))
b = float(input("Enter DELD marks out of 100:"))
c = float(input("Enter OS marks out of 100:"))
d = float(input("Enter marks of ENTP out of 100:"))
e = float(input("Enter marks of UHV out of 100:"))

Total =(a+b+c+d+e)
per=(Total/5)

if per >= 75:
     print("Distinction")
elif per < 75 and per >= 60:
     print("First class")
elif per < 60  and per >= 50:
     print("second class")
elif per <50  and per >= 35:
     print("pass class")
elif per <35:
     print("Fail")
     
