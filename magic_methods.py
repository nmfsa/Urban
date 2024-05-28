class House:
    def __init__(self, numberOfFloors=0):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors(10)
print(my_house.numberOfFloors)  # проверка значения numberOfFloors
