class Car:
    wheel="Four Wheels"
    def __init__(self,name,model,price,milage):
        self.name=name
        self.model=model
        self.price=price
        self.milage=milage
    def details(self):
        print("Car name:",self.name)
        print("It's latest model:",self.model)
        print("It's price:",self.price)
        print("Milage given:",self.milage)
    @classmethod
    def getwheel(cls):
        return cls.wheel
    @staticmethod
    def getinfo():
        print("Congratulations on your new car!, I hope your car takes you to all the good places")

c1=Car("Rolls-Royce","Phantom","10.48cr","9.8 kmplit")
c2=Car("BMW","Bmw ix1","60 lak","20 kmplit")
c3=Car("volkswagen","volkswagen virtus","10.48 lak","20 kmplit")
c1.details()
c2.details()
c3.details()
print(Car.getwheel())
print(Car.getinfo())

# class Bike:
#     count = 0
#     def __init__(self,name,model,price,milage):
#         self.name=name
#         self.model=model
#         self.price=price
#         self.milage=milage
#         Bike.count+=1
#
#     def details(self):
#         print("Bike name:",self.name)
#         print("Bike model:",self.model)
#         print("Its price:",self.price)
#         print("Milage given:",self.milage)
# b1=Bike("Yamaha","MT-15 v2","2 lak","56 kmpl")
# b2=Bike("Royal enfield","classic 350","1.56 lak","45 kmpl")
# b3=Bike("Yamaha","R 15 v4","1.97 lak","55 kmpl")
# b1.details()
# b2.details()
# b3.details()
# print("total number of objects are created:",Bike.count)