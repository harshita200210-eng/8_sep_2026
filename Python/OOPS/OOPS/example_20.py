class Address:
    def __init__(self,city,state):
         self.city = city
         self.state = state

class Emp:
     def __init__(self,emp_name,address):
          self.emp_name = emp_name
          self.address = address

a1 = Address("AHM","GUJ")
e1 = Emp("Mittal",a1)

print(e1.emp_name)
print(e1.address.city)
                   
        