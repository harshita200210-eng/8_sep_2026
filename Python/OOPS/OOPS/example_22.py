class Sample:
    def __init__(self,name):
        self.name  = name


    def __str__(self):
        return "object created {self.name}"

obj = Sample("Mital")

print(obj)