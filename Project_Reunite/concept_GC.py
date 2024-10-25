import gc
import sys
import time


class Test:
    def m1(self):
        pass


t = Test()
print(id(t))
t1 = t
t2 = t1
t3 = t2
t4 = t3

print(sys.getrefcount(t4))


class Test:

    def __init__(self):
        print("parent constructor running")

    def __del__(self):
        print("parent destructor running")

    def m1_Test(self):
        print("parent class m1_test")


t1 = Test()
print(id(t1))
print("hello statement")

t1.m1_Test()

t2 = t1
print(sys.getrefcount(t2))

t1 = None
t2 = None  # If objects are finished there itself Destructor runs the Programme

print("please end the Application")
