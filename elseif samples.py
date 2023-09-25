# a=int(input("enter the num1:"))
# b=int(input("enter the num2:"))
# c=int(input("enter the num3:"))
# if a>=b & a>c:
#     print("A is biggest of all",a)
# elif b>a & b>=c:
#     print("B is biggest of all",b)
# elif c>=a & c>b:
#     print("C is biggest of all",c)
# else:
#     print("All values are equal")
#
# p=int(input("Enter the num1:"))
# q=int(input("Enter the num2:"))
# r=int(input("Enter the num3:"))
# s=int(input("Enter the num4:"))
# if p<=q and p<r and p<s:
#     print("P is smallest number",p)
# elif q<=r and q<s and q<p:
#     print("Q is smallest number",q)
# elif r<=s and r<p and r<q:
#     print("R is smallest number",r)
# elif s<p and s<q and s<r:
#     print("S is smallest number",s)
# else:
#     print("All the values are same!")

# num=int(input("Enter any number:"))
# if 80<= num <=100:
#     print("You are passed in First grade")
# elif 60<= num <=80:
#     print("You are passed in second grade")
# elif 40<= num <=60:
#     print("You are passed in third grade")
# else:
#     print("Sorry, you are fail")

# name=input("Enter ur name:")
# rollno=int(input("Enter ur register number:"))
# age=int(input("Enter ur age:"))
# bloodgrp=input("Enter ur blood group:")
# address=int(input("Enter ur Address:"))
m1=int(input("Enter ur Tamil mark:"))
m2=int(input("Enter ur English mark:"))
m3=int(input("Enter ur Maths mark:"))
m4=int(input("Enter ur Science mark:"))
m5=int(input("Enter ur Social mark:"))
sum=m1+m2+m3+m4+m5
print("Your total mark is:",sum,"out of 500")
avg=sum/5
print("Your percentage is:",avg)
if 80<= avg <=100:
    print("You are passed in first grade!",avg)
elif 60<= avg <=80:
    print("You are passed in second grade",avg)
elif 40<= avg <=60:
    print("You are passed in third grade",avg)
elif 0<= avg <=40:
    print("Sorry, You are fail!")
else:
    print("Thank you!")


