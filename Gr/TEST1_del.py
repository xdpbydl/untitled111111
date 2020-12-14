class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'


my_car = Car('red', 37281)
# print(my_car)
# print(my_car.color, my_car.mileage)
# print(type(my_car.color), type(my_car.mileage))
print(str(my_car))
print(repr(my_car))