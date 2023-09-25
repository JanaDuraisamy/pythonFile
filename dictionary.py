# square={x:x*x for x in range(1,6)}
# print(square)

# d={}
# m=0
# s=""
# while True:
#     print("--Type 1 to continue (OR) 0 to Stop--")
#     a=int(input(""))
#     if(a==1):
#         s=input("Enter the student name:")
#         m=int(input("Enter the mark:"))
#         d[s]=m
#         continue
#     else:
#         break
#
# print("--Enter the student name to get marks--")
# g=(input(""))
# g1=d[g]
# print(g1)

# n=int(input("Enter number of students:"))
# d={}
# for i in range(n):
#     name=input("Enter student name:")
#     marks=int(input("Enter student marks:"))
#     d[name]=marks
# while True:
#     name=input("Enter student name to get marks:")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("Student name not found")
#     else:
#         print("Mark of",name,"are",marks)
#     option=input("Do you want to find another student marks [yes/no]:")
#     if option=="no":
#         print("Thanks for using our application")
#         break

word=input("Enter the string:")
d={}
for i in word:
    d[i]=d.get(i,0)+1
    print(d)

