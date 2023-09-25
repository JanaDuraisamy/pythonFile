# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eatndrink(self):
#         print("Eat briyani and drink")
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#     def work(self):
#         print("Coding in python")
#     def empinfo(self):
#         print("Emp name:",self.name)
#         print("Emp age:",self.age)
#         print("Emp number:",self.eno)
#         print("Emp salary:",self.esal)
# e=Employee("Dharshan",20,45,50000)
# e.eatndrink()
# e.work()
# e.empinfo()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    # __str__ magic methods
    def __str__(self):
       return "Name={},Age={},Eno={},Esal={}".format(self.name,self.age,self.eno,self.esal)
e=Employee("dharshan",20,45,70000)
d=Employee("jana",9,5,80000)
print(e)
print(d)

# d=2*"u"
# print(d)