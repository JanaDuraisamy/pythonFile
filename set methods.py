s={10,20,30,40}
s.add(50)
print(s)
s2={10,20,30,40,50}
s2.remove(50)
print(s2)
# s={10,20,30,40,50}
# s.remove(50)
# s.remove(50)
# print(s)
s1={1,2,3,4,5,7}
s1.discard(7)
s1.discard(7)
print(s1)
s3={4,5,6}
l=[10,11,21]
s3.update(l)
print(s3)
# s4={31,32,33}
# s4.update(34)
# print(s4)
s5={1,35,6,9}
s5.clear()
print(s5)
x={10,20,30,40}
y={30,40,50,60}
print("union:",x|y)
print("diff:",x-y)
print("diff:",y-x)
print("intersection:",x&y)
