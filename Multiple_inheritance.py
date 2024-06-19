class Vehicle:

    def __init__(self, price, vehicle_type = "none"):
        self.vehicle_type = vehicle_type
        super().__init__(price)



class Car:

    def __init__(self,  price=1000000):
        self.price = price

    def horse_powers(self, power):
        return power


class Nissan(Vehicle, Car):

    def __init__(self, price, vehicle_type):
        super().__init__(price, vehicle_type)



avto1 = Nissan(5000, 'Nissan')
print(avto1.price)
print(avto1.vehicle_type)
print(avto1.horse_powers(123))


