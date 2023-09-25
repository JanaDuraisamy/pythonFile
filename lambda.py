# Lambda argumentlist, expression
s=lambda n:n*n
print("the square of 4 is:",s(4))
print("the square of 55 is",s(55))
# addition of two numbers
add=lambda a,b:a+b
print("the sum of two numbers:",add(99,3))
#BIGGEST OF GIVEN VALUE
big=lambda a,b:b if a>b else b
print("the biggest value is:",big(23,24))
# LAMBDA METHODS
_______________________________
# 1.Filter()
l=[0,5,10,15,20,25,30,35,40,45,50]
res=list(filter(lambda x: x%2!=0,l))
print(res)
# 2.Map()
l=[1,2,3,4,5,6,7]
res1=list(map(lambda x:x*2,l))
print(res1)
# 3.reduce()
from functools import *
l=[10,20,30,40,50]
o=reduce(lambda x,y:x+y,l)
print(o)