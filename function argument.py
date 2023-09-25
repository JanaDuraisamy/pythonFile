# print('positional argument')
# def add(x,y):
#     return x+y
# result=add(200,6)
# print("the sum is:",result)
# keyword argument
# default argument
# def wish (name="Guest"):
#     print("Hello",name,"gud afternoon")
# wish("Hari")
# wish()
# # variable length argument
# def sum(*n):
#     total=0
#     for i in n:
#         total=total+i
#     print("the sum is:",total)
# sum()
# sum(10)
# sum(10,20,30,40,50)
# keyword variable length argument
def abc(*n, **data):
    print(n)
    print(data)
    for x in n:
        print(x)
        for k,v in data.items():
            print(k,v)
abc('ram','gokul',age=20,city="salem")
#
#
