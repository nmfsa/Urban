class Car:
    price = 1000000

    def horse_powers(self, horse_power):
        return horse_power


class Nissan(Car):
    price = 5000

    def horse_powers(self, horse_power):
        return horse_power


class Kia(Car):
    price = 7000

    def horse_powers(self, horse_power):
        return horse_power


car = Car()
print(car.price, '\n',  car.horse_powers(666))

nissan = Nissan()
print(nissan.price, "\n", nissan.horse_powers(333))

kia = Kia()
print(kia.price, '\n', kia.horse_powers(222))
