class Vehicle:
    _wheels = 0
    _storage = {}

    def __init__(self, wheels, storage):
        self._wheels = wheels
        self._storage = storage

    def getWheels(self):
        return self._wheels
    def getStorage(self):
        return self._storage
    def setStorage(self, value):
        self._storage = value    

class PartVehicle(Vehicle):
    def __add__(self, secondVehicle):
        return PartVehicle(self.getWheels() + secondVehicle.getWheels(), self.getStorage() | secondVehicle.getStorage())
    def __eq__(self, secondVehicle):
        return self.getWheels() == secondVehicle.getWheels() and self.getStorage() == secondVehicle.getStorage()
    def __len__(self):
        return self.getWheels()

if __name__ == "__main__":
    cars = [ PartVehicle(4, {}) ]
    cars.append(PartVehicle(6, {'a','c','d'}))
    part3 = PartVehicle(2, {1,2,3})
    part4 = PartVehicle(2, {3, 4})
    cars.append(part3 + part4)

    print('Cars count:', len(cars))
    for car in cars:
        print('Car number', cars.index(car)+1, 'has', car.getWheels(), 'wheels and carring', car.getStorage())
        