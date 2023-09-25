# s1=input("enter the string:")
# l=s1.split()
# print(l)
# l1=[]
# i=len(s1)-1
# while i<0:
#     l1.append(l[i])
#     i=i+1
# output="".join(l1)
# print(output)
s=input("Enter the string:")
l=s.split()
print(l)
target=""
i=len(s)-1
while i>=0:
    target=target+s[i]
    i=i-1
print(target)
