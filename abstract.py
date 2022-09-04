from abc import ABC,abstractmethod

class Polygon(ABC):
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
pentagon.numberOfSides()