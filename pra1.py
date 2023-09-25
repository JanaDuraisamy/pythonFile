# s1=input("enter the string1:")
# s2=input("enter the string2:")
# i,j=0,0
# output=""
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i=i+1
#     if j<len(s2):
#         output=output+s2[j]
#         j=j+1
# print(output)
import pandas as pd
data={
    "name":["dharshan","karthi","suriya"],
    "age":[20,35,42],
    "place":["salem","rasipuram","pattikaadu"]
}
df=pd.DataFrame(data)
print(df)
filteringdf = df[df['age']>25]
print(filteringdf)