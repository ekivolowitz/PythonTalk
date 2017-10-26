
nationality = "US"

class dollar():
    def __init__(self, **kwargs):
        if value:
            self.value = value
        else:
            self.value = 0
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def __add__(self, otherValue):
        return self.value + otherValue.getValue()
    def add(self, otherValue):
        return self.value + otherValue.getValue()
    def __sub__(self, otherValue):
        return self.value - otherValue.getValue()

if __name__ == "__main__":
    d1 = dollar()
    d2 = dollar(5)
    d1.add(d2)
    # d3 = dollar(value = 10, nation = "US")
    d1.setValue(10)

    print("d1 + d2 = {0}".format(d1 + d2))

from math import pi as p
    