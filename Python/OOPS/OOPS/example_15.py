from abc import ABC,abstractmethod

class Sample(ABC):
    @abstractmethod
    def dispaly(self):
        pass


class Child(Sample):
    def dispaly(self):
        pass

obj = Child()
obj.dispaly()
