s1=input("Enter the string 1:")
s2=input("Enter the string 2:")
output=""
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)
# end="" used to print the output in a single or same line