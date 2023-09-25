class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Engine specification")
class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print("car using engine class function")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=Car()
c.m2()

# class College:
#     clg_name="MCAS"
#     def __init__(self):
#         self.dname="Bsc.CS"
#         self.hod="Subramani"
#     def a1(self):
#         print("There are 20+ academic courses are provided")
#         print("new courses are available like Bsc IT")
#
# class Dept:
#     def __init__(self):
#         self.clg=College()
#     def a2(self):+
#
#         print(self.clg.clg_name)
#         print(self.clg.dname)
#         print(self.clg.hod)
#         self.clg.a1()
# d=Dept()
# d.a2()