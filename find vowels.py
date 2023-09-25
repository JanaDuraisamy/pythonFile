# string = input( "Type in a string: " )
# vowels = "a", "e", "i", "o", "u"
# for i in string:
#     if i in vowels:
#         print(i,"is vowel")
#     else:
#         print(i,"is consonent")

string = input("Type in a string: ")
vowels = "a", "e", "i", "o", "u"
indices = ""
for i in string:
    if i in vowels:
        indices += i
print(indices)
