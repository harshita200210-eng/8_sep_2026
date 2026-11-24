class Sample:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

obj = Sample([12,23,34,54,65,34])

print(len(obj))
        