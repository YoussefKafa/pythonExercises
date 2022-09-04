class MyClass:
    a=1
    def sayHi(self):
        print("Hi!")
myC=MyClass()
print(myC.a)
print(MyClass.a)
myC.sayHi()
MyClass.sayHi(myC)
print(myC.sayHi()) #it will print Hi! then None because the function does not return anything

#Let's learn how to create a custom object

class FastFood():
    def __init__(self,name,items,time_to_prepare) -> None:
        self.name=name
        self.items=items
        self.time_to_prepare=time_to_prepare
    def __str__(self) -> str:
        return ("the "+self.name+" contains :"+str(self.items)+" and takes "+str(self.time_to_prepare)+" to prepare.")

pizza=FastFood("pizza",["bread","tomato sauce","cheese"],45)
burger=FastFood("burger",["Bun","beef","cheese"],10)
print(pizza.__str__())
print(burger.__str__())
