class Parent:
    def display(self):
        print("parent class here...")

class Child(Parent):
    def display(self):
        Parent.display(self)
        print("child class here...")

obj = Child()

obj.display()