"""method overloading not possible
note:: python does not support method overloading concept
"""

class student:
    def display(self):
        print("this is display 1")

    def display(self,num1):
        self.num1 = num1

obj = student()

obj.display()