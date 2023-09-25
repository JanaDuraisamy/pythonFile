# input="one two three four five six seven"
# output="one owt three ruof five xis seven"
s=input("enter the string:")
l=s.split()
print(l)
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output="".join(l1)
print("the original string is",s)
print("the result is:",output)