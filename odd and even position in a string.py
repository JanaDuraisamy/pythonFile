s=input("Enter the string:")
i=0
print("To print even position in a string")
while i<len(s):
    print(s[i],end="-")
    i=i+2

print()
print("To print odd position in a string")
i=1
while i<len(s):
    print(s[i], end=",")
    i=i+2

