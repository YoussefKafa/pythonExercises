
def first():
    car="BMW"
    print("Inside first before calling second car was : "+ car)
    def second():
        nonlocal car
        car = "Toyota"
        print("Inside second, car is: "+car)
    second()
    print("Outside second, car is: "+car)
car="Honda"
print(car)
first()