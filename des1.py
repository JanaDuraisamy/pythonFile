# import time
# class Test:
#     def __init__(self):
#         print("constructor execution")
#     def a(self):
#         print("gfdf")
#     def __del__(self):
#         print("full fill my last wish and perform cleanup")
# s=Test(),Test(),Test()
# del s
# time.sleep(3)
# print("End of my application")

import time
class Test:
    def __init__(self):
        print("object intialization")
    def __del__(self):
        print("database connection close")
t=Test()
del t
time.sleep(5)
print("end of my program")