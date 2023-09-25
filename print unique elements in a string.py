myString = input("enter the string:")
uniqueChars = ""
for a in myString:
    if a not in uniqueChars:
        uniqueChars=uniqueChars+a
for a in uniqueChars:
    print(a,end="")