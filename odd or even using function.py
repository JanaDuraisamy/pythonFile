def oddeven(num):
    for i in num:
        if i%2==0:
            print("The given number is even",i)
        else:
            print("The given number is odd",i)
# num1=[i*i for i in range(1,11)]
num1=[1,2,11,55,68,63,44,3,4,5]
# num1=int(input("Enter the number:"))
oddeven(num1)

