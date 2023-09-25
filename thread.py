from threading import *
import time
def double(numbers):
    for n in numbers:
        time.sleep(1.5)
        print("double",2*n)
def square(numbers):
    for n in numbers:
        time.sleep(1.7)
        print("square",n*n)
numbers=[1,2,3,4,5]
begintime=time.time()
# double(numbers)
# square(numbers)
# print("total time is",time.time()-begintime)
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=square,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("total time is",time.time()-begintime)