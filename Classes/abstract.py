from abc import ABC,abstractmethod

class Polygon(ABC):
    def whatIsThis(self):
        print("this is a polygon.")
    @abstractmethod
    def numberOfSides(self):
        pass

class Triangle(Polygon):
    def numberOfSides(self):
        print("A triangle has 3 sides.")

class Pentagon(Polygon):
    def numberOfSides(self):
        print("A pentagon has 5 sides")

triangle=Triangle()
pentagon=Pentagon()
triangle.numberOfSides()
triangle.whatIsThis()
pentagon.numberOfSides()
pentagon.whatIsThis()