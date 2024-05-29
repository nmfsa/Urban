class Buiding:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors


buiding1 = Buiding(10, 'сталинка')
buiding2 = Buiding(10, 'сталинка')

print(buiding2 == buiding1)  # результат был бы False без перегрузки метода equal
