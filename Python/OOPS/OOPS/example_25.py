class Sample:
    def __init__(self,products):
       self.product = products

    def __getitem__(self,index):
        return self.product[index]

obj = Sample(["iphone","13000"])  

print(obj[0])
print(obj[1])