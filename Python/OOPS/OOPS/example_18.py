"""
method overriding:

when parent and child both have same names method and same name arguments 
its called method overriding

in python method overriding concept working perfectly.

and as well as we can perform constructor overloading.

"""

class Parent:
    def __init__(self):
        print("parent constructor here...")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("child constructor here...")

obj = Child()