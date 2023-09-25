# print('---------Class Object with HardCode---------')
#
# class Student:
#     def __init__(self):
#         self.name="jana"
#         self.age=21
#         self.mark=80
#
#     def talk(self):
#         print("hii i am",self.name, "i am",self.age,'years old', "my marks is",self.mark)
#         # print("i am",self.age,'years old')
#         # print("my marks is",self.mark)
# s=Student()
# s.talk()
#
# print("   ")
# print('---------Class Object with SoftCode---------')
#
# class Student:
#     def __init__(self,name,rollno,mark):
#         self.name=name
#         self.rollno=rollno
#         self.mark=mark
#
#     def talk(self):
#         print("hello my name is",self.name)
#         print("rollno:",self.rollno)
#         print("mark:",self.mark)
#
# s1=Student("Jana",100,80)
# s2=Student("Hari",103,79)
# s3=Student("Karthi",102,78)
# s2.talk()
# s3.talk()
# s1.talk()

# print("         ")
# print("____________class object with softcode(assignment)__________")
# class Car:
#     def __init__(self,name,model,):
#         self.name=
#
#
#
# print("______Class object with class and static methods_____")
# class Student:
#     school="python class"
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         return(self.m1+self.m2+self.m3)/3
#     @classmethod
#     def getschool(cls):
#         return cls.school
#     @staticmethod
#     def info():
#         print("this is python class for you")
# jana=Student(40,70,80)
# dharshan=Student(60,78,93)
# print(dharshan.avg())
# print(jana.avg())
# print(Student.info())
# print(Student.getschool())

class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobjects(cls):
        print("Total no of objects created:",cls.count)
t1=Test()
t2=Test()
Test.noofobjects()
t3=Test()
Test.noofobjects()